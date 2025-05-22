import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, Tool
from tools import get_balance

load_dotenv()
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

tools = [
    Tool(name="get_balance", func=get_balance, description="Get account balance by user ID.")
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    agent_kwargs={
        "handle_parsing_errors": True,
        "prefix": (
            "You are a finance agent that ONLY provides balance information based on the provided user ID. "
            "If the question is outside your scope, respond with 'I'm not able to help with that.'"
        )
    }
)


