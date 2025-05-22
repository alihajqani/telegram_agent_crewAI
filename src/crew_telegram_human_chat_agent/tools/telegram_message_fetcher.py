# src/crew_telegram_human_chat_agent/tools/telegram_message_fetcher.py

from telethon.sync import TelegramClient
from crewai.tools import tool

@tool("TelegramMessageFetcherTool")
def telegram_message_fetcher_tool(
    telegram_app_id: int,
    telegram_app_hash: str,
    group_username: str,
    limit: int = 10
) -> str:
    """
    Fetches the latest messages from the given Telegram group.
    """
    session_name = "telegram_session"

    try:
        client = TelegramClient(session_name, telegram_app_id, telegram_app_hash)
        client.connect()

        if not client.is_user_authorized():
            return "❌ User not authorized. Please run connector tool first."

        messages = client.get_messages(group_username, limit=limit)

        result = "\n---\n".join(
            [f"[{msg.date}] {msg.sender_id}: {msg.text}" for msg in messages if msg.text]
        )
        client.disconnect()
        return result if result else "⚠️ No text messages found."

    except Exception as e:
        return f"❌ Failed to fetch messages: {str(e)}"
