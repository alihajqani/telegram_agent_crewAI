import os
import asyncio
from exa_py import Exa
from telegram import Bot
from typing import Optional
from crewai.tools import tool
from pydantic import BaseModel, Field
from telegram.ext import ApplicationBuilder

class ExaTools:
    @tool("Search and Get Contents")
    def search_and_get_contents(
        query: str,
        type: str = "auto",
        max_characters: int = 1000,
        num_results: int = 2,
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

class TelegramTools:    
    @tool("Send Telegram Post")
    def send_telegram_post(post_content: str, image_url: Optional[str] = None) -> str:
        """
        Send a post to a Telegram channel using the python-telegram-bot library.
        Channel ID and token are read from environment variables.

        Args:
            post_content: The content of the post to send.
            image_url: Optional URL of an image to include in the post.
        Returns:
            A success message or an error message if sending fails.
        """
        async def _inner():
            bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
            channel_id = os.environ.get("TELEGRAM_CHANNEL_ID")

            if not bot_token or not channel_id:
                raise ValueError("Environment variables TELEGRAM_BOT_TOKEN or TELEGRAM_CHANNEL_ID are missing.")

            application = ApplicationBuilder().token(bot_token).build()
            await application.initialize()

            try:
                if image_url:
                    await application.bot.send_photo(chat_id=channel_id, photo=image_url, caption=post_content, parse_mode="HTML")
                else:
                    await application.bot.send_message(chat_id=channel_id, text=post_content, parse_mode="HTML")
            except Exception as e:
                raise RuntimeError(f"Failed to send post: {e}")

        try:
            asyncio.run(_inner())
            return "✅ Telegram message sent successfully."
        except Exception as e:
            return f"❌ Error sending message: {e}"



    @classmethod
    def tools(cls) -> list:
        """
        Return all Telegram tools.
        """
        return [cls.send_telegram_post]