from agent import create_agent

def main():
    agent = create_agent()

    print("=== Milestone 2: Tool-Enabled Gemini Agent ===")
    print("Type 'exit' to quit\n")

    print("Try examples:")
    print("- What is 25 * 4 + 10?")
    print("- What is the weather in Delhi?")
    print("- Calculate 10 + 5 and tell weather in Mumbai\n")

    while True:
        query = input("You: ").strip()
        if query.lower() == "exit":
            print("Agent: Goodbye!")
            break

        try:
            response = agent.run(query)
        except Exception as e:
            response = f"Agent error: {e}"

        print("Agent:", response)

if __name__ == "__main__":
    main()
