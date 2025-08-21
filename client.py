import sys
import asyncio
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters

async def main():
    print("Starting client...")
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["server.py"]
    )

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream=read_stream, write_stream=write_stream) as session:
            await session.initialize()
            print(" Connected to server")

            # list tools returns tuples (name, description, schema)
            tools = await session.list_tools()
            print("Available tools:", [t.name for t in tools.tools])  # just tool names

            res = await session.call_tool("add", {"a": 5, "b": 7})
            print("add(5,7) =", res.structuredContent["result"])

            res = await session.call_tool("multiply", {"a": 3, "b": 4})
            print("multiply(3,4) =", res.structuredContent["result"])

asyncio.run(main())
