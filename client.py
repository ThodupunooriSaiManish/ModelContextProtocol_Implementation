import asyncio
import os
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
async def main():
    if "GOOGLE_API_KEY" not in os.environ:
        print("Error: Please set your GOOGLE_API_KEY environment variable.")
        return

    print("🔄 Initializing multi-server connections...")
    
    client = MultiServerMCPClient({
        "math_service": {
            "transport": "stdio",
            "command": "python",
            "args": ["/absolute/path/to/mathserver.py"],
        },
        "weather_service": {
            "transport": "http",
            "url": "http://localhost:8000/mcp",
        }
    })

    print("🔍 Collecting tools from active servers...")
    tools = await client.get_tools()
    print(f"✅ Loaded tools successfully: {[t.name for t in tools]}")

    llm = ChatOllama(model="llama3", temperature=0.0)
    agent = create_react_agent(llm, tools)

    print("\n💬 Sending Query 1 to Agent...")
    prompt_1 = "Calculate (15 + 25) * 4"
    print(f"User: {prompt_1}")
    response_1 = await agent.ainvoke({"messages": [{"role": "user", "content": prompt_1}]})
    print(f"Agent: {response_1['messages'][-1].content}\n")

    print("💬 Sending Query 2 to Agent...")
    prompt_2 = "What is the weather like in New York right now?"
    print(f"User: {prompt_2}")
    response_2 = await agent.ainvoke({"messages": [{"role": "user", "content": prompt_2}]})
    print(f"Agent: {response_2['messages'][-1].content}\n")

if __name__ == "__main__":
    asyncio.run(main())