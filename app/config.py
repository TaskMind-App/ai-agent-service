from langchain_ollama import OllamaLLM

# הגדרות בסיסיות
OLLAMA_BASE_URL = "http://localhost:11434"
TASK_SERVICE_URL = "http://localhost:8090/api/tasks/user"

# יצירת ה-Client של ה-LLM
llm = OllamaLLM(model="llama3.2:1b", base_url=OLLAMA_BASE_URL)