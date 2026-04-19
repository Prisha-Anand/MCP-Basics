from mcp.server.fastmcp import FastMCP
@mcp.tool
def weather(location:str) -> str:
    """
    Gives you the weather in a city 
    """
    return "Weather is fine in California"

