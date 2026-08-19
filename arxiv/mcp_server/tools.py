from mcp.server.fastmcp import FastMCP

from mcp_server.arxiv_client import ArxivClient


def register_tools(mcp: FastMCP, arxiv_client: ArxivClient) -> None:

    @mcp.tool()
    async def search_arxiv(
        query: str,
        max_results: int = 5,
        category: str | None = None,
    ) -> list[dict]:
        search_query = f'all:"{query}"'

        if category:
            search_query += f" AND cat:{category}"

        return await arxiv_client.search(
            query=search_query,
            max_results=max_results,
        )

    @mcp.tool()
    async def search_by_author(
        author: str,
        max_results: int = 10,
    ) -> list[dict]:
        return await arxiv_client.search(
            query=f'au:"{author}"',
            max_results=max_results,
        )