# Oracle Agentic AI Foundations

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


## 📖 Module 1 – Introduction to AI Agents

### Topics Covered

- Introduction to AI Agents
- Agentic AI
- Components of AI Agents
- Agent Architecture
- AI Agent Workflow
- Chain of Thought (CoT)
- ReAct Framework
- AI Safety & Guardrails

### Hands-on

- Built First AI Agent
- Explored AI Agent Workflow

---

## 📖 Module 2 – LangChain for AI Agents

### Topics Covered

- Introduction to LangChain
- LangChain Expression Language (LCEL)
- Chat Models
- Messages
- Prompts
- Tool Calling
- Function Calling
- Agent Execution
- Understanding `agent.invoke()`

### Hands-on

- Built LangChain AI Agent
- Created Custom Python Tools
- Multi-step Tool Calling

---

## 📖 Module 3 – Introduction to Model Context Protocol (MCP)

### Topics Covered

- What is MCP?
- MCP Architecture
- MCP Server
- MCP Client
- JSON-RPC
- stdio Transport
- HTTP Transport
- Tool Discovery
- Local vs Remote MCP Servers

### Hands-on

- Built Custom MCP Math Server
- Connected LangChain with MCP
- Dynamic Tool Discovery

---

## 📖 Module 4 – OpenAI Responses API & Agents SDK

### Topics Covered

- Responses API
- Chat Completions
- Multi-turn Conversations
- Tools
- Function Calling
- AI Agents SDK
- Runner
- Multi-Agent Systems
- Agent Handoffs
- Guardrails
- Tracing

### Hands-on

- Responses API Examples
- Multi-turn Chat
- AI Agents SDK
- Customer Support Multi-Agent System

---

## 📖 Module 5 – Agentic AI for Enterprises

### Topics Covered

- OCI Enterprise AI Platform
- Enterprise AI Agents
- Hosted Models
- Knowledge Bases
- Sessions & Memory
- Logging
- Sandboxed Tools
- Enterprise Deployment

### Hands-on

- Explored OCI Enterprise AI Platform
- Enterprise AI Agent Concepts

---

## 📖 Module 6 – Agentic AI with Oracle AI Database

### Topics Covered

- Oracle AI Database
- Oracle AI Vector Search
- Vector Embeddings
- Private Agent Factory
- Select AI Agent
- Autonomous AI Database MCP Server
- Enterprise Data + AI Agents

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
├── AI-Agent/
│   ├── first_agent.py
│   ├── first_agent_with_mcp.py
│   ├── mcp_math_server.py
│   ├── requirements.txt
│   └── README.md
├── Module1.md
├── Module2.md
├── Module3.md
├── Module4.md
├── Module5.md
├── Module6.md
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
