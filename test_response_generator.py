# test_response_generator.py

from src.crew_telegram_human_chat_agent.tools.response_generator import response_generator_tool, ResponseGeneratorInput

input_data = ResponseGeneratorInput(
    message="This airdrop looks suspicious, is it legit?",
    matched_topic="airdrop",
    response_templates=["Thank you for asking!", "Always verify the source before interacting."]
)

result = response_generator_tool.run(input_data)
print(result)
