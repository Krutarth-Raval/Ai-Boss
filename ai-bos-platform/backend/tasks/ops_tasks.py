from crewai import Task
from schemas.business_schemas import OperationsPlanSchema, HiringCandidateSchema

def get_operations_task(agent, workload_desc: str):
    return Task(
        description=f"Analyze the current company workload: '{workload_desc}'. Design an optimized operational workflow and resource allocation plan.",
        agent=agent,
        expected_output="A structured operations plan in JSON format.",
        output_json=OperationsPlanSchema
    )

def get_hiring_task(agent, job_description: str):
    return Task(
        description=f"Source and evaluate potential candidates for the following role: '{job_description}'. Provide a prioritized list of candidates with fit scores.",
        agent=agent,
        expected_output="A list of candidate profiles in JSON format.",
        output_json=HiringCandidateSchema
    )
