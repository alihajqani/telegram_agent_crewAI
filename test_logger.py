# test_logger.py

from src.crew_telegram_human_chat_agent.tools.logger import interaction_logger_tool, InteractionLogInput

input_data = InteractionLogInput(
    message="This airdrop seems fishy!",
    matched_topic="airdrop",
    generated_response="Thanks for raising this — please double-check the project before interacting."
)

result = interaction_logger_tool.run(input_data)
print(result)
