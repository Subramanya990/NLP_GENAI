🔎 **LangChain: Chat with Web Search**:
This project is a Streamlit web application that enables users to interact with a conversational AI chatbot, which can perform web searches using Wikipedia, Arxiv and DuckDuckGo. The application leverages LangChain, a powerful framework for developing language model-based applications and Groq for LLM-based responses. Users can ask the chatbot questions and it will search the web to provide informative answers.

🚀 **Features**:
- Web search capabilities: The chatbot uses multiple tools to search and retrieve information from Wikipedia, Arxiv, and DuckDuckGo.

- Groq API Integration: The application uses Groq API for generating language model-based responses, powered by Llama3-8b-8192.

- Interactive Chat Interface: Developed using Streamlit, providing a seamless user interface for interaction.

- Real-time answers: The chatbot responds to user queries dynamically, combining retrieved web data and AI responses.

- Modular design: The system is built using LangChain’s agent-based architecture for flexibility in adding more tools or capabilities.

  📝 **Dependencies**:
-streamlit: For the UI.

-langchain: For integrating language models and tools.

-langchain_groq: For integration with the Groq API.

-wikipedia-api: For querying Wikipedia data.

-duckduckgo_search: For querying DuckDuckGo search results.

-python-dotenv: For loading environment variables.

🛠️ **Installation & Setup**:

1️⃣ Clone the Repository

2️⃣ Install Dependencies --- pip install -r requirements.txt

3️⃣ Run the Application --- streamlit run Search_engineTA.py
