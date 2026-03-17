from crewai import Agent
# from langchain_community.tools import DuckDuckGoSearchRun

# search_tool = DuckDuckGoSearchRun()

def get_research_agent():
    return Agent(
        role="Research Specialist",
        goal="Collect and analyze market trends, competitors, and industry data to identify business opportunities.",
        backstory="You are a data-driven market analyst with a sharp eye for emerging trends. You provide the foundational data that drives company strategy.",
        # tools=[search_tool],
        verbose=True,
        allow_delegation=False
    )
