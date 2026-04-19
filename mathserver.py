from mcp.server.fastmcp import FastMCP
@mcp.tool
def add(a:int,b:int) -> int:
    return a + b
@mcp.tool
def mult(a:int,b:int) -> int:
    return a*b
