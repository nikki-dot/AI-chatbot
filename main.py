import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OLLAMA_API_KEY = os.environ.get("OLLAMA_API_KEY")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

llm_groq=ChatGroq(model="llama-3.1-8b-instant")
llm_openai=ChatOpenAI(model="gpt-oss-120b")
llm_ollama=ChatOllama(model="deepseek-v3.2:cloud")
llm_google=ChatGoogleGenerativeAI(model="gemini-3-pro-preview")

search_tools=TavilySearch(max_results=2)

from langchain.agents import create_agent
from langchain_core.messages import AIMessage
def get_response_from_agent(query,llm_model,provider,system_prompt,allow_search):
    if provider=="Groq":
        llm=ChatGroq(model=llm_model)
    elif provider=="OpenAI":
        llm=ChatOpenAI(model=llm_model)
    elif provider=="Ollama":
        llm=ChatOllama(model=llm_model)
    elif provider=="Google":
        llm=ChatGoogleGenerativeAI(model=llm_model)
    tavily_tool=[TavilySearch(max_results=2)] if allow_search else[]
    agent=create_agent(
        model=llm,
        tools=tavily_tool,
        system_prompt="Act as a helpful and smart AI Chatbot",
    )
    state = {'messages':query}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1]

