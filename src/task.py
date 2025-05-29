from textwrap import dedent
from crewai import Task


class TelegramTask():
    def search_art_website_task(self, agent, list_of_art_website_task):
        return Task(
            description=dedent(
                f"""
                Use the list of specific art websites to find 
                popular and new topics in art.

                list of art website: {list_of_art_website_task}.
                """
            ),
            expected_output=dedent(
                f"""A list of trending and recent art topics, 
                each with a summary of key points and reference 
                links from the specified websites."""
            ),
            agent=agent,
            async_execution=True
        )
    
    def generate_persian_post_task(self, agent, ):
        return Task(
            description=dedent(
                f"""
                Create engaging posts in Persian about identified art topics
                and news, including reference links and related hashtags.
                """
            ),
            expected_output=dedent(
                f"""Persian posts ready for publication,
                complete with reference links and related hashtags."""
            ),
            agent=agent
        )
    
    def generate_persian_post_task(self, agent, ):
        return Task(
            description=dedent(
                f"""
                Create engaging posts in Persian about identified art topics
                and news, including reference links and related hashtags.
                """
            ),
            expected_output=dedent(
                f"""List of Persian posts ready for publication,
                complete with reference links and related hashtags."""
            ),
            agent=agent
        )
    
    def schedule_telegram_posts_task(self, agent):
        return Task(
            description=dedent(
                f"""
                Schedule and publish the Persian posts to the Telegram channel,
                ensuring proper timing and engagement strategies.
                """
            ),
            expected_output=dedent(
                f"""All Persian posts successfully scheduled on Telegram,
                with confirmation of scheduled times."""
            ),
            agent=agent
        )