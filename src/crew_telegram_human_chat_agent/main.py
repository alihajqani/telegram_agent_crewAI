# src/crew_telegram_human_chat_agent/main.py

import os
from dotenv import load_dotenv
from crew_telegram_human_chat_agent.crew import CrewTelegramHumanChatAgentCrew

def parse_env_list(key: str, separator=","):
    val = os.getenv(key, "")
    return [item.strip() for item in val.split(separator) if item.strip()]

def main():
    load_dotenv()

    inputs = {
        'telegram_app_id': int(os.getenv("TELEGRAM_APP_ID")),
        'telegram_app_hash': os.getenv("TELEGRAM_APP_HASH"),
        'phone_number': os.getenv("PHONE_NUMBER"),
        'group_id': os.getenv("GROUP_ID"),
        'target_topic_list': parse_env_list("TARGET_TOPICS"),
        'response_templates': parse_env_list("RESPONSE_TEMPLATES"),
    }

    print("🚀 Running Telegram Crew...")
    result = CrewTelegramHumanChatAgentCrew().crew().kickoff(inputs=inputs)
    print("✅ Final Output:\n", result)


if __name__ == "__main__":
    main()
