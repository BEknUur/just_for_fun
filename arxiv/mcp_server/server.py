from mcp.server.fastmcp import FastMCP

from mcp_server.arxiv_client import ArxivClient
from mcp_server.tools import register_tools


mcp = FastMCP("arxiv-research")

arxiv_client = ArxivClient()
register_tools(mcp,arxiv_client)



if __name__ == "__main__":
    mcp.run(transport="stdio")
