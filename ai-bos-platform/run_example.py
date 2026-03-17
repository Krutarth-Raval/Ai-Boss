import sys
import os

# Add backend to path
sys.path.append(os.path.join(os.getcwd(), 'backend'))

from workflows.lead_generation_workflow import run_lead_generation_workflow

def main():
    print("--- AI-BOS Platform: Business Workflow Runner ---")
    industry = input("Enter the industry to research: ") or "Renewable Energy"
    
    try:
        results = run_lead_generation_workflow(industry)
        print("\nSUCCESS: Workflow completed.")
        print(f"Results saved to: {results.get('storage_path', 'storage/data/')}")
    except Exception as e:
        print(f"ERROR: {str(e)}")

if __name__ == "__main__":
    main()
