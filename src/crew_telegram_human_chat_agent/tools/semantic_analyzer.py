# src/crew_telegram_human_chat_agent/tools/semantic_analyzer.py

from crewai.tools import tool
from pydantic import Field
from openai import OpenAI
import os

@tool("SemanticAnalyzerTool")
def semantic_analyzer_tool(
    message: str = Field(..., description="Incoming message from Telegram"),
    target_topics: list[str] = Field(..., description="List of topics to match against")
) -> str:
    """
    Analyzes the semantic meaning of the input message and determines
    if it relates to any of the target topics.
    """

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"""
    You are a semantic analyzer.
    Check whether the following message is semantically related to ANY of these topics:

    Message:
    \"\"\"{message}\"\"\"

    Topics:
    {", ".join(target_topics)}

    If yes, return: Matched topic: <topic>
    If not, return: No match
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Semantic analysis failed: {str(e)}"
