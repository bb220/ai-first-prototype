import streamlit as st
from main import agent

st.set_page_config(page_title="Finance Copilot 💸", page_icon="💸")

st.title("💸 Finance Copilot")
st.markdown("Ask me anything about your finances.")

# --- Session State Init ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending_user_input" not in st.session_state:
    st.session_state.pending_user_input = None
if "generating_response" not in st.session_state:
    st.session_state.generating_response = False

# --- Handle New Input ---
user_input = st.chat_input("Ask your finance copilot something...")

# Capture new user input, trigger response generation
if user_input and not st.session_state.generating_response:
    st.session_state.pending_user_input = user_input
    st.session_state.generating_response = True

# --- Render Existing Chat History (excluding last assistant message if pending response) ---
messages_to_render = (
    st.session_state.messages[:-1]
    if st.session_state.generating_response and st.session_state.messages and st.session_state.messages[-1]["role"] == "assistant"
    else st.session_state.messages
)

for msg in messages_to_render:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- If we have a pending user input, render it and generate response ---
if st.session_state.generating_response and st.session_state.pending_user_input:
    user_msg = st.session_state.pending_user_input

    # Show user input
    with st.chat_message("user"):
        st.markdown(user_msg)
    st.session_state.messages.append({"role": "user", "content": user_msg})

    # Show assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = agent.run(user_msg)
            except Exception as e:
                response = f"⚠️ Error: {e}"
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Clear pending input and trigger rerun
    st.session_state.pending_user_input = None
    st.session_state.generating_response = False
    st.rerun()
