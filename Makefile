.PHONY: setup install reinstall run clean

all: setup install

reinstall: clean setup install

setup:
	python3 -m venv venv
	@echo "Virtual environment created in ./venv"

install: setup
	. venv/bin/activate && pip install -r requirements.txt
	@if command -v ollama >/dev/null 2>&1; then \
		echo "Pulling Ollama models..."; \
		ollama pull deepseek-r1:1.5b; \
		ollama pull nomic-embed-text:latest; \
	else \
		echo "Ollama not installed. Please install from https://ollama.com/"; \
	fi

run: install
	. venv/bin/activate && python main.py

run-ui: install
	. venv/bin/activate && python main.py --ui

clean:
	rm -rf venv
	rm -rf .praison
	rm -rf __pycache__
	rm -rf *.pyc
