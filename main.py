from youtube_transcript_api import YouTubeTranscriptApi
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
yt_api = YouTubeTranscriptApi()

model = OllamaLLM(model="gemma3:1b")

class UserInput(BaseModel):
    url : str

class ModelInput(BaseModel):
    user_input : str
    summary : str

prompt = PromptTemplate.from_template("""
You are a professional assistant with a clear, concise, and respectful communication style. 
You are knowledgeable and provide well-structured, accurate explanations based on the given context. 
Always maintain a professional tone and respond directly to the user's questions.

Context: {context}
Human: {input}
AI:
""")

@app.get("/")
def greet():
    return "Hi, How are you"

def get_transcription(url):
    def get_video_id(url):
        index = url.index("v=") + 2
        vid_id = url[index:]
        return vid_id

    video_id = get_video_id(url)

    fetched_transcription  = yt_api.fetch(video_id)

    text = " ".join(snippet.text for snippet in fetched_transcription)

    return text

@app.post("/get-summary")
def summarizer(input: UserInput):
    template = PromptTemplate.from_template("Summarize the following: {text} and identity and understand the context and give summary points.")

    chain = template | model

    text = get_transcription(url = input.url)

    summary = chain.invoke({"text": text})

    return summary

@app.post("/generate-response")
def generate_response(input: ModelInput):
    user_input = input.user_input
    summary = input.summary

    chain = prompt | model
    response = chain.invoke({"context": summary, "input": user_input})

    return response


