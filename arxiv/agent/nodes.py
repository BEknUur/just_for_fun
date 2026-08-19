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
