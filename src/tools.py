import os
from exa_py import Exa
from crewai.tools import tool

class ExaTools:
    @tool("Search and Get Contents")
    def search_and_get_contents(
        query: str,
        type: str = "auto",
        max_characters: int = 1000,
        num_results: int = 5,
        start_published_date: str | None = None,
        start_crawl_date: str | None = None
    ) -> list[dict]:
        """
        Perform a combined search and content fetch.

        Args:
            query: The search query string.
            type: The search type (e.g., "auto", "neural").
            max_characters: Max characters of content to retrieve per result.
            num_results: Number of search results to return.
            start_published_date: ISO timestamp to filter by published date.
            start_crawl_date: ISO timestamp to filter by crawl date.

        Returns:
            A list of result dicts with keys: id, url, title, text, publishedDate, author, favicon, image.
        """
        exa = Exa(api_key=os.environ.get("EXA_API_KEY"))
        text_opts = {"max_characters": max_characters}
        # Call the combined search and contents API
        response = exa.search_and_contents(
            query,
            type=type,
            text=text_opts,
            num_results=num_results,
            start_published_date=start_published_date,
            start_crawl_date=start_crawl_date
        )
        # Convert each Result Pydantic model to dict using model_dump()
        results = []
        for result in getattr(response, "results", []):
            try:
                results.append(result.model_dump())
            except AttributeError:
                # Fallback: manually build dict
                results.append({
                    "id": getattr(result, "id", None),
                    "url": getattr(result, "url", None),
                    "title": getattr(result, "title", None),
                    "text": getattr(result, "text", None),
                    "publishedDate": getattr(result, "publishedDate", None),
                    "author": getattr(result, "author", None),
                    "favicon": getattr(result, "favicon", None),
                    "image": getattr(result, "image", None)
                })
        return results

    @classmethod
    def tools(cls) -> list:
        """
        Return all CrewAI tools.
        """
        return [cls.search_and_get_contents]
