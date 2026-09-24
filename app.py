import streamlit as st
from ollama import chat

# -------------------------
# APP SETTINGS
# -------------------------

st.set_page_config(
    page_title="Saurabh AI",
    page_icon="🤖",
    layout="centered"
)

# -------------------------
# AI PERSONALITY
# -------------------------

SYSTEM_PROMPT = """
You are Saurabh AI.

You are a helpful, intelligent and friendly AI assistant.

Rules:
- Reply in Hinglish if the user speaks Hindi or Hinglish.
- Reply in English if the user speaks English.
- Explain difficult topics simply.
- Give step-by-step explanations for technical topics when useful.
- Do not invent facts if you are unsure.
- Keep answers concise unless the user asks for detail.
"""

# -------------------------
# CHAT MEMORY
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------
# SIDEBAR
# -------------------------

with st.sidebar:
    st.title("🤖 Saurabh AI")
    st.caption("Local AI")

    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.write("Model: Qwen 3.5 2B")
    st.write("Runs locally on this PC")
    st.write("No Gemini daily quota")

# -------------------------
# MAIN SCREEN
# -------------------------

st.title("🤖 Saurabh AI")
st.caption("Your personal local AI assistant")

# -------------------------
# OLD MESSAGES
# -------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------
# CHAT INPUT
# -------------------------

prompt = st.chat_input("Message Saurabh AI...")

if prompt:

    # User message save
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # User message show
    with st.chat_message("user"):
        st.markdown(prompt)

    # Messages model ko bhejne ke liye
    messages_for_model = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ] + st.session_state.messages

    # AI response
    with st.chat_message("assistant"):

        response_box = st.empty()
        answer = ""

        try:

            stream = chat(
                model="qwen3.5:2b-q4_K_M",
                messages=messages_for_model,
                stream=True,
                think=False
            )

            for chunk in stream:

                part = chunk.message.content

                if part:
                    answer += part
                    response_box.markdown(answer + "▌")

            response_box.markdown(answer)

        except Exception:
            answer = (
                "⚠️ Local AI is not available right now.\n\n"
                "Please make sure Ollama is running."
            )

            response_box.warning(answer)

    # AI answer history me save
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })