from orchestrator import run_pipeline

def main():
    print("=== Milestone 3: Multi-Agent Orchestration & Memory ===\n")

    topic = input("Enter a research topic: ")

    research, summary = run_pipeline(topic)

    print("\n--- Research Output ---")
    print(research)

    print("\n--- Summary Output ---")
    print(summary)

if __name__ == "__main__":
    main()
