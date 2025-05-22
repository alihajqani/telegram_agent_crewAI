# src/crew_telegram_human_chat_agent/tools/telegram_connector.py

from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from crewai.tools import tool
from pydantic import BaseModel, Field


class TelegramConnectionInput(BaseModel):
    telegram_app_id: int = Field(..., description="Telegram API ID")
    telegram_app_hash: str = Field(..., description="Telegram API Hash")
    phone_number: str = Field(..., description="Phone number with country code, e.g., +989123456789")
    group_id_or_invite: str = Field(..., description="Group username (e.g., @mygroup) or invite link (e.g. https://t.me/joinchat/XXXX)")


@tool("TelegramConnectorTool")
def telegram_connector_tool(
  telegram_app_id: int,
  telegram_app_hash: str,
  phone_number: str,
  group_id_or_invite: str
) -> str:
    """
    Connects to Telegram using user credentials and joins a specified group.
    Returns success message after joining.
    """
    session_name = "telegram_session"

    try:
        client = TelegramClient(session_name, telegram_app_id, telegram_app_hash)
        client.connect()

        if not client.is_user_authorized():
            client.send_code_request(phone_number)
            code = input("Enter the code you received via Telegram: ")
            try:
                client.sign_in(phone_number, code)
            except SessionPasswordNeededError:
                pw = input("2FA password required. Enter your Telegram password: ")
                client.sign_in(password=pw)

        # Join group by invite or username
        if "joinchat" in group_id_or_invite:
            invite_hash = group_id_or_invite.split("/")[-1]
            client(ImportChatInviteRequest(invite_hash))
        else:
            username = group_id_or_invite.replace("https://t.me/", "").lstrip("@")
            client(JoinChannelRequest(username))
            
        client.disconnect()

        return f"✅ Successfully connected and joined group: {group_id_or_invite}"

    except Exception as e:
        return f"❌ Failed to connect or join group: {str(e)}"
