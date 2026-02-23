import requests
from app.config import llm, TASK_SERVICE_URL
from app.prompts import summary_prompt


def generate_task_summary(user_id: str):
    headers = {"Accept": "application/json", "X-User-Id": user_id}
    params = {"completed": "false"}

    response = requests.get(f"{TASK_SERVICE_URL}/{user_id}", headers=headers, params=params)
    response.raise_for_status()

    tasks_data = response.json()

    chain = summary_prompt | llm
    return chain.invoke({"tasks": tasks_data})