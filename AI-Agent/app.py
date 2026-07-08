# STEP 1: Initialize te Model
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY"),
)

# STEP 2: Define Your Tools

# Each tool needs: a name, a clear docstring, and type hints. LLM reads these to decide WHEN and HOW to use each tool

from langchain_core.tools import tool
import math

@tool   
def add(a: float, b: float) -> float:
    """Add two numbers together. USe for addition operations."""
    return a + b

@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together. Use for multiplication operations."""
    return a * b

@tool
def divide(a: float, b: float) -> float:
    """Divide one number by another. Use for division operations."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@tool
def subtract(a: float, b: float) -> float:
    """Subtract one number from another. Use for subtraction operations."""
    return a - b

@tool
def square_root(x: float) -> float:
    """Return the square root of a number."""
    return math.sqrt(x)

tools = [add, multiply, divide, subtract, square_root] 


#  STEP 3 : Create An Agent 
# create_agent builds a full ReAct loop:
# REason + Act (call tool) -> Observe -> Repeat



from langchain.agents import create_agent

agent  = create_agent(
    model=model,
    tools=tools,
)

# STEP 4: Run the Agent

def run_agent(question: str):
    print(f"User: {question}")
    print("-" * 50)

    result = agent.invoke({
    "messages": [
        ("system", "Reply in plain text only. Do not use Markdown or LaTeX."),
        ("user", question)
    ]
})

    final_message = result["messages"][-1]

    print("\nAgent:", final_message.content)
    print("-" * 50) 

user_ques = input("Enter your query: ")

run_agent(user_ques)
