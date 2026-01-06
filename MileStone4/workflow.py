from agents.research_agent import get_research_agent
from agents.summary_agent import get_summary_agent

def run_full_workflow(topic):
    research_agent = get_research_agent()
    summary_agent = get_summary_agent()

    research_prompt = f"""
    Research the topic below and write important points:

    Topic: {topic}
    """
    research_result = research_agent.run(research_prompt)

    summary_prompt = f"""
    Summarize the following content in simple words:

    {research_result}
    """
    summary_result = summary_agent.run(summary_prompt)

    return research_result, summary_result
