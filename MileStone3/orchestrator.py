from agents.research_agent import create_research_agent
from agents.summarization_agent import create_summarization_agent
from memory.shared_memory import create_shared_memory

shared_memory = create_shared_memory()

def run_pipeline(user_query: str):
    """
    Orchestrates collaboration between research and summarization agents.
    """

    research_agent = create_research_agent()
    summarization_agent = create_summarization_agent()

    # Step 1: Research agent
    research_prompt = f"Research the following topic and list key points:\n{user_query}"
    research_output = research_agent.run(research_prompt)

    # Save to shared memory
    shared_memory.save_context(
        {"input": user_query},
        {"output": research_output}
    )

    # Step 2: Summarization agent
    summary_prompt = f"Summarize the following research clearly:\n{research_output}"
    summary_output = summarization_agent.run(summary_prompt)

    return research_output, summary_output
