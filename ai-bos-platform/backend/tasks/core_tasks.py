from crewai import Task
from schemas.business_schemas import MarketResearchSchema, LeadListSchema

def get_market_research_task(agent, industry: str):
    return Task(
        description=f"Perform a deep-dive market research for the {industry} industry. Identify market size, growth rates, top 5 competitors, and major risks/opportunities.",
        agent=agent,
        expected_output="A comprehensive market research report in JSON format.",
        output_json=MarketResearchSchema
    )

def get_lead_generation_task(agent, target_audience: str):
    return Task(
        description=f"Find and analyze 3 potential high-value leads within the {target_audience} segment. Score them based on fit and budget.",
        agent=agent,
        expected_output="A list of validated leads in JSON format.",
        output_json=LeadListSchema
    )
