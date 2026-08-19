from typing import TypedDict


class ResearchState(TypedDict, total=False):
    user_query: str
    search_query: str
    category: str
    max_results: int
    papers: list[dict]
    selected_papers: list[dict]
    summary: str
    error: str | None
