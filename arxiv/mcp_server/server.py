from mcp.server.fastmcp import FastMCP

from mcp_server.arxiv_client import ArxivClient


mcp = FastMCP("arxiv-research")

arxiv_client = ArxivClient()


@mcp.tool()
async def search_arxiv(
    query: str,
    max_results: int = 5,
    category: str | None = None,
) -> list[dict]:
    """
    Search arXiv papers.

    Args:
        query: Search query, for example 'agentic RAG'.
        max_results: Maximum number of papers.
        category: Optional arXiv category, for example 'cs.AI'.
    """
    search_query = f'all:"{query}"'

    if category:
        search_query += f" AND cat:{category}"

    return await arxiv_client.search(
        query=query,
        max_results=max_results,
    )


@mcp.tool()
async def search_author(
    author: str,
    max_results: int = 10,
) -> list[dict]:
    """Search arxiv author"""

    return await arxiv_client.search(
        query=f'au:"{author}"',
        max_results=max_results,
    )


@mcp.tool()
async def get_paper(arxiv_id: str) -> dict | None:
    """Get the paper by the arxiv id"""

    results = await arxiv_client.search(
        query=f"id:{arxiv_id}",
        max_results=1,
    )

    if not results:
        return None

    return results[0]


if __name__ == "__main__":
    mcp.run(transport="stdio")
