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

### MCP Method #1: tools/list:
- Typically called when the client connects to dicover availible tools.
- The server returns every tool it offers.
- Agent discovers tools without you hardcoding them.

  <img width="591" height="281" alt="image" src="https://github.com/user-attachments/assets/fb664090-6f15-4546-b22d-88605500b893" />

  ### MCP Method #2: tools/call
  - called each time the LLM decides it needs a tool.
  - includes the tool name and arguments.
  - The LLM decides to call this tool baed on the user's request and availible tool discriptions.
 
    <img width="564" height="246" alt="image" src="https://github.com/user-attachments/assets/404feacf-3c84-4375-8552-c08f6a0fe084" />

### MCP Transport Mechanisms:

<img width="682" height="295" alt="image" src="https://github.com/user-attachments/assets/efe01f85-51e3-412c-8a90-951057403de8" />

### Add MCP Server to your first Agent:
- Before MCP: First Agent
- 
everything lives in one file - tighty coupled.

<img width="528" height="288" alt="image" src="https://github.com/user-attachments/assets/ac76c83c-e520-44af-81a3-2ab3c8770b4a" />

- After MCP: Two separate files (Client,Server)
  
  Tools live on a server - any AI app can discover and use them.
  
  <img width="627" height="267" alt="image" src="https://github.com/user-attachments/assets/f6d0b5fa-88b5-4d8f-b8d4-ba478a018a9b" />

  - After MCP : Agent Architecture:

    <img width="616" height="355" alt="image" src="https://github.com/user-attachments/assets/6a3611aa-be5a-450a-8904-824ae321e350" />

### WHat Changed(Tool Execution):

 <img width="600" height="313" alt="image" src="https://github.com/user-attachments/assets/7292c5d0-2546-4075-b960-ae2a425d7e19" />

### WHat Your Agebt App NO LOnger need to do:

MCP shifts responsibilities from your application to the MCP server.

<img width="654" height="277" alt="image" src="https://github.com/user-attachments/assets/80760e53-b346-483c-81f4-5f55cdc07ae8" />

### From the LLM's Point of View:

<img width="588" height="333" alt="image" src="https://github.com/user-attachments/assets/de61aee3-d051-43a6-a5c6-4ac562b7a55c" />

### Why MCP makes your Agent Better:

<img width="518" height="366" alt="image" src="https://github.com/user-attachments/assets/2ca7eca5-5a8a-4ff3-a98f-fe06981d1ecc" />

### WHen Does MCP actually HElp:
For our math Example(multiply, divide), MCP is overkill.A local Python functon is simpler and faster.

<img width="669" height="234" alt="image" src="https://github.com/user-attachments/assets/aa8dcd7c-3cad-4ec3-b27c-e2fbb20e4caa" />


### Real World MCP example:
-  From Sandbox to Real World MCP

  <img width="749" height="312" alt="image" src="https://github.com/user-attachments/assets/f66f257f-95b8-4d0a-bd83-8d7e8f6166dd" />

- Different Bounderies - Math vs Oracle Usage MCP server

<img width="650" height="290" alt="image" src="https://github.com/user-attachments/assets/1f7085bb-0eac-46bc-89dd-12ab2406fa21" />

- OCI Usage MCP Server Details:

  <img width="702" height="162" alt="image" src="https://github.com/user-attachments/assets/896dffe0-de41-4b4f-8ca2-512d5375bebc" />

<img width="741" height="140" alt="image" src="https://github.com/user-attachments/assets/51aa59a9-a418-4b19-91b8-290f3416a18f" />


### Real world MCP Server

<img width="345" height="343" alt="image" src="https://github.com/user-attachments/assets/2257d1e2-f324-4714-ae13-abb87235adaa" />






  

  

  



  



    
