from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_groq import ChatGroq
import os
import asyncio
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()
async def main():
    client = MultiServerMCPClient(
        {
            "math" : {
                "command" : "python",
                "args" : ["mathserver.py"],
                "transport" : "stdio"
            },
            "weather" : {
                "url": "http://localhost:8000/mcp",
                "transport" : "streamable-http"
            }
        }
    )
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    tools = await client.get_tools()
    model=ChatGroq(model="openai/gpt-oss-120b")
    agent = create_react_agent(model=model, tools=tools)

    math_response = await agent.ainvoke({"messages":[{"role": "user", "content": "What is 2+3?"}]})
    print("Math Response:", math_response['messages'][-1].content)

    weather_response = await agent.ainvoke({"messages":[{"role": "user", "content": "What is the weather in California?"}]})
    print("Weather Response:", weather_response['messages'][-1].content)

asyncio.run(main())

