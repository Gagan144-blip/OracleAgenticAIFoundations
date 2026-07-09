### IntroDuction to AI agents
Concepts -> Components -> Patterns -> Code -> safety

Ai Agents?
- Thinks and decides next step Dynamically
- Precieve Environment and act upon that environment accroding to thier observation
AI agent (LLM - based) : LLM + Tools + Loop

LLM : Brain (Understands the Environment)
Tools : Acts like Hands
Loop: Acts like a nervous system

Properties: 
- Goal Directed: Always focus Towards their final Goal
- Autonomous : Decides what to to Next
- Tool Using : Interacts with APis, databases, code Execution, and Web search
- Iterative : Operates in a loop <br>
  * Observe -> Reason -> Act -> Observe Again
    
  ### LLM vs (LLM-Based) AI Agent
  <img width="1075" height="486" alt="Screenshot_20260703_184414" src="https://github.com/user-attachments/assets/2b009f94-5866-4c83-8d75-773a05fd2f7e" />

### An AI agent is nt a new kind of model - It's an architecture pattern that wraps an LLM in a reason-act-observe loop

### The Agent Execution loop:

   <img width="714" height="219" alt="image" src="https://github.com/user-attachments/assets/a97f9f6c-0365-45e5-8e53-150aa3dd1504" />
   
Termination Conditions:
  - Agent decodes it has the final answer
  - Maximum iteration count reached
  - Error or timout triggers fallback

 What can go wrong
   - Infinite loops(agent never decides it's done)
   - Hallucined tool calls(Calling tools that don't exist)
   - Cost explosion(too many LLM API calls)
### Example:
   The Agent Execution Loop:

   <img width="1051" height="529" alt="image" src="https://github.com/user-attachments/assets/64a7d3a6-1b67-408d-8217-b32f718b1bc3" />

po

### AI AGENT CORE COMPONENTS
- Three core components of Every Agent:
   <img width="733" height="316" alt="image" src="https://github.com/user-attachments/assets/03342633-b83e-43a9-b675-9c76b60c7faa" />
   
1: LLM - Agent's Brain
<img width="764" height="312" alt="image" src="https://github.com/user-attachments/assets/19e62ba9-ac80-4bcd-be85-a21f75530866" />

2: Tools- Agent's Hands
<img width="683" height="328" alt="image" src="https://github.com/user-attachments/assets/a8f2051f-599f-41d0-8294-92e63a63eb0b" />

3: Loop(Orchestration) - Agent's Nervous System
<img width="752" height="340" alt="image" src="https://github.com/user-attachments/assets/dc356645-e716-45b0-95a4-d53aa3c93030" />


### REASONING PATTERNS:

- Major Reasoning Frameworks:
  <img width="729" height="314" alt="image" src="https://github.com/user-attachments/assets/6f04e6b3-5315-4a38-a964-a9e3f1f9d491" />

## Chain of Thought (CoT): THINKING STEP BY STEP
<img width="736" height="308" alt="image" src="https://github.com/user-attachments/assets/82763f7a-050f-4f9b-806a-b30d2f4596a0" />


- CoT Limitations for Agents:
  * Uses only internal knowledge - cannot look things up.
  * if knowledge is wrong, reasoning is confidently wrong.
  * cannot self- correct against external reality.
  * Cannot take actions in the real world.

 - Why this matters for Agents:
   * CoT gives agents the ability to 'think'.
   * but thinking alone isn't enough - aggents also need to act.
   * ReAct pattern: CoT +Tools use in loop.
   * modern reasning models(o1, R1) do CoT internally (may not expose 'thinking' block).
  
  ### ReAct : Reasoning + acting in a loop
   
  <img width="749" height="263" alt="image" src="https://github.com/user-attachments/assets/36a511c5-0081-4bf5-80c7-18d5857a63dd" />


### Building Your First AI Agent:

- Agent Frameworks:

<img width="768" height="294" alt="image" src="https://github.com/user-attachments/assets/dedd1241-5a91-445a-973a-13e769cba5f2" />

## Steps to creating any AI agent: 

<img width="961" height="105" alt="image" src="https://github.com/user-attachments/assets/9954c52c-4f09-430b-b0ea-218fd90549f1" />

### Python Essentials You'll Need:

<img width="702" height="308" alt="image" src="https://github.com/user-attachments/assets/3208e21b-d855-4325-8a81-2c650e3c9b8c" />

### Anatomy of an Agent Tool:

<img width="756" height="325" alt="image" src="https://github.com/user-attachments/assets/56356329-e970-4339-90a0-476051408229" />

### Step 2: Build the Agent's toolbox:

<img width="572" height="328" alt="image" src="https://github.com/user-attachments/assets/e9353f62-b014-42b3-9601-61ee2ed48181" />

### Step 3: Agent's Secret: a reasoning loop:

<img width="511" height="334" alt="image" src="https://github.com/user-attachments/assets/ba103deb-d21e-496a-acca-f8c2f58b4850" />

### Example : Question: "What is 42 + 58?"

<img width="508" height="226" alt="image" src="https://github.com/user-attachments/assets/3db2b42d-eea1-45e2-b045-31f0aa4368f5" />

### Question : Rectangle Area + square root:

<img width="547" height="297" alt="image" src="https://github.com/user-attachments/assets/4088cada-386d-4c82-ab74-affe2a0f3667" />

### Real - world Agent Attacks: These are Already Happend:

<img width="768" height="310" alt="image" src="https://github.com/user-attachments/assets/04028f72-34f4-490e-89b5-c519c683669e" />
### AI agent Threat Model : What Can Go Wrong:
- Prompt Injection: Attckers ijacks AI agent vuia craf







