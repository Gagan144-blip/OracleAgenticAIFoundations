### OpenAI Responses API and Agents SDK

### The OpenAI Agent Stack:
Agents SDK builds on top of the Responses APi, but you can also use the Responses API directl without the SDK.

<img width="475" height="334" alt="image" src="https://github.com/user-attachments/assets/16aed91a-b332-4f23-8478-c62505dc3c8d" />

### Choosing between Responses API and Agents SDK

<img width="500" height="360" alt="image" src="https://github.com/user-attachments/assets/79ee3075-9266-4fb8-a9b0-ee1653a8d16a" />

<img width="753" height="406" alt="image" src="https://github.com/user-attachments/assets/52416c2a-5531-4947-bddf-bb1af6221989" />

### OpenAI Responses API:

- The Responses APi : The core interface to interact with OpenAI models, Allows you to send input, recieve structures output, enable tool usage, and chain conversations across turns.
  
- Simpler Input: Pass a string or strucutred input - get output_text back.
- Conversation Chaining: You control when conversations are connected ( use previous_response_id to link turns)
- Tool Integration : Enable tools like wen search or code exectution.
- Model-Driven Tool Use: The model decides when to call tools.
- Efficient Execution: Desgined for improved performance and caching.

### Your first Responses API call:
  
  <img width="802" height="414" alt="image" src="https://github.com/user-attachments/assets/530e5db8-0ea6-4ef0-9b04-262e0e65d635" />

### Conversation Chaining with Responses API:

<img width="653" height="381" alt="image" src="https://github.com/user-attachments/assets/822d43ed-8ebc-4008-bb04-a1a7bac17a96" />

### Built-in Tools (Model Callable)
- Web Search : {"type" : "web_search"} : search the internet for current information
- File Search : { "type" : "file_search"} : Search through uploaded documents
- Code interpreter : { "type" : "code_interpreter" } : write and execute Python Code
- Computer Use : {"type" : "computer_use_preview"} : Control a computer interface ( experimental)
- Image Generation : {"type" : "imagge_generation"} : Generate images via  DALL-E.
  * just add tools=[{"type" : "web_search"}] to any Responses API call

<img width="628" height="355" alt="image" src="https://github.com/user-attachments/assets/a839d175-ba99-4a7a-951f-2e44a789ff61" />

### OpenAI Agents SDK:
- A python framework that hepls you define agents, manage tools usage, and build multi-agent systems.It is built on top of the Responses API.
  * Agent : LLM + intructions + tools.
  * Runner: Executes the agent loop.
  * Tools : Functions the agent can call.
  * HandOffs : Transfers control between agents.
  * Guardrails : Validate inputs and outputs for safety.
  * Tracing : Monitor what the agent did.

- Install:
  ```bash
  pip install openai-agents
  ```
### Your First Agent:

<img width="736" height="362" alt="image" src="https://github.com/user-attachments/assets/49f2ed93-32a4-4e60-aab0-cf78b8fe9c45" />
<img width="726" height="338" alt="image" src="https://github.com/user-attachments/assets/b600fd09-f1c7-4364-8926-b770c39be963" />


<img width="757" height="395" alt="image" src="https://github.com/user-attachments/assets/3925a1bc-b8b8-4ea1-bd8d-f455fdb32af0" />












