from langchain_mcp_adapters.client import MultiServerMCPClient


def create_mcp_client() -> MultiServerMCPClient:
    return MultiServerMCPClient(
        {
            "arxiv": {
                "command": "python",
                "args": ["-m", "mcp_server.server"],
                "transport": "stdio",
            }
        }
    )
