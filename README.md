# 🤖 Saurabh AI Local

## Project Overview

**Saurabh AI Local** is a self-hosted AI chatbot built using Python, Streamlit, Ollama, and the Qwen 3.5 local language model.

Unlike API-based chatbots, the AI model runs directly on the local computer.

This means the application does not depend on Gemini or OpenAI API quotas for generating responses.

The project also supports remote access through ngrok, allowing another person to use the chatbot from their phone or computer while the host PC is running.

---

## 🎯 Project Goal

The main goal of this project was to create an AI chatbot that:

- Runs locally on my own computer
- Does not depend on Gemini daily API limits
- Does not require a paid AI API
- Supports ChatGPT-style conversations
- Remembers the current conversation
- Can be shared temporarily with other users through a public link
- Can be started easily using a single launcher file

---

# 🛠 Technologies Used

## Python

Python is used as the main programming language.

## Streamlit

Streamlit is used to build the ChatGPT-style web interface.

## Ollama

Ollama is used to run the AI model locally on the computer.

## Qwen 3.5

The chatbot currently uses a lightweight Qwen 3.5 model suitable for local inference.

Model used:

```text
qwen3.5:2b-q4_K_M
```

## ngrok

ngrok is used to create a temporary public internet link for the locally running application.

## GitHub

GitHub is used to store and manage the project source code.

---

# 🧠 How the Application Works

The local application architecture is:

```text
User
  ↓
Streamlit Chat Interface
  ↓
Python Application
  ↓
Ollama
  ↓
Qwen Local AI Model
  ↓
Generated Response
  ↓
Displayed to User
```

The AI inference happens on the host computer.

---

# 🌐 Remote User Architecture

When another person uses the application remotely, the flow becomes:

```text
Friend's Phone / Computer
          ↓
      ngrok URL
          ↓
       Internet
          ↓
      Host Computer
          ↓
       Streamlit
          ↓
        Ollama
          ↓
   Qwen AI Model
          ↓
       Response
          ↓
Remote User
```

The remote user does not need to install:

```text
Python ❌
VS Code ❌
Ollama ❌
Qwen Model ❌
```

The remote user only needs:

```text
Web Browser ✅
Internet Connection ✅
Active ngrok Link ✅
```

---

# 📁 Project Structure

```text
saurabh-ai-local/
│
├── app.py
├── requirements.txt
├── .gitignore
├── start_ai.bat
└── README.md
```

Local-only files may also include:

```text
.venv/
__pycache__/
```

These files are not required in the GitHub repository.

---

# 📦 Python Virtual Environment

A Python virtual environment is used to keep this project's packages separate.

The environment was created using:

```bash
python -m venv .venv
```

---

# 📚 Required Python Packages

The project requires:

```text
streamlit
ollama
```

These packages are listed in:

```text
requirements.txt
```

They can be installed using:

```bash
python -m pip install streamlit ollama
```

---

# 🤖 Local AI Model

The AI model is downloaded using Ollama.

Command:

```bash
ollama pull qwen3.5:2b-q4_K_M
```

The model can also be tested directly using:

```bash
ollama run qwen3.5:2b-q4_K_M
```

Example prompt:

```text
Explain VLAN in simple Hinglish.
```

---

# 💬 ChatGPT-Style Interface

The application uses Streamlit chat components.

Chat input:

```python
st.chat_input("Message Saurabh AI...")
```

User messages:

```python
st.chat_message("user")
```

Assistant messages:

```python
st.chat_message("assistant")
```

This creates a conversational interface similar to modern AI chat applications.

---

# 🧠 Conversation Memory

The current conversation is stored using:

```python
st.session_state.messages
```

This allows follow-up conversations such as:

```text
User:
What is VLAN?

AI:
VLAN stands for Virtual Local Area Network...

User:
Give me a real-life example.

AI:
...
```

The current version uses temporary session-based memory.

Permanent chat storage has not yet been added.

---

# ➕ New Chat Feature

A New Chat button is included in the sidebar.

When pressed, the current conversation is cleared.

Example:

```python
st.session_state.messages = []
st.rerun()
```

---

# ⚡ Streaming AI Responses

The application uses streaming responses so the AI answer appears gradually instead of waiting for the complete response.

The Ollama chat request uses:

```python
stream=True
```

This makes the chatbot feel more responsive and similar to modern AI assistants.

---

# 🎭 Custom AI Personality

The project includes a custom system prompt.

The assistant is configured to:

- Reply in Hinglish when the user uses Hindi or Hinglish
- Reply in English when the user uses English
- Explain technical concepts simply
- Give step-by-step explanations when useful
- Avoid intentionally inventing facts
- Keep responses concise unless more detail is requested

---

# ▶️ Running the Application Manually

The Streamlit application can be started using:

```bash
.\.venv\Scripts\python.exe -m streamlit run app.py
```

The application normally opens at:

```text
http://localhost:8501
```

---

# 🚀 One-Click Launcher

A Windows batch file named:

```text
start_ai.bat
```

was created to make the application easier to start.

Instead of manually running multiple commands, the user can double-click:

```text
start_ai.bat
```

The launcher:

```text
Checks / Starts Ollama
        ↓
Starts Streamlit
        ↓
Starts ngrok
        ↓
Creates a Public Link
```

This simplifies the startup process.

---

# 🌍 Remote Access with ngrok

After the Streamlit application is running, ngrok can expose the local application to the internet.

Command:

```bash
ngrok http 8501
```

ngrok generates a public URL similar to:

```text
https://example.ngrok-free.dev
```

This URL can be shared with another person.

They can open the link in their browser and use Saurabh AI.

---

# ⚠️ Important Remote Access Requirement

Because the AI model runs on the host PC, the host computer must remain available.

For remote access, these must remain running:

```text
Host PC ✅
Internet Connection ✅
Ollama ✅
Streamlit ✅
ngrok ✅
```

If the host computer is turned off, the remote AI application will stop working.

If Streamlit or ngrok is closed, the remote user will also lose access.

---

# 🔄 Local AI vs Cloud AI

## Local AI

This project uses:

```text
Streamlit
   ↓
Ollama
   ↓
Qwen Local Model
```

Advantages:

- No Gemini daily request quota
- No per-message AI API charge
- AI processing happens locally
- More control over the model
- Custom behavior can be added
- Useful for learning self-hosted AI systems

Limitations:

- Uses local CPU and RAM
- Speed depends on computer hardware
- Host PC must be running for remote users
- Large models may not run efficiently on low-end hardware

---

# 📊 Request Limits

This application does not use the Gemini API for its AI responses.

Therefore, it does not have a provider limit such as:

```text
20 Gemini requests per day
```

However, the application is not literally unlimited in every sense.

Practical limitations include:

- CPU performance
- RAM capacity
- Device temperature
- Internet upload speed
- Number of simultaneous users
- ngrok free-plan limits

The local computer provides the actual AI processing power.

---

# 🔐 Privacy

The AI model runs locally through Ollama.

The project does not require sending prompts to Gemini or OpenAI for model inference.

However, when ngrok is used, the application becomes reachable through a public internet tunnel.

For this reason, sensitive information should not be exposed through an unsecured public deployment.

Authentication can be added in a future version.

---

# 🐙 GitHub

The project source code is stored on GitHub.

The repository contains:

```text
app.py
requirements.txt
.gitignore
start_ai.bat
README.md
```

The Python virtual environment is excluded from GitHub using:

```text
.venv/
```

inside `.gitignore`.

---

# ✅ Current Features

- Local AI chatbot
- ChatGPT-style interface
- Qwen local AI model
- Ollama integration
- Streaming responses
- Conversation memory
- Follow-up question support
- New Chat button
- Custom AI personality
- Hinglish support
- No Gemini daily AI quota
- No paid AI API required
- One-click Windows launcher
- Temporary remote sharing through ngrok
- GitHub source-code storage

---

# 📚 What I Learned

This project helped me understand:

- Python
- Python virtual environments
- Streamlit
- AI chatbot interfaces
- Local LLMs
- Ollama
- Qwen models
- AI inference
- System prompts
- Session-based memory
- Streaming responses
- Localhost
- Ports
- Self-hosting
- ngrok tunnels
- Remote access
- GitHub
- `.gitignore`
- `requirements.txt`
- Windows batch files
- Local AI vs cloud AI architecture

---

# 🔮 Future Improvements

Possible future improvements include:

## Permanent Chat History

Store conversations in a database.

## Multiple Conversations

Add a ChatGPT-style conversation sidebar.

## User Authentication

Add login and password protection for remote users.

## Better UI

Improve the visual design, sidebar, themes, and animations.

## Larger AI Models

Use a stronger model when better hardware becomes available.

## PDF Support

Allow users to upload PDF files and ask questions.

## Image Understanding

Add support for image input using a multimodal model.

## Voice Input

Allow users to speak to the AI.

## Voice Output

Allow the AI to read answers aloud.

## Web Search

Give the AI access to current internet information.

## RAG

Allow the AI to answer questions using custom documents and notes.

## Permanent Public Server

Move the local model from a personal PC to a dedicated cloud or GPU server.

## Android Application

Create a mobile version of the chatbot.

## Windows Desktop Application

Package the project as a standalone Windows application.

## Admin Dashboard

Add usage information and user management.

---

# 📝 Summary

Saurabh AI Local started as an experiment to understand how an AI model can run without depending on a commercial AI API.

The development process included:

```text
Python Setup
      ↓
Virtual Environment
      ↓
Streamlit
      ↓
Ollama
      ↓
Qwen Local Model
      ↓
Chat Interface
      ↓
Conversation Memory
      ↓
Streaming Responses
      ↓
One-Click Launcher
      ↓
ngrok Remote Access
      ↓
GitHub Repository
```

The final result is a self-hosted AI chatbot where the AI model runs directly on the host computer.

---

# 👨‍💻 Project Information

**Project Name:** Saurabh AI Local

**Project Type:** Self-Hosted AI Chatbot

**Programming Language:** Python

**Web Framework:** Streamlit

**Local AI Runtime:** Ollama

**AI Model:** Qwen 3.5 2B

**Remote Access:** ngrok

**Source Code:** GitHub

**AI Processing:** Local Computer
