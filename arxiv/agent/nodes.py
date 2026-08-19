from pydantic import BaseModel, Field


class SearchPlan(BaseModel):
    search_query: str = Field(description="English query suitable for arXiv search")
    category: str = Field(
        default=None,
        description="arXiv category such as cs.AI, cs.CL or cs.LG",
    )


def create_generate_query_node(llm):
    structured_llm = llm.with_structured_output(SearchPlan)

    async def generate_query(state: dict) -> dict:
        plan = await structured_llm.ainvoke(
            [
                {
                    "role": "system",
                    "content": (
                        "Convert the user's research request into a concise "
                        "English arXiv search query. Select an arXiv category "
                        "only when confident."
                    ),
                },
                {
                    "role": "user",
                    "content": state["user_query"],
                },
            ]
        )

        return {
            "search_query": plan.search_query,
            "category": plan.category,
        }

    return generate_query



def create_search_node(tools):
    tools_by_name = {tool.name: tool for tool in tools}
    search_tool = tools_by_name["search_arxiv"]

    async def search_arxiv_node(state: dict) -> dict:
        result = await search_tool.ainvoke(
            {
                "query": state["search_query"],
                "category": state.get("category"),
                "max_results": state.get("max_results", 5),
            }
        )

        return {"papers": result}

    return search_arxiv_node


