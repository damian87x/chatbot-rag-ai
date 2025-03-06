#!/bin/bash

echo "Setting up RAG Chatbot with NHS App Knowledge Base"

if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed. Please install pip for Python3."
    exit 1
fi

echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing required packages..."
pip3 install -r requirements.txt

echo "Checking for Ollama..."
if ! command -v ollama &> /dev/null; then
    echo "Ollama is not installed. Please install Ollama from https://ollama.com/"
    echo "After installing, run: ollama pull deepseek-r1:1.5b nomic-embed-text:latest"
else
    echo "Ollama found. Pulling required models..."
    ollama pull deepseek-r1:1.5b
    ollama pull nomic-embed-text:latest
fi

echo "Setup complete!"
echo "To run the app: python3 app.py"
