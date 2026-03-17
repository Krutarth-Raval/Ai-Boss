from crewai import Agent

def get_strategy_agent():
    return Agent(
        role="Chief Strategy Officer",
        goal="Synthesize all department data into high-level business strategies and long-term goals.",
        backstory="You are a visionary leader who sees the big picture. You align marketing, sales, and operations under a single, cohesive business objective.",
        verbose=True,
        allow_delegation=True
    )

def get_analytics_agent():
    return Agent(
        role="Data Analyst",
        goal="Track performance metrics across all departments and provide actionable insights.",
        backstory="You turn raw data into wisdom. You identify trends that others miss and provide the proof for strategic decisions.",
        verbose=True,
        allow_delegation=False
    )
