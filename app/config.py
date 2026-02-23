import os
from langchain_ollama import OllamaLLM

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
GATEWAY_URL = os.getenv("GATEWAY_URL", "http://localhost:8090")

TASK_SERVICE_URL = f"{GATEWAY_URL}/api/tasks/user"

llm = OllamaLLM(model="llama3.2:1b", base_url=OLLAMA_BASE_URL)