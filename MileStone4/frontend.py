import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/process"

st.title("Milestone 4 – Multi-Agent Orchestration")

user_input = st.text_input("Enter your topic")

if st.button("Run Agents"):
    if user_input:
        response = requests.post(
            API_URL,
            json={"query": user_input}
        )

        if response.status_code == 200:
            result = response.json()
            st.subheader("Research Output")
            st.write(result["research"])

            st.subheader("Summary Output")
            st.write(result["summary"])
        else:
            st.error("Backend error")
