import sys
import os
from dotenv import load_dotenv
load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from crews.growth_crew import GrowthCrew
from crews.strategy_crew import StrategyCrew
from storage.json_storage import JSONStorage
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI(title="AI-BOS API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve generated media
media_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "storage", "media")
if not os.path.exists(media_path):
    os.makedirs(media_path)
app.mount("/media", StaticFiles(directory=media_path), name="media")

class WorkflowRequest(BaseModel):
    industry: str
    objective: str

@app.get("/")
def read_root():
    return {"status": "AI-BOS is operational"}

@app.post("/run-growth-workflow")
async def run_growth_workflow(request: WorkflowRequest):
    max_retries = 3
    retry_delay = 5  # seconds
    
    for attempt in range(max_retries):
        try:
            # Initialize and kickoff growth crew
            crew_obj = GrowthCrew(industry=request.industry)
            crew = crew_obj.create_crew()
            
            result = crew.kickoff()
            
            # CrewAI results can be exported as dict/json if structured
            output_data = {
                "raw": result.raw,
                "tasks_output": [t.json_dict for t in result.tasks_output if t.json_dict]
            }
            
            # Save to storage
            saved_path = JSONStorage.save_result("growth_crew", output_data)
            
            return {
                "status": "success",
                "storage_path": saved_path,
                "result": output_data
            }
        except Exception as e:
            if "rate_limit_exceeded" in str(e).lower() and attempt < max_retries - 1:
                print(f"Rate limit hit. Retrying in {retry_delay}s... (Attempt {attempt + 1}/{max_retries})")
                import time
                time.sleep(retry_delay)
                continue
            raise HTTPException(status_code=500, detail=str(e))

@app.post("/run-strategy-workflow")
async def run_strategy_workflow(request: WorkflowRequest):
    try:
        crew_obj = StrategyCrew(business_goal=request.objective)
        crew = crew_obj.create_crew()
        result = crew.kickoff()
        output_data = {
            "raw": result.raw,
            "tasks_output": [t.json_dict for t in result.tasks_output if t.json_dict]
        }
        saved_path = JSONStorage.save_result("strategy_crew", output_data)
        return {
            "status": "success",
            "storage_path": saved_path,
            "result": output_data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
