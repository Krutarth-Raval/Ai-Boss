import os
import requests
import time
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class ImageGenerationInput(BaseModel):
    """Input for ImageGenerationTool."""
    prompt: str = Field(..., description="The highly detailed prompt for the marketing poster.")

class ImageGenerationTool(BaseTool):
    name: str = "image_generation_tool"
    description: str = "Generates a high-quality marketing poster using Tongyi-MAI/Z-Image-Turbo on HuggingFace."
    args_schema: Type[BaseModel] = ImageGenerationInput

    def _run(self, prompt: str) -> str:
        api_url = "https://api-inference.huggingface.co/models/Tongyi-MAI/Z-Image-Turbo"
        api_key = os.getenv("HF_TOKEN")
        headers = {"Authorization": f"Bearer {api_key}"}
        
        # Adding provider as per user reference
        payload = {
            "inputs": prompt,
            "provider": "wavespeed"
        }

        try:
            response = requests.post(api_url, headers=headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                storage_dir = os.path.join(os.getcwd(), "storage", "media")
                if not os.path.exists(storage_dir):
                    os.makedirs(storage_dir)
                
                timestamp = int(time.time())
                filename = f"poster_{timestamp}.png"
                filepath = os.path.join(storage_dir, filename)
                with open(filepath, "wb") as f:
                    f.write(response.content)
                
                return f"http://localhost:8002/media/{filename}"
            else:
                return f"Error: Image generation failed (Status {response.status_code}). {response.text}"
        except Exception as e:
            return f"Error in image generation tool: {str(e)}"

class VideoGenerationInput(BaseModel):
    """Input for VideoGenerationTool."""
    prompt: str = Field(..., description="The prompt for the 10-second cinematic marketing video.")

class VideoGenerationTool(BaseTool):
    name: str = "video_generation_tool"
    description: str = "Generates a marketing video using RunwayML (gen4.5) with fallback to Wan-AI on HuggingFace."
    args_schema: Type[BaseModel] = VideoGenerationInput

    def _run(self, prompt: str) -> str:
        runway_key = os.getenv("RUNWAY_API_KEY")
        runway_version = os.getenv("RUNWAY_VERSION", "2024-11-06")

        if runway_key and runway_key != "your_key":
            try:
                # RunwayML Gen-4.5 (as per user reference)
                api_url = "https://api.dev.runwayml.com/v1/text_to_video"
                headers = {
                    "Authorization": f"Bearer {runway_key}",
                    "X-Runway-Version": runway_version,
                    "Content-Type": "application/json"
                }
                payload = {
                    "model": "gen4.5",
                    "promptText": prompt,
                    "ratio": "1280:720",
                    "duration": 5 # 5s as per reference
                }

                response = requests.post(api_url, headers=headers, json=payload, timeout=30)
                if response.status_code in [200, 201]:
                    task_id = response.json().get("id")
                    return f"https://dashboard.runwayml.com/tasks/{task_id}"
                print(f"RunwayML failed (Status {response.status_code}), falling back to HF...")
            except Exception as e:
                print(f"RunwayML error: {e}, falling back to HF...")

        # Fallback to HuggingFace (Wan-AI)
        hf_token = os.getenv("HF_TOKEN")
        if hf_token:
            api_url = "https://api-inference.huggingface.co/models/Wan-AI/Wan2.1-T2V-14B"
            headers = {"Authorization": f"Bearer {hf_token}"}
            payload = {
                "inputs": prompt,
                "provider": "fal-ai"
            }
            try:
                response = requests.post(api_url, headers=headers, json=payload, timeout=60)
                if response.status_code == 200:
                    # For video we might just return the binary if it's small, 
                    # but usually we save it or return a URL.
                    # As per reference, we return the base64 or URL.
                    # We'll save it locally like the poster.
                    storage_dir = os.path.join(os.getcwd(), "storage", "media")
                    if not os.path.exists(storage_dir):
                        os.makedirs(storage_dir)
                    
                    timestamp = int(time.time())
                    filename = f"video_{timestamp}.mp4"
                    filepath = os.path.join(storage_dir, filename)
                    with open(filepath, "wb") as f:
                        f.write(response.content)
                    
                    return f"http://localhost:8002/media/{filename}"
                return f"Error: HF Video generation failed (Status {response.status_code})."
            except Exception as e:
                return f"Error in HF fallback: {str(e)}"

        return "Error: No API keys available for video generation."
