# src/crew_telegram_human_chat_agent/tools/interaction_logger.py

import os
import json
from datetime import datetime
from crewai.tools import tool

@tool("InteractionLoggerTool")
def interaction_logger_tool(
    message: str,
    matched_topic: str,
    generated_response: str
) -> str:
    """
    Logs the interaction details to a local JSONL file for auditing and improvement.
    """

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "message": message,
        "matched_topic": matched_topic,
        "generated_response": generated_response
    }

    log_path = "interaction_logs.jsonl"
    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")
        return f"✅ Interaction logged at {log_path}"
    except Exception as e:
        return f"❌ Logging failed: {str(e)}"
