# TaskMind - AI Agent Service

## 📝 Overview
The **AI Agent Service** is the intelligence engine of the TaskMind ecosystem. It leverages Artificial Intelligence to transform raw task data into actionable insights, providing users with smart summaries, productivity forecasting, and personalized tips.

## 🚀 Key Responsibilities
* **AI-Driven Insights:** Processing complex user data to generate natural language summaries and productivity recommendations.
* **Model Integration:** Securely interfacing with external AI/ML models (e.g., OpenAI, Hugging Face) or internal LLM pipelines.
* **Scalable Analysis:** Providing high-availability API endpoints for real-time intelligent content generation.

## 🛠 Tech Stack
* **Language:** Java (OpenJDK 17+) / Python (for ML integration)
* **Framework:** Spring Boot / Maven
* **AI/ML:** LangChain , Ollama
* **Service Mesh:** Integrated with Gateway & Discovery Services (Netflix Eureka/Consul)
* **Containerization:** Dockerized for independent scaling

## 🏗 Architecture Context
The AI Agent Service operates as a specialized consumer within the TaskMind distributed system:
1.  **Request:** The TaskMind UI requests a summary for a user's weekly tasks.
2.  **Flow:** The request passes through the **Gateway Service**, which validates the JWT (issued by the User Service).
3.  **Processing:** The AI Agent Service fetches relevant data, processes it via AI models, and returns the result.
4.  **Discovery:** Registers with the **Discovery Service** to allow dynamic scaling based on computational demand.

## 🛣 API Endpoints (Quick Look)
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/ai/summary` | Generate a smart summary of specific tasks |
| `GET` | `/api/ai/tips` | Fetch personalized productivity insights |
| `POST` | `/api/ai/analyze` | Analyze task patterns for efficiency bottlenecks |

## 📦 Getting Started
To run the AI Agent Service locally:

```bash
# Build the image
docker build -t taskmind-ai-service .

# Run the container
docker run -p 8083:8083 taskmind-ai-service
