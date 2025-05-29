from textwrap import dedent
from crewai import Agent
from tools import ExaTools

class TelegramAgent():
    def art_topics_researcher_agent(self):
        return Agent(
            role="Art Topic and News Researcher",
            goal=dedent(
                """
                Identify popular and new art topics and news from specified websites.
                """
            ),
            tools=ExaTools.tools(),
            backstory=dedent(
                """
                As an Art Topic Researcher, you excel at finding trending and new art topics and news 
                from a curated list of art websites, ensuring content is always fresh and engaging.
                """),
            verbose=True
        )
    
    def art_post_creation_agent(self):
        return Agent(
            role="Art Post Creation Specialist",
            goal=dedent(
                """
                Generate engaging posts in Persian about identified art topics and news, 
                including reference links and related hashtags.
                """
                ),
            tools=ExaTools.tools(),
            backstory=dedent(
                """
                With a passion for art and language, you create compelling posts in 
                Persian that resonate with the audience, incorporating reference 
                links for credibility and related hashtags for visibility.
                """),

        )
    
    def content_scheduler_agent(self):
        return Agent(
            role="Content Scheduling Manager",
            goal=dedent(
                """
                Schedule and manage the posting of content to the Telegram channel.
                """),
            tools=ExaTools.tools(),
            backstory=dedent(
                """
                As a Content Scheduling Manager, you ensure that all posts are timely 
                and strategically published to maximize audience engagement.
                """),
        )