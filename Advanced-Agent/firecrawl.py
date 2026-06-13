import os

from dotenv import load_dotenv
from firecrawl import FirecrawlApp, ScrapeOptions

load_dotenv()


class FirecrawlService:
    def __init__(self):
        api_key = os.getenv("FIRECRAWL_API_KEY")
        if not api_key:
            raise ValueError("FIRECRAWL_API_KEY is not configured")

        self.app = FirecrawlApp(api_key=api_key)

    def search_companies(self, query: str, num_results: int = 5):
        try:
            return self.app.search(
                query=f"{query} company pricing",
                limit=num_results,
                scrape_options=ScrapeOptions(
                    formats=["markdown"]
                ),
            )
        except Exception as exc:
            print(f"Firecrawl search failed: {exc}")
            return type("Result", (), {"data": []})()

    def scrape_company_pages(self, url: str):
        try:
            return self.app.scrape_url(
                url,
                formats=["markdown"],
            )
        except Exception as exc:
            print(f"Firecrawl scrape failed: {exc}")
            return None
