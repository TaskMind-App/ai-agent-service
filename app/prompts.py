from langchain_core.prompts import PromptTemplate

SUMMARY_TEMPLATE = """
You are a personal assistant. Here is a list of tasks:
{tasks}
Please summarize the three most important tasks that should be completed today, and also recommend the most urgent or important task that should be completed quickly. In addition, provide one tip for productivity today.
Expose only the name and the description of the task, and write the summary base on this information. the summary will be limited to 7 sentences.
Respond in English.
"""

summary_prompt = PromptTemplate(input_variables=["tasks"], template=SUMMARY_TEMPLATE)