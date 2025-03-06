from praisonaiagents import Agent
import os
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.config import get_default_config, get_knowledge_path

config = get_default_config()

knowledge_path = get_knowledge_path("kw.txt")

agent = Agent(
    name="Knowledge Agent",
    instructions="You answer questions based on the provided knowledge.",
    knowledge=[knowledge_path], #indexing
    knowledge_config=config,
    user_id="user1",
    llm=config["llm"],
)

if __name__ == "__main__":
    # Simple start with no additional parameters
    response = agent.start("Who can use the NHS App?") #Retrieval
    print(response)
