import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, Tool
from tools import get_balance

load_dotenv()
llm = ChatOpenAI(model="gpt-4", temperature=0)

tools = [
    Tool(name="get_balance", func=get_balance, description="Get account balance by user ID.")
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

result = agent.run("What is my balance? My user ID is 1234.")
print(result)
