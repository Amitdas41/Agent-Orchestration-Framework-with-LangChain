# Agent Orchestration Framework using LangChain

## Project Overview
This project demonstrates the step-by-step development of an **AI Agent Orchestration System** using **LangChain** and the **Google Gemini API**.  
The project is built using an **Agile approach**, where features are added gradually through four milestones.

Each milestone improves the system and adds new functionality, starting from a basic agent and ending with a complete system with API and UI support.

---

## Project Structure (Milestone-wise)

agent-orchestration-framework/
│
├── Milestone1/
├── Milestone2/
├── Milestone3/
├── Milestone4/
│
├── Unit_tests/
├── Agile_Documents/
├── Defects_Tracker/
│
├── requirements.txt
├── .env.example
└── README.md


---

## Milestone 1 – Basic Single Agent

### Objective
To create a simple AI agent that can interact with the user through the console.

### What is implemented
- A single AI agent
- Prompt-based interaction
- Console input and output
- Connection with Google Gemini API

### Outcome
A basic working AI agent that can answer simple user questions.

---

## Milestone 2 – Tool Integration

### Objective
To allow the agent to use external tools when required.

### What is implemented
- Tool integration (example: calculator)
- Agent reasoning to decide when to use a tool
- Basic error handling

### Outcome
The agent can now use tools to solve tasks more accurately instead of only relying on text responses.

---

## Milestone 3 – Multi-Agent Workflow

### Objective
To enable multiple agents to work together using an orchestrated workflow.

### What is implemented
- Research agent
- Summarization agent
- Orchestrator to manage agent flow
- Individual and shared memory

### Outcome
Multiple agents collaborate to complete a task by sharing information and working step by step.

---

## Milestone 4 – API & Frontend Integration

### Objective
To expose the multi-agent system through an API and a user interface.

### What is implemented
- FastAPI backend
- REST API endpoints
- Streamlit-based frontend
- End-to-end user interaction

### Outcome
Users can interact with the multi-agent system through a web interface instead of the console.

---

## Agile Development Approach

This project follows Agile methodology with:
- Incremental development using milestones
- Testing after each milestone
- Continuous improvements and refactoring
- Clear objectives for every phase



---

## Unit Testing
Unit tests are written to verify:
- Agent responses
- Tool functionality
- Workflow execution
- API responses



---

## Defect Tracking
Issues found during development were tracked and fixed properly.

Defect details include:
- Issue description
- Root cause
- Fix applied
- Verification status


---

## Technologies Used
- Python
- LangChain
- Google Gemini API
- FastAPI
- Streamlit

---

## Conclusion
This project shows how an AI system can be built step by step using agents, tools, memory, and orchestration.  
The milestone-based approach helps in understanding real-world AI system development clearly and practically.
