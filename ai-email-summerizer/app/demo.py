import requests
import streamlit as st

API_URL = "http://127.0.1:8000/summarize"

st.set_page_config(page_title="Email Summarizer", page_icon="✉️", layout="centered")

st.title("✉️ AI Email Summarizer")
st.write("Enter your email content below, and the AI will summarize it for you.")

email_input = st.text_area("Email Content", height=300)

if st.button("Summarize"):
    if not email_input.strip():
        st.error("Please enter some email content to summarize.")
    else:
        with st.spinner("Summarizing..."):
            try:
                response = requests.post(API_URL, json={"email": email_input}, timeout=60)
                response.raise_for_status()
                result = response.json()

                st.subheader("Summary")
                st.write(result["summary"])
                st.subheader("Priority")
                st.write(result["priority"])
                st.subheader("Sentiment")
                st.write(result["sentiment"])
                st.subheader("Action Items")

                for item in result["action_items"]:
                    st.markdown(
                        f"- **Task:** {item['task']}  \n"
                        f"  **Owner:** {item['owner']}  \n"
                        f"  **Deadline:** {item['deadline']}"
                    )

                st.subheader("Suggested Reply")
                st.write(result["suggested_reply"])
                
            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred: {e}")