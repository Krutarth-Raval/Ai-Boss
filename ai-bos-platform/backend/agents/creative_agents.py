from crewai import Agent
from tools.media_tools import ImageGenerationTool, VideoGenerationTool

def get_creative_marketing_agent():
    return Agent(
        role="Creative Content Creator",
        goal="Produce visually stunning posters and short-form video content that align with marketing objectives.",
        backstory="You are an award-winning digital artist and videographer. You have a knack for visual storytelling and know exactly how to use AI tools like Hugging Face and RunwayML to create viral marketing assets.",
        tools=[ImageGenerationTool(), VideoGenerationTool()],
        verbose=True,
        allow_delegation=False
    )
