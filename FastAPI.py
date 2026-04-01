from pydantic import BaseModel
from typing import List
from main import get_response_from_agent
from fastapi import FastAPI
class RequiredData(BaseModel):
    model_name:str
    model_provider:str
    message:List[str]
    system_prompt:str
    allow_search:bool

ALLOWED_MODELS=['llama-3.1-8b-instant','llama-3.3-70b-versatile','meta-llama/llama-guard-4-12b','GPT-4o mini','llama3.1:8b','deepseek-r1:8b','llama3.2:3b','mistral:7b','qwen2.5:7b','gemini-2.0-flash','gemini-2.5-flash','gemini-2.5-pro']

app=FastAPI(title="AI Chatbot")
@app.post("/chat")
def chat_endpoint(request:RequiredData):
    if request.model_name not in ALLOWED_MODELS:
        return {"Error":"Invalid model name"}
    query=request.message
    llm_model=request.model_name
    provider=request.model_provider
    system_prompt=request.system_prompt
    allow_search=request.allow_search

    response=get_response_from_agent(query,llm_model,provider,system_prompt,allow_search)
    return response

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=5000)
