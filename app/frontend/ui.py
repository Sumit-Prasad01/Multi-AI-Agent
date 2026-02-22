import streamlit as st
import requests

from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

st.set_page_config(page_title="Multi AI Agent 🤖", layout="centered")
st.title("Multi AI Agent using Groq and Tavily")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

system_prompt = st.text_area("Define your AI Agent:", height=70)
selected_model = st.selectbox("Select your AI model:", settings.ALLOWED_MODEL_NAMES)
allow_web_search = st.checkbox("Allow web search")

user_query = st.text_area("Enter your query:", height=150)

API_URL = "http://127.0.0.1:9999/chat"

if st.button("Ask Agent") and user_query.strip():

    
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_query
    })

    payload = {
        "model_name": selected_model,
        "system_prompt": system_prompt,
        "messages": st.session_state.chat_history, 
        "allow_search": allow_web_search
    }

    try:
        logger.info("Sending request to backend.")

        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:

            agent_response = response.json().get("response", "")

            
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": agent_response
            })

            logger.info("Successfully received response from backend")

        else:
            logger.error(response.text)
            st.error(response.json().get("detail", "Backend error"))

    except Exception as e:
        logger.exception("Error occurred while communicating with backend")
        st.error(str(CustomException("Failed to communicate with backend")))


if st.session_state.chat_history:
    st.subheader("Conversation")

    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f"**🧑 You:** {message['content']}")
        else:
            st.markdown(f"**🤖 Agent:** {message['content']}")