# test_telegram_connector.py
from src.crew_telegram_human_chat_agent.tools.telegram_connector import telegram_connector_tool, TelegramConnectionInput

input_data = TelegramConnectionInput(
    telegram_app_id=26623137,  # 🔁 جایگزین کن با API ID خودت
    telegram_app_hash="019a3afa49ed0e9784cec8a0f61edb8a",  # 🔁 جایگزین کن با API Hash خودت
    phone_number="+573503080001",  # 🔁 شماره خودت
    group_id_or_invite="@nftgrp1403"  # 🔁 لینک یا آی‌دی گروه
)

# استفاده صحیح از Tool
result = telegram_connector_tool.run(input_data)
print(result)
