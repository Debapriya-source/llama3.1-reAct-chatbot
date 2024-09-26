import os
from dotenv import dotenv_values
import streamlit as st
from groq import Groq
from agent import agent
from langchain_core.messages import HumanMessage, AIMessage

# frontend congifurations
st.set_page_config(
    page_title="Llama Think with web",
    page_icon=":robot:",
    layout="centered",
)

st.title("Llama Think with web")
st.caption("🚀 A Streamlit chatbot powered by Groq and Meta")

GROQ_API_KEY = dotenv_values(".env")["GROQ_API_KEY"]
os.environ['GROQ_API_KEY'] = GROQ_API_KEY
client = Groq()

if "messages" not in st.session_state:
    st.session_state["messages"] = [AIMessage(content="How can I help you")]

for msg in st.session_state.messages:
    st.chat_message(msg.type).write(msg.content)

if prompt := st.chat_input():

    st.session_state.messages.append(HumanMessage(content=prompt))
    st.chat_message("user").write(prompt)

    try:
        response = AIMessage(content=(agent(prompt)))
    except:
        response = AIMessage(content="API limit exceeded")
    print(response)
    # msg = response
    st.session_state.messages.append(response)
    st.chat_message("assistant").write(response.content)
