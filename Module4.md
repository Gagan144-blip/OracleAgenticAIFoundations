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
  
  
