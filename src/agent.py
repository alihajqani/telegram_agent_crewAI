from textwrap import dedent
from crewai import Agent
from tools import ExaTools, TelegramTools

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
    
    def telegram_post_sender_agent(self):
        return Agent(
            role="Telegram Post Sender",
            goal=dedent(
                """
                Send the created Persian posts to the Telegram channel, ensuring they are 
                formatted correctly and include all necessary links and hashtags.
                """),
            tools=TelegramTools.tools(),
            backstory=dedent(
                """
                As a Telegram Post Sender, you ensure that all posts are delivered 
                successfully to the channel, maintaining formatting and including all 
                necessary links and hashtags and if the post had image, send the image with the post.
                """),
        )