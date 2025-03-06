# Chatbot RAG AI

A RAG (Retrieval-Augmented Generation) AI chatbot that uses the praisonaiagents library and Ollama models to provide knowledge-based responses.

## Project Structure

```
./
├── Makefile                # Build instructions and commands
├── README.md              # Project documentation
├── docker-compose.yml     # Docker configuration
├── main.py                # Main entry point for the application
├── requirements.txt       # Python dependencies
├── scripts/               # Shell scripts for setup and management
│   ├── init-db.sh         # Database initialization script
│   ├── setup.sh           # Setup script
│   └── start-local.sh     # Script to start the application locally
├── src/                   # Source code directory
│   ├── api/               # API functionality
│   │   └── knowledge_agent.py # Main agent API
│   ├── data/              # Data storage
│   │   └── knowledge/     # Knowledge files
│   │       └── kw.txt     # Sample knowledge text file
│   ├── ui/                # User interfaces
│   │   └── streamlit_app.py # Streamlit UI
│   └── utils/             # Utility functions
└── venv/                  # Virtual environment (gitignored)
```

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/chatbot-rag-ai.git
   cd chatbot-rag-ai
   ```

2. Run the setup:
   ```
   make setup install
   ```

3. Run the application:
   ```
   make run  # for CLI mode
   make run-ui  # for Streamlit UI
   ```

## Requirements

- Python 3.8+
- Ollama
- Docker (optional, for containerized deployment)

## Environment Variables

The application can be configured using the following environment variables (see .env file or set them directly):

- `VECTOR_STORE_PROVIDER`: Vector store provider (default: chroma)
- `COLLECTION_NAME`: Collection name (default: custom_knowledge)
- `LLM_PROVIDER`: LLM provider (default: ollama)
- `LLM_MODEL`: LLM model (default: deepseek-r1:1.5b)
- `OLLAMA_BASE_URL`: Ollama API URL (default: http://localhost:11434)

## License

[Your License]
