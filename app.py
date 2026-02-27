import streamlit as st

from prompts import SYSTEM_PROMPT
from utils import (
    get_llm_response,
    is_exit_command,
    analyze_sentiment
)

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="TalentScout Hiring Assistant",
    page_icon="🤖",
    layout="centered"
)

# -------------------------
# Sidebar
# -------------------------
st.sidebar.title("About TalentScout")
st.sidebar.info(
    """
    TalentScout AI Hiring Assistant
    
    This chatbot helps conduct initial candidate screening 
    by collecting information and generating technical 
    interview questions based on your skills.
    """
)

# -------------------------
# Main Title
# -------------------------
st.title("🤖 TalentScout Hiring Assistant")
st.write("Welcome! I will guide you through the initial screening process.")

# -------------------------
# Initialize Session State
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

if "conversation_ended" not in st.session_state:
    st.session_state.conversation_ended = False

# -------------------------
# Display Previous Messages
# -------------------------
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------
# Chat Input
# -------------------------
if not st.session_state.conversation_ended:
    user_input = st.chat_input("Type your response here...")

    if user_input:

        # Exit Handling
        if is_exit_command(user_input):
            farewell = (
                "Thank you for applying to TalentScout. "
                "Our recruitment team will review your profile and contact you soon. "
                "Have a great day!"
            )

            with st.chat_message("assistant"):
                st.markdown(farewell)

            st.session_state.messages.append(
                {"role": "assistant", "content": farewell}
            )

            st.session_state.conversation_ended = True
            st.stop()

        # Display user message
        with st.chat_message("user"):
            st.markdown(user_input)

        # Sentiment analysis
        sentiment = analyze_sentiment(user_input)
        st.sidebar.write(f"Candidate Sentiment: {sentiment}")

        # Save user message
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        # Generate bot reply (offline logic)
        reply = get_llm_response(st.session_state.messages)

        # Save assistant reply
        st.session_state.messages.append(
            {"role": "assistant", "content": reply}
        )

        # Display assistant reply
        with st.chat_message("assistant"):
            st.markdown(reply)

else:
    st.info("Conversation has ended. Please refresh the page to start again.")
