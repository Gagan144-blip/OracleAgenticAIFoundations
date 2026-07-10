# ============================================================
# LangChain for AI Agents – Companion Code
# ============================================================

# This program demonstrates:
# - How an AI Agent uses the ReAct pattern (Reason → Act → Observe)
# - How to build an agent using LangChain's create_agent

# Prerequisites:
# pip install langchain langchain-openai langgraph python-dotenv

# Setup:
# Create a .env file with:
# OPENAI_API_KEY=your-api-key-here

# ============================================================
# STEP 0: Load Environment Variables
# ============================================================

# We store sensitive information like API keys in a .env file.
# This keeps secrets out of the source code (best practice).

import os 
from dotenv import load_dotenv

load_dotenv() #Loads variables like GROQ_API_KEY into environment

# ============================================================
# STEP 1: Initialize the Model (The "Brain")
# ============================================================

# The LLM (Large Language Model) will:
# - Understand the user's question
# - Decide which tool to use (if needed)
# - Generate the final response

from langchain_groq import ChatGroq

model = ChatGroq(
    model="openai/gpt-oss-20b",
)

# ============================================================
# STEP 2: Define Your Tools ("the hands")
# ============================================================

# Tools allow agent to DO things instead of just responding.
# Each tool must have:
# 1. A clear name      
# 2. A descriptive docstring (VERY important )
# 3. Type hints (so the LLM knows expected inputs)

from langchain_core.tools import tool
import math 

@tool
def add(a: float, b: float) -> float:
    """Add two numbers together. Use for addition operations."""
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
    """Return the square root of a number.
       Includes error handling for negtive inputs."""
    if x < 0:
        raise ValueError("Input must be a non-negative number.")    
    return math.sqrt(x)   


#Combine all tools into a list

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
# This function sends a question to the agent and prints:
# - The Final Answer
# - (optional) the internal execution trace 


def run_agent(question: str):
    """Run the agent a clean , beginner-friendly execution trace."""

    print(f"\nUser: {question}")
    print("-" * 60)

    result = agent.invoke({
    "messages": [
        ("system", "Reply in plain text only. Do not use Markdown or LaTeX."),
        ("user", question)
    ]
})

    print("Clean Agent Execution Trace")
    print("_" * 60)

    step = 1

    for msg in result["messages"]:

        # 1. Human Message = original user question
        if msg.type == "human":
            print(f"{step}. User asked:")
            print(f"   {msg.content}")
            step += 1

        # 2. AI Message with tool_calls = agent decided to use a tool
        elif msg.type == "ai" and getattr(msg, "tool_calls", None):
            for tool_call in msg.tool_calls:
                tool_name = tool_call["name"]
                tool_args = tool_call["args"]

                print(f"{step}. Agent decision:")
                print(f"I need to use the tool: {tool_name}")
                print(f"   Tool inputs: {tool_args}")
                step += 1
    
        # 3. Tool message = result returned by the tool
        elif msg.type == "tool":
            print(f"{step}. Tool observation:")
            print(f"  Tool returned: {msg.content}")
            step += 1


        #4. Final AI Message = final answer to user
        elif msg.type == "ai" and msg.content:
            print(f"{step}. Final Answer:")
            print(f"  {msg.content}")
            step += 1

print("=" * 60)


#-------------------------------------------------------------
# TEST CASES - Watch the agent in action!
#-------------------------------------------------------------

User_Query = input("Enter your query: ")
run_agent(User_Query)

# #Final Message
print(" Agent Demo completed!")

#1. Simple case -> single tool call
#Agent should directly use "add"
# run_agent("What is 2 + 2?")

# #2. Medium complexity -> multiple tool calls
# #Agent should use "multiply" then "add"
# run_agent("What is 3 multiplied by 4, then divided by 5?")

# #3. Complex case -> multiple tool calls + Planning Required

# #Agent must:
# # step 1: calculate area
# # step 2: calculate square root of area
# run_agent("What is the square root of the area of a rectangle with length 5 and width 10?")


# # # 4. Edge case -> invalid input     
# # #Agent should handle error gracefully
# # run_agent("What is the square root of -9?")

  