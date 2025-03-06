#!/usr/bin/env python
"""
Utility functions for configuration management.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Determine project root path
PROJECT_ROOT = Path(__file__).parent.parent.parent

def get_default_config():
    """
    Get the default configuration for the application.
    
    Returns:
        dict: Configuration dictionary
    """
    # Load environment variables
    try:
        load_dotenv()
    except ImportError:
        print("python-dotenv not installed. Using environment variables as is.")
        
    return {
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

def get_knowledge_path(filename):
    """
    Get the absolute path to a knowledge file.
    
    Args:
        filename (str): Filename to find in the knowledge directory
        
    Returns:
        str: Absolute path to the knowledge file
    """
    return os.path.join(PROJECT_ROOT, "src", "data", "knowledge", filename)
