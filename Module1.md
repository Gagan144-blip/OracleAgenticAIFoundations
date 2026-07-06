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



