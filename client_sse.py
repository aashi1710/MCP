import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def main():
    print("Starting MCP client...")

    async with sse_client("http://127.0.0.1:8000/sse") as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("Available tools:", [t.name for t in tools.tools])

            result_add = await session.call_tool("add", {"a": 5, "b": 7})
            print("add(5,7) =", result_add.structuredContent["result"])

            result_mul = await session.call_tool("multiply", {"a": 3, "b": 4})
            print("multiply(3,4) =", result_mul.structuredContent["result"])

if __name__ == "__main__":
    asyncio.run(main())
