from dotenv import load_dotenv
from crewai import Crew

from agent import TelegramAgent
from task import TelegramTask



def main():
    load_dotenv()

    print("Starting Telegram Art Content Creation Process...")
    print("************************************************************")
    print("*** Welcome to the Telegram Art Content Creation Process ***")
    print("************************************************************")
    
    art_websites = [
    "https://www.artnews.com/",
    "https://www.thisiscolossal.com/",
    "https://www.designboom.com/art/",
    "https://www.dezeen.com/art/",
    ]

    agents = TelegramAgent()
    researcher = agents.art_topics_researcher_agent()
    writer = agents.art_post_creation_agent()
    post_sender = agents.telegram_post_sender_agent()

    tasks = TelegramTask()
    research_task = tasks.search_art_website_task(researcher, art_websites)
    post_creation_task = tasks.generate_persian_post_task(writer)
    send_post_task = tasks.send_post_to_telegram_task(post_sender)

    post_creation_task.context = [research_task]
    send_post_task.context = [research_task, post_creation_task]

    crew = Crew(
        name="Telegram Art Content Creation Crew",
        agents=[
            researcher,
            writer,
            post_sender
        ],
        tasks=[
            research_task,
            post_creation_task,
            send_post_task
        ],
        verbose=True
    )

    result = crew.kickoff()
    print("******************************************************")
    print("** Telegram Art Content Creation Process Completed! **")
    print("******************************************************")
    print("Results:")
    print(result)

if __name__ == "__main__":
    main()
