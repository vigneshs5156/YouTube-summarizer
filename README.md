# 🎥 YouTube Content Summarizer

A powerful and elegant web app that extracts **transcripts** from any YouTube video and generates a **smart summary**, along with an **interactive AI chat assistant** to ask questions about the content — just like ChatGPT!

---

## 🚀 Features

- 🔗 Paste any YouTube video URL and get the title and a detailed summary.
- 🧠 Ask questions about the summarized content using natural language.
- 📜 Auto-fetches transcripts via `youtube-transcript-api`.
- 🤖 Powered by `LangChain` and `Ollama` (LLM).
- 💬 Clean and conversational chat interface using Streamlit's native chat features.
- 📦 Modern frontend (Streamlit) and backend (FastAPI) architecture.

---

## 🖥️ Tech Stack

| Layer       | Technology            |
|-------------|------------------------|
| Frontend    | [Streamlit](https://streamlit.io) |
| Backend     | [FastAPI](https://fastapi.tiangolo.com) |
| LLM         | [LangChain](https://www.langchain.com) + Ollama (Gemma3:1b) |
| Transcript  | [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api) |
| HTML Parser | [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) |
| Deployment  | (You can use Streamlit Cloud + Render or run locally)

---

## 🧠 How It Works

### 1. 🔗 URL Input
- The user enters a YouTube URL.
- The app fetches and displays the **video title** using `requests` + `BeautifulSoup`.

### 2. 📄 Transcription & Summarization
- When you click `Get summary`, the URL is sent to the FastAPI backend.
- The backend uses `youtube-transcript-api` to fetch the full transcript.
- A LangChain prompt sends this transcript to a local LLM (`gemma3:1b`) via `Ollama` to summarize it.
- The summary is then returned and displayed in the left panel.

### 3. 💬 AI Chat Assistant
- You can ask follow-up questions about the summarized content.
- A custom prompt template ensures professional and relevant responses from the AI model.
- Messages are tracked using `st.session_state` to keep the chat history intact.

---

## 🧪 Sample Prompt Template

```text
You are a professional assistant with a clear, concise, and respectful communication style. 
You are knowledgeable and provide well-structured, accurate explanations based on the given context. 
Always maintain a professional tone and respond directly to the user's questions.

Context: {context}
Human: {input}
AI:
```

## ✅ Setup Instructions

### ⚙️ 1. Clone the Repository

```bash
git clone https://github.com/your-username/youtube-content-summarizer.git
cd youtube-content-summarizer
```

### 📦 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🧠 3. Start Ollama (if not already running)

```bash
ollama run gemma3:1b
```
### 🔙 4. Run FastAPI Backend

```bash
uvicorn main:app --reload
```

### 🖼️ 5. Run Streamlit Frontend

```bash
streamlit run streamlit_app.py
```
---

## 📌 Example Use Case
Paste this in the app:

```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```
✅ Get:

🎬 Title: Rick Astley - Never Gonna Give You Up

📖 Summary of the lyrics/transcript

💬 Ask: "What is the theme of this video?" — get smart answers instantly.

---

## 👨‍💻 Author
Built with ❤️ by Vignesh S



