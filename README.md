# 🤖 Oracle Agentic AI Foundations

This repository contains my learning journey, notes, code implementations, and hands-on projects completed during the **Oracle Agentic AI Foundations** course offered by **Oracle University**.

---

## 📜 Course Overview

The Oracle Agentic AI Foundations course introduces the concepts of AI Agents, Agentic AI, Model Context Protocol (MCP), LangChain, and modern AI application development through practical examples and projects.

---

## 🎯 Learning Objectives

Throughout this course, I learned how to:

- Understand AI Agents and Agentic AI
- Build AI agents using Python
- Work with LLMs using APIs
- Implement Tool Calling & Function Calling
- Build LangChain Agents
- Understand the Model Context Protocol (MCP)
- Build custom MCP Servers
- Connect LangChain Agents with MCP Servers
- Perform multi-step reasoning using AI agents
- Build reusable AI tools
- Document AI projects professionally

---

# 📚 Course Modules

## Module 1 – Introduction to Agentic AI

Topics Covered

- What is Artificial Intelligence?
- What are Large Language Models (LLMs)?
- What is an AI Agent?
- Components of AI Agents
- Agentic AI
- AI Agent Architecture
- AI Agent Workflow

---

## Module 2 – Building AI Agents

Topics Covered

- Python Environment Setup
- Working with APIs
- OpenAI SDK
- Groq API (Alternative)
- Responses API
- Chat Completions
- Multi-turn Conversations
- AI Agent SDK Basics

---

## Module 3 – LangChain

Topics Covered

- LangChain Basics
- Models
- Prompts
- Messages
- Tools
- Tool Calling
- Function Calling
- Creating LangChain Agents
- Agent Execution Flow

---

## Module 4 – Model Context Protocol (MCP)

Topics Covered

- Introduction to MCP
- MCP Architecture
- MCP Server
- MCP Client
- Tool Discovery
- JSON-RPC Communication
- Stdio Transport
- Remote MCP Servers
- Building Custom MCP Tools
- LangChain + MCP Integration

---

## 💻 Hands-on Projects

### 1️⃣ AI Agent using LangChain

Features

- Tool Calling
- Mathematical Operations
- Multi-step Reasoning
- Interactive Agent

---

### 2️⃣ MCP Math Server

Implemented reusable MCP tools:

- ➕ Add
- ✖ Multiply
- ➗ Divide
- √ Square Root

---

### 3️⃣ LangChain Agent with MCP

Features

- Automatic Tool Discovery
- MCP Client
- Dynamic Tool Loading
- Sequential Tool Execution
- Multi-step Reasoning

---

# 📂 Repository Structure

```text
OracleAgenticAIFoundations/
│
├── Module1.md
├── Module2.md
├── Module3.md
├── Module4.md
│
├── AI-Agent/
│   ├── first_agent.py
│   ├── first_agent_with_mcp.py
│   ├── mcp_math_server.py
│   ├── requirements.txt
│   └── README.md
│
├── Images/
│
├── Certificate/
│
└── README.md
```

---

# 🛠️ Technologies Used

- Python
- LangChain
- MCP (Model Context Protocol)
- OpenAI SDK
- Groq API
- VS Code
- Git & GitHub

---

# 🚀 How to Run

## Clone Repository

```bash
git clone https://github.com/Gagan144-blip/OracleAgenticAIFoundations.git
cd OracleAgenticAIFoundations
```

## Create Virtual Environment

```bash
python -m venv .venv
```

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

or

```env
OPENAI_API_KEY=your_openai_api_key
```

## Run LangChain Agent

```bash
python first_agent.py
```

## Run MCP Agent

```bash
python first_agent_with_mcp.py
```

---

# 📖 Key Takeaways

- Learned the fundamentals of Agentic AI
- Built AI Agents from scratch
- Explored LangChain Agent architecture
- Understood Tool Calling and Function Calling
- Built reusable MCP Servers
- Connected LangChain with MCP
- Implemented multi-step reasoning workflows

---

# 📜 Certificate

Successfully completed the **Oracle Agentic AI Foundations** course by Oracle University.

---

⭐ I Hope you found this repository helpful!
