from crewai import Crew, Process, Task
from agents.research_agent import get_research_agent
from agents.strategy_agents import get_strategy_agent, get_analytics_agent
from tasks.core_tasks import get_market_research_task
from schemas.business_schemas import BusinessStrategySchema, PerformanceInsightsSchema

class StrategyCrew:
    def __init__(self, business_goal: str):
        self.business_goal = business_goal
        self.researcher = get_research_agent()
        self.strategist = get_strategy_agent()
        self.analyst = get_analytics_agent()

    def create_crew(self):
        # 1. Research the market
        research_task = get_market_research_task(self.researcher, self.business_goal)
        
        # 2. Strategy formation
        strategy_task = Task(
            description=f"Based on the market research, develop a high-level business strategy for: '{self.business_goal}'.",
            agent=self.strategist,
            expected_output="A comprehensive business strategy in JSON format.",
            output_json=BusinessStrategySchema,
            context=[research_task]
        )
        
        # 3. Analytics & Prediction
        analytics_task = Task(
            description=f"Analyze the proposed strategy for '{self.business_goal}' and provide performance projections and success metrics.",
            agent=self.analyst,
            expected_output="Performance insights and projections in JSON format.",
            output_json=PerformanceInsightsSchema,
            context=[strategy_task]
        )

        return Crew(
            agents=[self.researcher, self.strategist, self.analyst],
            tasks=[research_task, strategy_task, analytics_task],
            process=Process.sequential,
            verbose=True
        )
