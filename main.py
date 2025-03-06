#!/usr/bin/env python
"""
Main entry point for the chatbot RAG AI application.

This script serves as the main entry point for running the application.
It provides options to run either the API or UI version of the app.
"""
import sys
import os
from dotenv import load_dotenv

# Load environment variables
try:
    load_dotenv()
except ImportError:
    print("python-dotenv not installed. Using environment variables as is.")

def main():
    """Main function that parses arguments and runs the appropriate app."""
    if len(sys.argv) > 1 and sys.argv[1] == "--ui":
        # Run the Streamlit UI
        import streamlit.web.cli as stcli
        sys.argv = ["streamlit", "run", os.path.join("src", "ui", "streamlit_app.py")]
        sys.exit(stcli.main())
    else:
        # Run the API version by default
        from src.api.knowledge_agent import agent
        
        # Default query if none provided
        query = sys.argv[1] if len(sys.argv) > 1 else "Who can use the NHS App?"
        response = agent.start(query)
        print(f"Query: {query}\nResponse: {response}")

if __name__ == "__main__":
    main()
