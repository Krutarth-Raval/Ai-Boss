from crewai import Agent

def get_marketing_agent():
    return Agent(
        role="Marketing Strategist",
        goal="Develop high-impact marketing plans and campaign ideas that resonate with target audiences.",
        backstory="You are a creative mastermind who understands consumer psychology. You turn market research into compelling narratives and growth strategies.",
        verbose=True,
        allow_delegation=False
    )

def get_sales_agent():
    return Agent(
        role="Sales Executive",
        goal="Identify high-quality leads and design conversion-focused outreach strategies.",
        backstory="You are a persuasive communicator who excels at building relationships and closing deals. You know how to tailor a pitch to solve a client's specific pain points.",
        verbose=True,
        allow_delegation=False
    )
