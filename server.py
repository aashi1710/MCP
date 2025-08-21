# server.py
from fastmcp import FastMCP
import asyncio

# Create MCP server instance
mcp = FastMCP("math-server")

# Add function: add two numbers
@mcp.tool()
async def add(a: int, b: int) -> int:
    """Add two integers"""
    return a + b

# Multiply function
@mcp.tool()
async def multiply(a: int, b: int) -> int:
    """Multiply two integers"""
    return a * b

if __name__ == "__main__":
    # Run server with stdio transport
    mcp.run(transport="stdio")

