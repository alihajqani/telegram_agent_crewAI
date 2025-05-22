# src/crew_telegram_human_chat_agent/crew.py

from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task

# ابزارها
from crew_telegram_human_chat_agent.tools import (
    telegram_connector_tool,
    telegram_message_fetcher_tool,
    semantic_analyzer_tool,
    response_generator_tool,
    interaction_logger_tool,
)

@CrewBase
class CrewTelegramHumanChatAgentCrew():
    """Crew for monitoring, analyzing and responding to Telegram group messages"""

    # 🧠 Agents
    @agent
    def UserConnectionOperator(self) -> Agent:
        return Agent(
            config=self.agents_config['UserConnectionOperator'],
            tools=[telegram_connector_tool],
        )

    @agent
    def GrokSemanticMonitor(self) -> Agent:
        return Agent(
            config=self.agents_config['GrokSemanticMonitor'],
            tools=[telegram_message_fetcher_tool, semantic_analyzer_tool],
        )

    @agent
    def GrokEngager(self) -> Agent:
        print("🔍 type of GrokEngager config:", type(self.agents_config['GrokEngager']))
        print("🔍 value of GrokEngager config:", self.agents_config['GrokEngager'])
        return Agent(
            config=self.agents_config['GrokEngager'],
            tools=[response_generator_tool],
        )

    @agent
    def LoggingCoordinator(self) -> Agent:
        return Agent(
            config=self.agents_config['LoggingCoordinator'],
            tools=[interaction_logger_tool],
        )

    # 📌 Tasks
    @task
    def user_connection_task(self) -> Task:
        return Task(
            config=self.tasks_config['user_connection_task'],
            tools=[telegram_connector_tool],
        )

    @task
    def semantic_monitoring_task(self) -> Task:
        return Task(
            config=self.tasks_config['semantic_monitoring_task'],
            tools=[telegram_message_fetcher_tool, semantic_analyzer_tool],
        )

    @task
    def engagement_task(self) -> Task:
        print("🔍 type of engagement_task config:", type(self.tasks_config['engagement_task']))
        print("🔍 value of engagement_task config:", self.tasks_config['engagement_task'])
        return Task(
            config=self.tasks_config['engagement_task'],
            tools=[response_generator_tool],
        )

    @task
    def logging_task(self) -> Task:
        return Task(
            config=self.tasks_config['logging_task'],
            tools=[interaction_logger_tool],
        )

    # 🤝 CREW
    @crew
    def crew(self) -> Crew:
        """Creates the complete Telegram chat analysis crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
