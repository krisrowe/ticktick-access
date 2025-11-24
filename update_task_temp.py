import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

TICKTICK_ACCESS_TOKEN = os.getenv("TICKTICK_ACCESS_TOKEN")
API_BASE_URL = "https://api.ticktick.com/open/v1/task"

def update_ticktick_task(task_data: dict):
    """
    Updates a TickTick task with the provided data.
    task_data should be a dictionary containing all fields of the task,
    including id and projectId.
    """
    if not TICKTICK_ACCESS_TOKEN:
        return {"error": "TICKTICK_ACCESS_TOKEN not found in .env"}
    
    task_id = task_data.get("id")
    if not task_id:
        return {"error": "Task ID is required for updating a task."}

    headers = {
        "Authorization": f"Bearer {TICKTICK_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(f"{API_BASE_URL}/{task_id}", headers=headers, data=json.dumps(task_data))
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to update task: {e}", "response": response.json() if response else None}

if __name__ == "__main__":
    # Example Usage (replace with actual task data)
    # You would typically get this task_data from a list_tasks call first
    # and then modify the fields you want to update.
    
    # This is the task data that was successfully updated via curl
    example_task_data = {
        "id": "GENERIC_TASK_ID",
        "projectId": "GENERIC_PROJECT_ID",
        "sortOrder": 12345,
        "title": "Example: Follow-up on Product Feedback",
        "content": "Example: Discuss feedback from the engineering team regarding product X on DATE with NAME.",
        "startDate": "2025-01-01T06:00:00.000+0000",
        "dueDate": "2025-01-01T06:00:00.000+0000",
        "timeZone": "America/Los_Angeles",
        "isAllDay": True,
        "priority": 3,
        "repeatFlag": "",
        "status": 0,
        "etag": "GENERIC_ETAG",
        "kind": "TEXT"
    }

    updated_task = update_ticktick_task(example_task_data)
    print(json.dumps(updated_task, indent=2))
