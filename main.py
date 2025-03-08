import streamlit as st
from chatbot import Chatbot
import os

chatbot = Chatbot()

logo_path = os.path.join('misc', 'cougar_ai_logo.png')

st.set_page_config(page_title="Cougar AI Adorable Chatbot", page_icon="🤖")
with st.container():         
    img_col, title_col = st.columns((1, 2))
    with img_col:
        st.image(logo_path)
    with title_col:
        st.title('Embrace the Future')

with st.sidebar:
    st.sidebar.header("Chatbot Settings")
    temperature = st.sidebar.slider("Temperature (Creativity)", 0.0, 1.0, 0.7, 0.1)
    personality = st.sidebar.selectbox("Personality", ["Friendly", "Professional", "Sarcastic", "Encouraging", "Direct"])
    chatbot.set_temperature(temperature)
    chatbot.set_personality(personality)


st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by Ollma")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    msg = chatbot.invoke(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)