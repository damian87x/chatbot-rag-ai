from praisonaiagents import Agent
import os
from dotenv import load_dotenv

try:
    load_dotenv()
except ImportError:
    print("python-dotenv not installed. Using environment variables as is.")

config = {
    "vector_store": {
        "provider": os.getenv("VECTOR_STORE_PROVIDER", "chroma"),
        "config": {
            "collection_name": os.getenv("COLLECTION_NAME", "custom_knowledge"),
            "path": os.getenv("VECTOR_STORE_PATH", ".praison"),
        }
    },
    "llm": {
        "provider": os.getenv("LLM_PROVIDER", "ollama"),
        "config": {
            "model": os.getenv("LLM_MODEL", "deepseek-r1:1.5b"),
            "temperature": int(os.getenv("LLM_TEMPERATURE", "0")),
            "max_tokens": int(os.getenv("LLM_MAX_TOKENS", "8000")),
            "ollama_base_url": os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        }
    },
    "embedder": {
        "provider": os.getenv("EMBEDDER_PROVIDER", "ollama"),
        "config": {
            "model": os.getenv("EMBEDDER_MODEL", "nomic-embed-text:latest"),
            "ollama_base_url": os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
            "embedding_dims": int(os.getenv("EMBEDDING_DIMS", "1536"))
        }
    }
}


agent = Agent(
    name="Knowledge Agent",
    instructions="You answer questions based on the provided knowledge.",
    knowledge=["kw.txt"],
    knowledge_config=config,
    user_id="user1",
    llm=config["llm"]
)

agent.start("Who can use the NHS App?")
