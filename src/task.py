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
    
    def generate_persian_post_task(self, agent):
        return Task(
            description=dedent("""
                Create engaging Persian social media posts from the art topics below.
                For each topic include:
                - A summary (translated in Persian)
                - The original image (if exists)
                - A clickable link to the source using markdown
                Your output should be formatted as:
                ---
                **{translated_title}**
                {translated_summary}

                🔗 اطلاعات بیشتر: [{source_title}]({source_url})
                ![Image]({image_url})

                #هشتگ #مرتبط #با #موضوع
                ---
                If no image is available, skip the image markdown.
                """),
            expected_output=dedent("""
                A list of formatted Persian posts with titles, summaries, images (if exist), 
                and clickable markdown links back to the original sources.
            """),
            agent=agent
        )

    
    def send_post_to_telegram_task(self, agent):
        return Task(
            description=dedent(
                """
                Send the created Persian posts to the Telegram channel,                
                ensuring they are formatted correctly and include all necessary links and hashtags.
                if the post had image, send the image with the post.
                """
            ),
            expected_output=dedent(
                """
                All Persian posts successfully sent to the Telegram channel,
                with confirmation of successful delivery."""
            ),
            agent=agent,
            inputs={
                "post_content": "{post_content}"            }
        )