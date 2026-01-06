# Milestone 4 – Multi-Agent Orchestration with API & Frontend

## 📌 Objective
The objective of Milestone 4 is to design and implement a **multi-agent system** where different agents collaborate to process a user query.  
This milestone exposes the agent workflow through a **FastAPI backend** and provides a **Streamlit frontend** for user interaction.

---

## 🧠 Features Implemented

- Multiple agents with separate responsibilities
  - Research Agent
  - Summary Agent
- Central workflow to orchestrate agent execution
- FastAPI backend to serve agent responses
- Streamlit frontend for easy user interaction
- End-to-end communication between frontend and backend

---

## 📁 Project Structure

Milestone4/
│
├── agents/
│ ├── research_agent.py
│ └── summary_agent.py
│
├── api.py
├── workflow.py
├── frontend.py
└── README.md


---

## ⚙️ Technologies Used

- Python
- LangChain (classic)
- Google Gemini API
- FastAPI
- Uvicorn
- Streamlit

