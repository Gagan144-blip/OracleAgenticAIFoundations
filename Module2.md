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

### LangChain under the hood :
1. User runs the Python Code

   <img width="712" height="312" alt="image" src="https://github.com/user-attachments/assets/5c8e807b-5fb6-4a44-b948-38502d076cb4" />
   
2. LangChain calls Model API
  LangChain calls the Model API with user message and availible tools:
   - Messages : Conversation so far.
   - Tools : the list of functions model is allowed to call.
   - langchain generated tool schemas from @tool functions.

    <img width="308" height="355" alt="image" src="https://github.com/user-attachments/assets/5af216b3-f8b5-4fb9-9f5e-b3ca383c0207" />

3. Model Returns a Tool Call #1
   The model sees the question and decides:
   - First, I need to multiply 15 by 8.
   - Then I need to divide that result by 3.
   - but the model cannot execute Python itself. So, it returns a Tool Call Request.
   - Conceptually, the first response might look like this:

     <img width="328" height="219" alt="image" src="https://github.com/user-attachments/assets/81b8705a-5446-47f1-b1fa-c6b31a3d673a" />

  - Content: " " : No text answer yet, model wants an action
  - tool_calls: Structured request for a function call
  - name: "multiply" : Which tool to invoke
  - Arguments : {"a" : 15, "b": 8} - parsed by your app

4. LangChain interprets the response

   LangChain reads the response and notices:
   - LLM did not give a final natural-language answer yet. instead, it asked for a tool call.
     * Is there a text answer?
       No -> content is empty
     * Are there tool_calls?
       yes -> tool call detected

    LanChain extracts three pieces of info:
    - Concpetually, LangChain does something like this:

      <img width="314" height="174" alt="image" src="https://github.com/user-attachments/assets/6ff67057-d793-4adf-bdfb-4eed70733078" />

### LangChain maps Tool name to real Python function reference
internally, LangChain maintains a registry of tools like this:
  
  <img width="664" height="313" alt="image" src="https://github.com/user-attachments/assets/15237510-be89-42c9-88c9-2aa558592bc2" />


5. LangChain executes the Python Function (Multiply)

     Real code runs on your machine - this is where reasoning becomes action.
   
   <img width="680" height="284" alt="image" src="https://github.com/user-attachments/assets/393136e1-92a6-4dba-900c-070794d246d0" />
   
6. LangChain sends the Tool #1 result back

   <img width="802" height="427" alt="image" src="https://github.com/user-attachments/assets/dabf7475-5356-459e-823e-7ce3b0f5c396" />
  
7. Model reasons and reqests Tools #2
The model sees result = 120 and knows it still needs to divide by 3.
LLM Reasoning:
"15 x 8 = 120 , now i need 120/3. Let me call divide"

<img width="692" height="262" alt="image" src="https://github.com/user-attachments/assets/b67d30f3-c796-48a8-8d2a-6896aa813e33" />

8. LangChain (interprets) and executes Python Function #2
   
9. LangCain Returns Tool #2 result

   <img width="759" height="373" alt="image" src="https://github.com/user-attachments/assets/8836cdde-0073-4a57-9227-fa426a9186fe" />

10.Model generates final answer

<img width="762" height="370" alt="image" src="https://github.com/user-attachments/assets/6fda80cd-1709-44fb-8e7a-07578e721336" />

11. Python prints the result:
    LangChain returns the result object,and your code prints the final answer.

### What LangChain hides from you
agent.invoke() is one line - but there is a LOT of machinery behind it.

<img width="773" height="312" alt="image" src="https://github.com/user-attachments/assets/232b72c4-524a-4e38-b6af-8781de00bb4d" />


<img width="485" height="434" alt="image" src="https://github.com/user-attachments/assets/b01c959d-3911-46f1-8ea2-20da290bd08d" />





    


   


