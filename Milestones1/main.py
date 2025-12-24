import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.prompts import PromptTemplate
from langchain_classic.chains import LLMChain

# Load environment variables from .env
load_dotenv()


def get_llm():
    """
    Creates and returns a Gemini LLM instance.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GOOGLE_API_KEY is missing. Please add it to your .env file."
        )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=api_key,
        temperature=0.3,
    )
    return llm


def build_chain(llm):
    """
    Builds a basic PromptTemplate + LLMChain.
    """
    prompt = PromptTemplate(
        input_variables=["topic"],
        template=(
            "You are a friendly teacher.\n"
            "Explain the following topic in very simple words so that a beginner can understand.\n\n"
            "Topic: {topic}"
        ),
    )

    chain = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=False,
    )
    return chain


def main():
    print("=== Milestone 1: Basic LangChain Agent (Gemini) ===")
    print("Type 'exit' to quit.\n")

    llm = get_llm()
    chain = build_chain(llm)

    while True:
        user_input = input("Enter a topic: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        if not user_input:
            continue

        try:
            response = chain.run(user_input)
            print("\nAnswer:")
            print(response)
            print("-" * 50)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
