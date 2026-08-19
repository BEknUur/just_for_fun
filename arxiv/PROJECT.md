# PROJECT.md

# ArXiv Research MCP

> Production-grade AI Research Assistant powered by MCP, LangGraph, and Telegram.

---

# Vision

The purpose of this project is to build a modular AI Research Assistant focused on Machine Learning papers while learning modern AI engineering practices.

This is **not** a simple Telegram bot.

This is a production-oriented AI system built around the following ideas:

- Model Context Protocol (MCP)
- Agent orchestration with LangGraph
- Tool calling
- Clean architecture
- Vendor-independent LLM support
- Extensibility
- Async-first Python

The system should be easy to extend with additional research providers without changing the core agent.

---

# Main Goals

## Educational Goal

Learn how production AI agents are built.

Understand:

- MCP
- LangGraph
- LangChain
- Agent orchestration
- Tool calling
- AI system architecture
- Async Python
- Production software engineering

---

## Product Goal

Create a personal AI research assistant capable of:

- searching papers
- understanding research topics
- generating literature reviews
- comparing papers
- following researchers
- monitoring new publications
- sending research digests

---

# Non Goals

The first version should NOT include:

- autonomous AGI
- complicated multi-agent systems
- code generation
- browser automation
- unnecessary abstractions

The MVP should remain simple.

---

# Guiding Principles

## 1. Modularity

Every component should have one responsibility.

Bad

Telegram Bot

↓

Business Logic

↓

Database

↓

LLM

↓

API

inside one file

Good

Telegram

↓

Agent

↓

MCP

↓

External API

---

## 2. MCP Owns External Systems

External systems should never be accessed directly from LangGraph.

Correct

LangGraph

↓

MCP Tool

↓

ArXiv API

Wrong

LangGraph

↓

HTTP Request

↓

ArXiv API

All external integrations should live inside MCP servers.

---

## 3. LangGraph Owns Workflow

LangGraph is responsible for:

- orchestration
- state
- routing
- retries
- decision making

LangGraph is NOT responsible for API integrations.

---

## 4. LLM Owns Reasoning

LLMs should only:

- understand user requests
- improve search queries
- rank papers
- summarize information
- compare research

LLMs should never:

- perform HTTP requests
- query databases directly
- access external APIs

---

## 5. MCP Tools Should Be Small

Each MCP tool should perform exactly one task.

Good

search_arxiv()

get_paper()

search_by_author()

Bad

research_everything()

---

## 6. JSON Everywhere

MCP should always return structured data.

Never markdown.

Never formatted text.

Never presentation logic.

Formatting belongs to the LLM.

---

# High-Level Architecture

```text
                    Telegram
                        │
                        ▼
                 Telegram Bot
                        │
                        ▼
              LangGraph Research Agent
                        │
                        ▼
                   MCP Client
                        │
                        ▼
               ArXiv MCP Server
                        │
                        ▼
                   ArXiv API
```

Future architecture:

```text
                    Telegram
                        │
                        ▼
               LangGraph Supervisor
                        │
      ┌─────────────────┼──────────────────┐
      ▼                 ▼                  ▼
 Research Agent     Review Agent      Memory Agent
      │                 │                  │
      └─────────────────┼──────────────────┘
                        ▼
                  MCP Client Layer
                        │
 ┌──────────┬────────────┼─────────────┬──────────────┐
 ▼          ▼            ▼             ▼              ▼
ArXiv   GitHub   HuggingFace   PapersWithCode   Semantic Scholar
```

---

# Current MVP

The MVP contains only:

Telegram

↓

LangGraph

↓

ArXiv MCP

↓

ArXiv API

Workflow

START

↓

Generate Search Query

↓

Search Papers

↓

Rank Papers

↓

Generate Summary

↓

END

---

# Directory Structure

```text
arxiv-research-mcp/

apps/
    telegram_bot/

agent/
    graph.py
    state.py
    nodes.py
    prompts.py
    llm.py

mcp_server/
    server.py
    arxiv_client.py
    tools.py
    schemas.py

mcp_client/
    client.py

core/
    config.py
    logging.py

tests/

README.md

PROJECT.md
```

---

# MCP Responsibilities

The MCP server wraps external APIs.

It should expose tools.

Example tools:

search_arxiv

get_paper

search_recent

search_by_author

download_pdf

extract_pdf

compare_papers

The MCP server should never contain prompt engineering.

---

# LangGraph Responsibilities

LangGraph owns the workflow.

Nodes should be deterministic.

Each node should have one responsibility.

Possible nodes:

GenerateQuery

↓

Search

↓

Filter

↓

Rank

↓

Summarize

↓

FormatOutput

↓

Finish

Every node receives state.

Every node returns updated state.

---

# State

Example state

user_query

search_query

papers

selected_papers

summary

error

The state should remain serializable.

Avoid storing LLM objects inside the graph state.

---

# LLM Layer

The LLM layer should be isolated.

The project must never depend on one provider.

Supported providers should include:

OpenAI

Anthropic

Gemini

DeepSeek

Qwen

Ollama

The code should allow replacing the provider with minimal changes.

A future LiteLLM integration should make model switching transparent.

---

# Telegram

Responsibilities

Receive commands

Display progress

Send summaries

Handle user interaction

No business logic should exist inside Telegram handlers.

---

# Coding Standards

Python 3.12+

Use uv

Use async

Use type hints

Use Ruff

Use Pytest

Use Pydantic

Use dependency injection where appropriate

Avoid global mutable state.

---

# Error Handling

Every external request should:

retry

timeout

log failures

return useful errors

Never crash the entire workflow.

---

# Logging

Every node should log:

start

finish

duration

errors

Every MCP tool should log:

tool name

execution time

arguments

status

---

# Future Roadmap

## Phase 1

MVP

Search papers

Generate summaries

Telegram bot

---

## Phase 2

PDF downloading

PDF parsing

Full paper summaries

---

## Phase 3

Research memory

Bookmarks

Reading history

Qdrant integration

---

## Phase 4

Subscriptions

Daily digests

Author tracking

Research alerts

---

## Phase 5

Additional MCP Servers

Semantic Scholar

Papers With Code

GitHub

HuggingFace

CrossRef

DOI lookup

---

## Phase 6

Multi-agent architecture

Planner

Researcher

Reviewer

Writer

Memory

Supervisor

---

# Long-Term Vision

The final goal is not only an ArXiv assistant.

The long-term goal is to build a modular AI Research Platform.

Every research provider should be implemented as an independent MCP server.

LangGraph should orchestrate those MCP servers without knowing their implementation details.

New capabilities should be added by attaching new MCP servers rather than modifying existing workflows.

The system should remain modular, maintainable, and provider-agnostic.

A future version should support:

- literature reviews
- trend analysis
- citation exploration
- researcher profiles
- paper recommendations
- research memory
- automatic research digests
- collaborative multi-agent workflows

The architecture should scale from a single-user Telegram assistant to a production research platform without requiring major redesign.
