# Project Context: ArXiv Research MCP

## Project Goal

We are building a production-quality AI Research Assistant focused on Machine Learning papers from arXiv.

This project is primarily for learning modern AI engineering concepts:

- Model Context Protocol (MCP)
- LangGraph
- LangChain
- Agent workflows
- Tool calling
- Telegram integration
- Async Python
- Production architecture

The goal is **not** simply to build another Telegram bot.

The goal is to understand how modern AI agents are architected and how MCP servers expose tools to LLMs.

---

# High-Level Architecture

```
Telegram
    │
    ▼
Telegram Bot (aiogram)
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

Responsibilities:

Telegram

- receives user requests
- sends responses

LangGraph

- orchestrates the workflow
- stores graph state
- decides which tool to call
- generates summaries

MCP Client

- connects LangGraph to one or more MCP servers

ArXiv MCP Server

- exposes research tools
- hides ArXiv API implementation

ArXiv API

- returns real paper metadata

---

# Current Scope (MVP)

We intentionally keep the first version small.

The first version should NOT include:

- memory
- vector databases
- RAG
- autonomous agents
- multi-agent systems
- PDF parsing
- long-term storage
- complex planning

The MVP should only search arXiv and summarize papers.

---

# Technologies

Package manager

- uv

Language

- Python 3.12+

Libraries

- MCP Python SDK
- LangGraph
- LangChain
- langchain-mcp-adapters
- aiogram
- httpx
- feedparser
- pydantic
- pydantic-settings
- python-dotenv

LLM

The architecture must be model-independent.

We do NOT want vendor lock-in.

The code should easily support:

- OpenAI
- Anthropic Claude
- Gemini
- Qwen
- DeepSeek
- Ollama

Ideally through LiteLLM later.

---

# Project Structure

```
arxiv-research-bot/

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

tests/

.env
pyproject.toml
README.md
```

---

# MCP Server

The MCP server is responsible only for exposing tools.

It should never contain business logic.

It wraps the ArXiv API.

Current tools:

search_arxiv()

get_paper()

search_by_author()

search_recent_papers()

Every tool should return structured JSON.

No markdown.

No formatted text.

The LLM is responsible for formatting.

---

# LangGraph Workflow

Current graph:

START

↓

Generate Search Query

↓

Search ArXiv (MCP)

↓

Rank Papers

↓

Generate Summary

↓

END

Every node should have one clear responsibility.

Nodes should be small and composable.

---

# Telegram Workflow

Example:

User:

/research agentic rag

↓

Telegram receives command

↓

LangGraph executes workflow

↓

MCP searches arXiv

↓

LLM summarizes papers

↓

Telegram sends digest

---

# Future Features

After the MVP is complete, we plan to add:

## Phase 2

Download PDFs

Extract text

Summarize full papers

Compare papers

## Phase 3

Qdrant

Personal paper memory

Bookmarks

Reading history

## Phase 4

Daily digests

Subscriptions

Notifications

## Phase 5

Research database

Author tracking

Trend detection

Paper recommendation

## Phase 6

Multi-agent architecture

Planner Agent

Research Agent

Reviewer Agent

Writer Agent

---

# Coding Style

Use:

- async everywhere
- type hints
- Pydantic models
- clean architecture
- dependency injection where appropriate
- small functions
- modular code
- docstrings
- no global mutable state
- production-quality code

Avoid:

- giant files
- duplicated code
- hardcoded values
- blocking IO
- unnecessary abstractions

---

# Development Philosophy

We prefer:

quality over quantity

clarity over cleverness

modularity over shortcuts

The project should look like a real production AI system rather than a quick prototype.

Every architectural decision should make future extensions easier.

The codebase should be maintainable, testable, and easy to extend with additional MCP servers beyond ArXiv (Semantic Scholar, Hugging Face, GitHub, Papers With Code, etc.).

The long-term vision is to build a modular AI Research Platform where LangGraph orchestrates multiple MCP servers, each exposing a different research capability.
