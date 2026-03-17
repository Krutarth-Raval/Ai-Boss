from crewai import Task
from pydantic import BaseModel
from typing import List

class CreativeOutputSchema(BaseModel):
    poster_status: str
    video_status: str
    poster_prompt: str
    video_prompt: str

def get_poster_generation_task(agent, objective: str):
    return Task(
        description=f"Create a high-fidelity marketing poster for the following objective: {objective}. "
                    "Use the image_generation_tool with a detailed, visually descriptive prompt including lighting, style, and composition.",
        expected_output="The file path of the generated poster and the prompt used.",
        agent=agent
    )

def get_video_generation_task(agent, objective: str):
    return Task(
        description=f"Generate a 10-second cinematic marketing video for the following objective: {objective}. "
                    "Use the video_generation_tool with a prompt that describes movement, atmosphere, and the core message.",
        expected_output="The status of the video generation task and the prompt used.",
        agent=agent
    )

def get_creative_summary_task(agent, context_tasks: List[Task]):
    return Task(
        description="Summarize the creative assets generated, including prompts used and where the files are stored.",
        expected_output="A structured summary of the created marketing assets.",
        agent=agent,
        context=context_tasks,
        output_json=CreativeOutputSchema
    )
