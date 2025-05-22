from src.crew_telegram_human_chat_agent.tools.semantic_analyzer import semantic_analyzer_tool, SemanticAnalyzerInput

input_data = SemanticAnalyzerInput(
    message="This airdrop might be a scam, be careful.",
    target_topics=["airdrop", "scam", "metamask"]
)

result = semantic_analyzer_tool.run(input_data)
print(result)
