from langchain.tools import tool

@tool
def get_balance(user_id: str) -> str:
    """Returns the current account balance for the user."""
    return f"User {user_id} has a balance of $1,234.56"
