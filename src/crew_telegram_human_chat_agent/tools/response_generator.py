# src/crew_telegram_human_chat_agent/tools/response_generator.py

from crewai.tools import tool
from openai import OpenAI
import os

@tool("ResponseGeneratorTool")
def response_generator_tool(
    message: str,
    matched_topic: str,
    response_templates: list[str] = None
) -> str:
    """
    Uses LLM to generate a natural, helpful and context-aware response to a message,
    based on the detected semantic topic.
    """

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"""
    شما یک عضو مفید در یک گروه تلگرام هستی که به زبان فارسی محاوره‌ای با بقیه گفتگو می‌کنی.
    پیام زیر دریافت شده:
    "{message}"
    موضوعی که این پیام به آن مرتبط است: {matched_topic}
    با استفاده از لحن دوستانه و طبیعی فارسی، یک پاسخ کوتاه و قابل فهم بده. از این جملات الگو بگیر:
    {('\n'.join(response_templates)) if response_templates else ''}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Response generation failed: {str(e)}"
