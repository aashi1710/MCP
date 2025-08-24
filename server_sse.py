# server_sse.py
from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP(name="MathServer")

# Register tools
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

if __name__ == "__main__":
    
    mcp.run(transport="sse")   
