from crewai import Crew, Process
from agents.research_agent import get_research_agent
from agents.growth_agents import get_marketing_agent, get_sales_agent
from agents.creative_agents import get_creative_marketing_agent
from tasks.core_tasks import get_market_research_task, get_lead_generation_task
from tasks.strategic_tasks import get_marketing_plan_task
from tasks.creative_tasks import get_poster_generation_task, get_video_generation_task, get_creative_summary_task

class GrowthCrew:
    def __init__(self, industry: str):
        self.industry = industry
        self.researcher = get_research_agent()
        self.marketer = get_marketing_agent()
        self.sales = get_sales_agent()
        self.creator = get_creative_marketing_agent()

    def create_crew(self):
        # 1. Market Research
        task1 = get_market_research_task(self.researcher, self.industry)
        
        # 2. Marketing Plan
        task2 = get_marketing_plan_task(self.marketer, f"Dominate the {self.industry} market")
        
        # 3. Lead Generation
        task3 = get_lead_generation_task(self.sales, self.industry)
        
        # 4. Creative Assets (Poster & Video)
        creative_objective = f"Facebook ad and marketing materials for {self.industry}. Goals: High conversion, professional visuals."
        task4 = get_poster_generation_task(self.creator, creative_objective)
        task5 = get_video_generation_task(self.creator, creative_objective)
        task6 = get_creative_summary_task(self.creator, [task4, task5])

        return Crew(
            agents=[self.researcher, self.marketer, self.sales, self.creator],
            tasks=[task1, task2, task3, task4, task5, task6],
            process=Process.sequential,
            verbose=True
        )
