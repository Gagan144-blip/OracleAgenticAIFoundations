### Langchain For AI Agents:

### Introduction to LangChain:
An open- source framework that connects Large Language Models woth the Outside world - tools, data and APIs.

<img width="725" height="208" alt="image" src="https://github.com/user-attachments/assets/4a59b649-dabb-4f38-836c-85c638a313d2" />


### LangChain Ecosystem:
Interconnected components that work together.

<img width="744" height="215" alt="image" src="https://github.com/user-attachments/assets/2d33603e-272b-4940-a556-157141d68f43" />

### Models = Reasoning Engine:
LangChain Provides a unified interface - but model capabilities may still differ across providers.

 ## Install Required Packages

```bash
pip install langchain-openai langchain-anthropic
```

---

## Import

```python
from langchain.chat_models import init_chat_model
```

---

## Initialize OpenAI Model

```python
model = init_chat_model("openai:gpt-4o")
```

---

## Switch to Anthropic Model

```python
model = init_chat_model("anthropic:claude-3.5")
```

<img width="295" height="308" alt="image" src="https://github.com/user-attachments/assets/dbb9ed42-a763-4daf-9291-1f692cdce3b2" />

### Prompt Template - steering The Model
prompts are usable templates with placeholders. They let you build dyanmic instructions for LLM.

<img width="687" height="246" alt="image" src="https://github.com/user-attachments/assets/9cf7dac1-9cc0-487b-8e05-025aefd811d7" />

### Chains - Connecting the pieces:
The "Chain" in LangChain. Pipe data through a sequence of steps.

<img width="737" height="280" alt="image" src="https://github.com/user-attachments/assets/81ef9eb6-9cb9-48d9-aea9-2ad75602a3a0" />

### Build your first Agent using LangChain:
### what makes An AI Agent?

<img width="722" height="252" alt="image" src="https://github.com/user-attachments/assets/179f2092-64f9-43ec-b188-cca09daf5f44" />

### Tools -Giving LLMs Superpowers:
Tools are functions that an LLM can call during its reasoning process. They Extend the model Beyond text generattion into real - world actions.
- Web search : Look up real-time information online
- Database Query : Read/Write data in SQL or NoSQL
- Code Execution: Run python code for calculaions
- Custom APIs: call any external service or endpoint

### 








