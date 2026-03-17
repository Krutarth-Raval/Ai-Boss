import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crews.growth_crew import GrowthCrew
from storage.json_storage import JSONStorage

def run_lead_generation_workflow(industry: str):
    """
    Workflow: Research -> Marketing Plan -> Lead List
    """
    print(f"Starting Lead Generation Workflow for: {industry}")
    
    crew_obj = GrowthCrew(industry=industry)
    crew = crew_obj.create_crew()
    
    result = crew.kickoff()
    
    # Process structured output
    output_data = {
        "workflow": "Lead Generation",
        "timestamp": str(datetime.now()) if 'datetime' in globals() else "now",
        "industry": industry,
        "raw_result": result.raw,
        "structured_data": [t.json_dict for t in result.tasks_output if t.json_dict]
    }
    
    storage_path = JSONStorage.save_result("lead_gen", output_data)
    print(f"Workflow Complete. Results saved to: {storage_path}")
    return output_data

if __name__ == "__main__":
    from datetime import datetime
    run_lead_generation_workflow("AI SaaS for HR")
