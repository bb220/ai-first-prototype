from langchain.agents import initialize_agent, AgentType, Tool
from langchain.chat_models import ChatOpenAI

# Tool definition
def get_balance(user_id: str) -> str:
    return f"User {user_id} has $1,234.56"

tools = [
    Tool(
        name="get_balance",
        func=get_balance,
        description="Get a user's balance by ID."
    )
]

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

def run_agent(message: str) -> str:
    return agent.run(message)
