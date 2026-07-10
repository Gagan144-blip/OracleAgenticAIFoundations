"""
========================================================
LangChain for AI Agents – Companion Code
========================================================

Lesson 1: Core Building Blocks
- Models, Prompts, Chains, Output Parsers, Memory, Tools

Demo order (matches the lessons):
    Lesson 1 - Models, Prompts, Chains, Memory
    Lesson 2 - Tools

Prerequisites:
    pip install langchain langchain-openai python-dotenv

Setup:
    Create a .env file with:
    OPENAI_API_KEY=sk-your-key-here

========================================================
"""

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import os
from pathlib import Path
from dotenv import load_dotenv

# Find the .env file sitting next to THIS script (not wherever we ran from).
# Path(__file__) = this file; .parent = its folder. This makes the key load
# correctly no matter which directory you launch python from.

script_dir = Path(__file__).resolve().parent
env_path = script_dir / ".env"

#print("Current working directory:", os.getcwd())
#print("Script directory:", script_dir)
#print("Using .env from:", env_path)

load_dotenv(dotenv_path=env_path)

# Quick sanity check that the key actually loaded before we call the model.
print("GROQ_API_KEY found:", bool(os.getenv("GROQ_API_KEY")))

# ------------------------------------------------------------
# 1. MODELS — The Reasoning Engine
# ------------------------------------------------------------

# The "model" is the LLM itself — the part that actually thinks.
# init_chat_model gives ONE interface to every provider: to switch from
# OpenAI to Anthropic or Google, you change only the string below.

from langchain_groq import ChatGroq

model = ChatGroq(
    model="openai/gpt-oss-20b"
)

# The simplest possible use: send text in, get an answer back.
# .invoke() is the universal "run it" method across LangChain.

response = model.invoke("What is the capital of France?")
print("Model response:", response.content)  # .content = just the text of the reply 
print()


# ------------------------------------------------------------
# 2. PROMPT TEMPLATES — Steering the Model
# ------------------------------------------------------------

# A prompt template is a reusable sentence with blanks ({placeholders})
# you fill in later — write the wording once, reuse it many times.

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

# Prompt Template = a single plain-text string with blanks.
simple_template = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} to a complete beginner in 2-3 sentences."
)

# .format() fills the black and return the finished text.

formatted = simple_template.format(topic="AI Agents")
print("=== Formatted Prompt ===")
print(formatted)
print()

# ChatPromptTemplate = built from ROLES (system / human), which is how chat
# models expect their input. "system" sets behavior, "human" is the user turn.

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that explains things in simple terms."),
    ("human", "Explain {topic} with one simple example.")
])

messages = chat_template.format_messages(topic="AI Agents")

print("=== chat Messsages ===")
for msg in messages:
    print(f"{msg.type.upper()}: {msg.content[:80]}...")
print()


#-------------------------------------------------
# 3. CHAINS - Connecting the pieces with LCEL
#-------------------------------------------------

#The pip | glues components inton a pipeline. Each step's output flows
#into the next , left to right: prompt -> model -> output parser -> parser.

from langchain_core.output_parsers import StrOutputParser

# prompt fills the blanks → model answers → parser pulls out clean text.
# StrOutputParser just extracts the plain string from the model's reply
# object, so you don't have to write .content yourself every time.

chain = chat_template | model | StrOutputParser()

# Run the whole pipeline with a single .invoke().
result = chain.invoke({"topic": "for loops"})

print("=== Chain Output ===")
print(result)
print()

#------------------------------------------------------------
# 4. MEMORY - Remembering the Conversation
#------------------------------------------------------------

# Models are stateless — they forget everything between calls.
# "Memory" is simply storing past messages and feeding them back in.
# (Modern LangChain uses ChatMessageHistory; the old
# ConversationBufferMemory is deprecated and out of the core package.)

from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage

# A simple in-memory store that holds the conversation.
memory = InMemoryChatMessageHistory()

# Hand-build a short conversation so we have something to "remember".
memory.add_message(HumanMessage(content="My name is Gagan and I'm learning LangChain"))
memory.add_message(AIMessage(content="Nice to meet you, Gagan! LangChain is a great choice."))
memory.add_message(HumanMessage(content="What tools should I learn first?"))
memory.add_message(AIMessage(content="Start with PromptTemplates and simple chains, then move to tools and agents."))

print("=== Memory Contents ===")
for msg in memory.messages:
    print(f"{msg.type.upper()}: {msg.content}")
print()


# The "placeholder" slot is where the stored messages get injected into the
# prompt, so the model can SEE the earlier conversation.
chat_with_memory = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful tutor. Use the conversation history to personalize your responses."),
    ("placeholder", "{history}"),   # past messages get dropped in here
    ("human", "{question}"),
])

chain_with_memory = chat_with_memory | model | StrOutputParser()

# We pass the stored history in alongside the new question.
# Watch the model correctly recall the name "Gagan" — that's "memory".
result = chain_with_memory.invoke({
    "history": memory.messages,
    "question": "What was my name again?"
})

print("=== Memory-Aware Response ===")
print(result)
print()

