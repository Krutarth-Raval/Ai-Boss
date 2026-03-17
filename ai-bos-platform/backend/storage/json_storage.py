import json
import os
from datetime import datetime
STORAGE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "storage", "data")
if not os.path.exists(STORAGE_DIR):
    os.makedirs(STORAGE_DIR)

class JSONStorage:
    @staticmethod
    def save_result(crew_name: str, result: dict):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{crew_name}_{timestamp}.json"
        filepath = os.path.join(STORAGE_DIR, filename)
        
        with open(filepath, 'w') as f:
            json.dump(result, f, indent=4)
        
        return filepath

    @staticmethod
    def list_results():
        return os.listdir(STORAGE_DIR)
