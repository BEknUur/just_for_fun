#
from __future__ import annotations
from datetime import datetime

from urllib.parse import urlencode

import feedparser
import httpx


ARXIV_API_URL = "https://export.arxiv.org/api/query"


class ArxivClient:
    def __init__(self) -> None:
        self.http_client = httpx.AsyncClient(
            timeout=30,
            headers={"User-Agent": "arxiv-research-bot/0.1 contact@example.com"},
        )

    async def search(
        self,
        query: str,
        max_results: int = 5,
        start: int = 0,
        sort_by: str = "submittedDate",
        sort_order: str = "descending",
    ) -> list[dict]:
        params = {
            "search_query": query,
            "start": start,
            "max_results": max(max_results, 20),
            "sort_by": sort_by,
            "sort_order": sort_order,
        }

        url = f"{ARXIV_API_URL}?{urlencode(params)}"

        response = await self.http_client.get(url)

        response.raise_for_status()

        feed = feedparser.loads(response.text)

        papers = []

        for entry in feed.entries:
            arxiv_id = entry.id.split("/abs/")[-1]

            pdf_url = None

            for link in entry.get("links", []):
                if link.get("type") == "application/pdf":
                    pdf_url = link.get("href")

            papers.append(
                {
                    "arxiv_id": arxiv_id,
                    "title": " ".join(entry.title.split()),
                    "abstract": " ".join(entry.summary.split()),
                    "authors": [author.name for author in entry.get("authors", [])],
                    "published": entry.published,
                    "updated": entry.updated,
                    "url": entry.id,
                    "pdf_url": pdf_url,
                    "categories": [tag["term"] for tag in entry.get("tags", [])],
                }
            )

        return papers

    async def close(self) -> None:
        await self.http_client.aclose()
