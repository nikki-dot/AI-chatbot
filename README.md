# 🤖 AI Chatbot with Multiple LLM Providers

An intelligent, agentic AI chatbot that supports multiple Large Language Model (LLM) providers including Groq, OpenAI, Ollama, and Google. The chatbot features web search capabilities and a user-friendly Streamlit interface.

## ✨ Features

- **Multiple LLM Providers**: Support for Groq, OpenAI, Ollama, and Google models
- **Web Search Integration**: Optional Tavily search for real-time information
- **Custom System Prompts**: Define your agent's behavior and personality
- **Chat History**: Maintain conversation context with persistent chat history
- **Responsive UI**: Clean, modern interface built with Streamlit
- **Error Handling**: Comprehensive error handling and timeout management
- **Async Processing**: Non-blocking API calls for better performance
- **Model Selection**: Choose from various models based on your needs

## 🚀 Supported Models

### Groq Models
- `llama-3.1-8b-instant`
- `llama-3.3-70b-versatile`
- `meta-llama/llama-guard-4-12b`

### OpenAI Models
- `GPT-4o mini`

### Ollama Models
- `llama3.2:3b` (fast)
- `qwen2.5:7b` (balanced)
- `mistral:7b` (balanced)
- `llama3.1:8b` (slower, higher quality)
- `deepseek-r1:8b` (slower, higher quality)

### Google Models
- `gemini-2.0-flash`
- `gemini-2.5-flash`
- `gemini-2.5-pro`

## 📋 Prerequisites

- Python 3.8 or higher
- API keys for the services you plan to use
- For Ollama: [Ollama installed locally](https://ollama.ai/)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nikki-dot/ai-chatbot.git
   cd ai-chatbot
