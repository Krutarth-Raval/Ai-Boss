from crewai import Task
from schemas.business_schemas import MarketingPlanSchema, FinanceReportSchema

def get_marketing_plan_task(agent, goal: str):
    return Task(
        description=f"Create a detailed marketing plan for the objective: '{goal}'. Include target audience, channels, and expected ROI.",
        agent=agent,
        expected_output="A structured marketing plan in JSON format.",
        output_json=MarketingPlanSchema
    )

def get_finance_report_task(agent, business_plan: str):
    return Task(
        description=f"Analyze the following business plan and provide a financial feasibility report: '{business_plan}'.",
        agent=agent,
        expected_output="A financial report including projected costs and risks in JSON format.",
        output_json=FinanceReportSchema
    )
