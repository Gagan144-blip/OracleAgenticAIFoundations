### Introduction to MCP
### What is context Model Protocol:
AN open standers that provides a universal interface for AI applications to conenct with external tools, data sources, and systems -- securely and consistently.

<img width="768" height="290" alt="image" src="https://github.com/user-attachments/assets/d11cdc1c-530c-4028-87c8-5f89226bc007" />

### The problem MCP Solves:
N: no of applications 
M: no. of tools

<img width="769" height="281" alt="image" src="https://github.com/user-attachments/assets/38990f40-0b8a-4b95-a33a-206f9038ee77" />

### MCP Architecture:
<img width="686" height="278" alt="image" src="https://github.com/user-attachments/assets/53a28da9-2cf0-43eb-872e-fb1006528531" />

### MCP Core Components:
- Core Primitives:
 <img width="725" height="352" alt="image" src="https://github.com/user-attachments/assets/82dd6e31-5125-44fb-ac12-54f5f3b9b865" />

### The MCP Connection Lifecycle:

<img width="765" height="183" alt="image" src="https://github.com/user-attachments/assets/c5740305-135f-42fd-b2dd-d599e5129480" />

- MCP uses JSON_RPC 2.0
  * JSON_RPC messages include:
  * jsonprc ("always 2.0")
  * id(used to match requests and responses, when applicable).
  * One of: method (request), result(success), or error(failure).
  * in most cases, frameworks like FastMCP and LangChain handle this for you - but understanding the structure helps with debugging.
    
  <img width="556" height="217" alt="image" src="https://github.com/user-attachments/assets/5cd203ad-b607-4b01-b00c-5e74a9265166" />

### MCP Method #1: toos/list


    
