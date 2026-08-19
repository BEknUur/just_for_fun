from langgraph.graph import END, START, StateGraph
from agent.state import ResearchState


def build_graph(
    generate_query_node,
    search_node,
    rank_node,
    summarize_node,
):
    graph = StateGraph(ResearchState)

    graph.add_node("generate_query", generate_query_node)
    graph.add_node("search_arxiv", search_node)
    graph.add_node("rank_papers", rank_node)
    graph.add_node("summarize", summarize_node)

    graph.add_edge(START, "generate_query")
    graph.add_edge("generate_query", "search_arxiv")
    graph.add_edge("search_arxiv", "rank_papers")
    graph.add_edge("rank_papers", "summarize")
    graph.add_edge("summarize", END)

    return graph.compile()
