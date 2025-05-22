# test_telegram_fetcher.py

from src.crew_telegram_human_chat_agent.tools.telegram_message_fetcher import telegram_message_fetcher_tool, TelegramMessageFetchInput

input_data = TelegramMessageFetchInput(
    telegram_app_id=123456,
    telegram_app_hash="your_api_hash_here",
    phone_number="+989123456789",
    group_username="@nftgrp1403",
    limit=5
)

result = telegram_message_fetcher_tool.run(input_data)
print(result)
