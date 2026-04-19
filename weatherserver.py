from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Weather")
@mcp.tool()
def weather(location:str) -> str:
    """
    Gives you the weather in a city 
    """
    return "Weather is fine in California"

if __name__ == "__main__":
    mcp.run(transport = "streamable-http")