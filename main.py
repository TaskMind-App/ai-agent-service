from fastapi import FastAPI, Header
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
import requests

app = FastAPI()

# 1. הגדרת ה"מוח" המקומי (Ollama)
llm = OllamaLLM(model="llama3.2:1b", base_url="http://localhost:11434")


template = """
You are a personal assistant. Here is a list of tasks for the user:
{tasks}

Please summarize these tasks into 3 main bullet points and provide one tip for productivity today.
Respond in English.
"""

prompt = PromptTemplate(input_variables=["tasks"], template=template)


@app.get("/api/ai/summary")
def get_ai_summary(x_user_id: str = Header(None)):
    try:
        # 2. פנייה לסרוויס ה-Java (שימי לב: כשנריץ בדוקר זה יהיה task-service)
        # כרגע, אם את מריצה מקומית ב-PyCharm, השתמשי ב-localhost
        headers = {
            "Accept": "application/json",
            "X-User-Id": str(x_user_id)
        }
        response = requests.get(f"http://localhost:8090/api/tasks/user/{x_user_id}", headers=headers)
        tasks_data = response.json()

        # 3. הפעלת השרשרת
        formatted_prompt = prompt.format(tasks=tasks_data)
        summary = llm.invoke(formatted_prompt)

        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    # הפקודה הזו מפעילה את השרת ידנית כשהדיבאגר של PyCharm מריץ את הקובץ
    uvicorn.run(app, host="127.0.0.1", port=8000)