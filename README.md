# Agent Orchestration Framework using LangChain & Gemini

## 📌 Project Overview
This project demonstrates the step-by-step development of an **AI Agent Orchestration System** using **LangChain** and **Google Gemini API**.  
The system is built incrementally using **four milestones**, following an **Agile development approach**.

The final solution includes:
- Intelligent AI agents
- Tool usage
- Multi-agent collaboration
- FAST API backend
- Web-based frontend
- Agile documentation
- Unit testing
- Defect tracking

---

## 📁 Project Structure

agent-orchestration-langchain/
│
├── Milestone1/
├── Milestone2/
├── Milestone3/
├── Milestone4/
│
├── Unit_tests/
├── Agile_Documents/
├── defects_Tacker/
│
├── venv/
├── .env
└── README.md


---

## 🧠 Milestone-wise Description

### 🔹 Milestone 1 – Basic Single Agent
**Objective:**  
Create a basic AI agent that interacts through the console.

**Features:**
- Single agent
- Prompt-based interaction
- Console input/output
- Uses Gemini API

**Outcome:**  
A working AI agent that answers simple questions.

---

### 🔹 Milestone 2 – Tool Integration
**Objective:**  
Enable the agent to use external tools.

**Features:**
- Calculator tool
- Tool reasoning
- Error handling

**Outcome:**  
Agent can decide when to use tools for solving tasks.

---

### 🔹 Milestone 3 – Multi-Agent Workflow
**Objective:**  
Introduce collaboration between multiple agents.

**Features:**
- Research agent
- Summary agent
- Orchestrated workflow

**Outcome:**  
Agents work together to research and summarize topics.

---

### 🔹 Milestone 4 – API & Frontend Integration
**Objective:**  
Expose the multi-agent system using an API and a frontend.

**Features:**
- FastAPI backend
- Streamlit frontend
- REST endpoint
- End-to-end interaction

**Outcome:**  
Users can interact with the system via a web interface.

---

## 🔁 Agile Development Approach

This project follows **Agile methodology**, where development is divided into small, manageable iterations (milestones).

### Agile Practices Used:
- Incremental development (Milestone 1 → 4)
- Continuous testing after each milestone
- Regular improvements and refactoring
- Clear definition of milestone objectives

### Agile Documents Maintained:
- Sprint-wise milestone planning
- Task breakdown for each milestone
- Continuous feedback and fixes

---

## 🧪 Unit Testing

Unit tests are written to ensure that:
- Agents return valid responses
- Tools work correctly
- Workflow executes without errors
- API endpoints respond as expected

### Testing Scope:
- Agent creation functions
- Workflow execution
- API response validation

Tests are placed inside the `tests/` folder and can be extended further.

---

## 🐞 Defect Tracking

Defects identified during development were tracked and resolved systematically.

### Defect Tracking Includes:
- Issue description
- Root cause analysis
- Fix applied
- Verification status

Common defects fixed:
- Import errors
- API parameter validation errors
- Agent function name mismatches
- Environment configuration issues

Defect details are maintained in the `defects/` folder.

---

## ⚙️ Technologies Used
- Python
- LangChain (classic)
- Google Gemini API
- FastAPI
- Uvicorn
- Streamlit

