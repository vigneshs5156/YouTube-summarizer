import streamlit as st
import requests
import json
from bs4 import BeautifulSoup

st.set_page_config(layout="wide")

st.title("Youtube Content Summarizer")

url = st.text_input("Enter the URL")
input = {"url": url}
data = json.dumps(input)

if url:
    try:
        html = requests.get(url=url).text
        soup = BeautifulSoup(html, "html.parser")
        title_tag = soup.find("title")
        if title_tag:
            video_title = title_tag.text.replace(" - YouTube", "")
            st.subheader(f"🎬 Video Title: {video_title}")
        else:
            st.warning("Could not extract the title from the page.")
    except Exception as e:
        st.error(f"Failed to fetch title: {e}")

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "messages" not in st.session_state:
    st.session_state.messages = []


col1, col2 = st.columns([8, 4])  

with col1:
    if st.button("Get summary"):
        with st.spinner("⏳ Loading..."):
            try:
                response = requests.post(
                    url="http://127.0.0.1:8000/get-summary",
                    data=data,
                    headers={"Content-Type": "application/json"}
                )
                if response.status_code == 200:
                    result = json.loads(response.text)
                    st.session_state.summary = result
                    st.subheader("📖 Summary")
                    st.markdown(result.replace("\n", "  \n"))
                else:
                    st.error(f'Backend error: {response.status_code}')
            except Exception as e:
                st.error(f"Request failed: {e}")
    else:
        if st.session_state.summary:
            st.markdown(st.session_state.summary.replace("\n", "  \n"))
        else:
            st.info("No summary yet.")

with col2:
    st.subheader("💬 Chat with LLM")

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input
    if prompt := st.chat_input("Type your message..."):
        # Save user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Send to backend
        with st.chat_message("assistant"):
            inputs = {
                "user_input": prompt,
                "summary": st.session_state.summary
            }
            model_data = json.dumps(inputs)
            print("Payload to /generate-response:")
            print(inputs)
            model_response = requests.post(
                url="http://127.0.0.1:8000/generate-response",
                data=model_data,
                headers={"Content-Type": "application/json"}
            )
            response_text = json.loads(model_response.text)
            st.markdown(response_text)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response_text
        })
