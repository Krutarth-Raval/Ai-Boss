from crewai import Crew, Process
from agents.creative_agents import get_creative_marketing_agent
from tasks.creative_tasks import get_poster_generation_task, get_video_generation_task, get_creative_summary_task

class CreativeCrew:
    def __init__(self, objective: str):
        self.objective = objective
        self.creator = get_creative_marketing_agent()

    def create_crew(self):
        task1 = get_poster_generation_task(self.creator, self.objective)
        task2 = get_video_generation_task(self.creator, self.objective)
        task3 = get_creative_summary_task(self.creator, [task1, task2])

        return Crew(
            agents=[self.creator],
            tasks=[task1, task2, task3],
            process=Process.sequential,
            verbose=True
        )
