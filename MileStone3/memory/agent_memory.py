from langchain_community.memory import ConversationBufferMemory

def create_agent_memory():
    return ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
