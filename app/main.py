from fastapi import FastAPI, Header, HTTPException
from app.services.ai_logic import generate_task_summary
import uvicorn
from py_eureka_client import eureka_client
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await eureka_client.init_async(
        eureka_server="http://discovery-service:8761/eureka",
        app_name="ai-agent-service",
        instance_port=8000
    )
    yield
    await eureka_client.stop_async()
app = FastAPI()

@app.get("/api/ai/summary")
def get_summary(x_user_id: str = Header(None)):
    if not x_user_id:
        raise HTTPException(status_code=400, detail="Missing X-User-Id header")
    try:
        summary = generate_task_summary(x_user_id)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)