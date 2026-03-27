import streamlit as st
import requests

st.set_page_config(page_title="AI Customer Support", layout="centered")

st.title("🤖 AI Customer Support")

# Session state init
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Type your message")

if st.button("Send"):
    if user_input:
        try:
            # Call backend chat API
            response = requests.post(
                "http://127.0.0.1:8020/chat",
                json={"query": user_input}
            )

            data = response.json()

            # Save chat in session
            st.session_state.chat_history.append({
                "user": user_input,
                "bot": data["ai_response"]
            })

        except Exception as e:
            st.error(f"Error: {e}")

# Display chat
for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")