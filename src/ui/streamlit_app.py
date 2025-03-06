import streamlit as st
import os
import sys
from pathlib import Path
from praisonaiagents import Agent

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.config import get_default_config, get_knowledge_path

def init_agent():
    config = get_default_config()
    
    return Agent(
        name="Knowledge Agent",
        instructions="You answer questions based on the provided knowledge.",
        knowledge=[get_knowledge_path("kw.txt")],
        knowledge_config=config,
        user_id="user1",
        llm="deepseek-r1"
    )

st.title("Knowledge Agent Chat")

if "agent" not in st.session_state:
    st.session_state.agent = init_agent()
    st.session_state.messages = []

if "messages" in st.session_state:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

prompt = st.chat_input("Ask a question...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.session_state.agent.start(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response}) 