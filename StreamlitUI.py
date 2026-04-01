import streamlit as st
st.set_page_config(page_icon=":robot:",page_title="AI Chatbot",layout='wide')
st.header("🤖 AI Chatbot")
st.markdown("""<h5><b>🧠 Define how your agent should Act:</b></h5>""",unsafe_allow_html=True)
system_prompt=st.text_area(label="system prompt",placeholder="Type system prompt here.....",label_visibility="collapsed")
st.markdown("""<h5><b><svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px" fill="#1f1f1f"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M9 13.75c-2.34 0-7 1.17-7 3.5V19h14v-1.75c0-2.33-4.66-3.5-7-3.5zM4.34 17c.84-.58 2.87-1.25 4.66-1.25s3.82.67 4.66 1.25H4.34zM9 12c1.93 0 3.5-1.57 3.5-3.5S10.93 5 9 5 5.5 6.57 5.5 8.5 7.07 12 9 12zm0-5c.83 0 1.5.67 1.5 1.5S9.83 10 9 10s-1.5-.67-1.5-1.5S8.17 7 9 7zm7.04 6.81c1.16.84 1.96 1.96 1.96 3.44V19h4v-1.75c0-2.02-3.5-3.17-5.96-3.44zM15 12c1.93 0 3.5-1.57 3.5-3.5S16.93 5 15 5c-.54 0-1.04.13-1.5.35.63.89 1 1.98 1 3.15s-.37 2.26-1 3.15c.46.22.96.35 1.5.35z"/></svg> Select Provider:</b></h5>""",unsafe_allow_html=True)
provider=st.radio(label="provider:",options=("Groq","OpenAI","Ollama","Google"),label_visibility="collapsed")
Groq_Model=['llama-3.1-8b-instant','llama-3.3-70b-versatile','meta-llama/llama-guard-4-12b']
OpenAI_Model=['GPT-4o mini']
Ollama_Model=['llama3.1:8b','deepseek-r1:8b','llama3.2:3b','mistral:7b','qwen2.5:7b']
Google_Model=['gemini-2.0-flash','gemini-2.5-flash','gemini-2.5-pro']
if provider == "Groq":
    selected_model=st.selectbox("Select Groq Model:",Groq_Model)
elif provider == "OpenAI":
    selected_model=st.selectbox("Select OpenAI Model:",OpenAI_Model)
elif provider == "Ollama":
    selected_model=st.selectbox("Select Ollama Model:",Ollama_Model)
elif provider == "Google":
    selected_model=st.selectbox("Select Google Model:",Google_Model)
st.markdown("""<h5> <svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24px" viewBox="0 0 24 24" width="24px" fill="#1f1f1f"><rect fill="none" height="24" width="24"/><path d="M11.71,17.99C8.53,17.84,6,15.22,6,12c0-3.31,2.69-6,6-6c3.22,0,5.84,2.53,5.99,5.71l-2.1-0.63C15.48,9.31,13.89,8,12,8 c-2.21,0-4,1.79-4,4c0,1.89,1.31,3.48,3.08,3.89L11.71,17.99z M22,12c0,0.3-0.01,0.6-0.04,0.9l-1.97-0.59C20,12.21,20,12.1,20,12 c0-4.42-3.58-8-8-8s-8,3.58-8,8s3.58,8,8,8c0.1,0,0.21,0,0.31-0.01l0.59,1.97C12.6,21.99,12.3,22,12,22C6.48,22,2,17.52,2,12 C2,6.48,6.48,2,12,2S22,6.48,22,12z M18.23,16.26L22,15l-10-3l3,10l1.26-3.77l4.27,4.27l1.98-1.98L18.23,16.26z"/></svg> Do you want to allow web search?</h5>""",unsafe_allow_html=True)
allow_web_search=st.checkbox(label="Allow Search")
st.markdown("""<h5><svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24px" viewBox="0 0 24 24" width="24px" fill="#1f1f1f"><g><rect fill="none" height="24" width="24"/></g><g><g><path d="M21,12.22C21,6.73,16.74,3,12,3c-4.69,0-9,3.65-9,9.28C2.4,12.62,2,13.26,2,14v2c0,1.1,0.9,2,2,2h1v-6.1 c0-3.87,3.13-7,7-7s7,3.13,7,7V19h-8v2h8c1.1,0,2-0.9,2-2v-1.22c0.59-0.31,1-0.92,1-1.64v-2.3C22,13.14,21.59,12.53,21,12.22z"/><circle cx="9" cy="13" r="1"/><circle cx="15" cy="13" r="1"/><path d="M18,11.03C17.52,8.18,15.04,6,12.05,6c-3.03,0-6.29,2.51-6.03,6.45c2.47-1.01,4.33-3.21,4.86-5.89 C12.19,9.19,14.88,11,18,11.03z"/></g></g></svg> How can I assist you today?</h5>""",unsafe_allow_html=True)
user_query=st.text_area(label="Define your query:",placeholder="Describe your question, issue or task...",label_visibility="collapsed")
API_URL="http://127.0.0.1:5000/chat"
st.markdown("""<style>div.stButton > button{
    background-color: #667eea;
    color: white;
    padding: 10px 24px;
    border-radius: 8px;
    border: none;
    font-size: 16px;}
    div.stButton > button:hover {
    background-color: #642b73;
}</style>""",unsafe_allow_html=True)

if st.button("Ask Agent"):
    if user_query.strip():
        import requests
        payload={
            "model_name":selected_model,
            "model_provider":provider,
            "message":[user_query],
            "system_prompt":system_prompt,
            "allow_search":allow_web_search,

        }
        response=requests.post(API_URL,json=payload)
        if response.status_code == 200:
            response_data=response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response**"
                            f" {response_data}")

st.caption("This Agent can make mistakes")
