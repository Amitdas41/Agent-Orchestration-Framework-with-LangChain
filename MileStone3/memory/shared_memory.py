from langchain_community.memory import VectorStoreRetrieverMemory
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

def create_shared_memory():
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    vectorstore = FAISS.from_texts([], embedding=embeddings)

    return VectorStoreRetrieverMemory(
        retriever=vectorstore.as_retriever()
    )
