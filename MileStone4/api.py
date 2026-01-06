from fastapi import FastAPI
from workflow import run_full_workflow

app = FastAPI()

@app.get("/process")
def process_topic(topic: str):
    research, summary = run_full_workflow(topic)

    return {
        "topic": topic,
        "research_output": research,
        "summary_output": summary
    }
