import asyncio
from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse
import uvicorn
import json

app = FastAPI()

# --- Our math tools ---
def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

@app.get("/sse")
async def sse(request: Request):
    """
    SSE endpoint that continuously sends available tools to the client
    """
    async def event_generator():
        while True:
            if await request.is_disconnected():
                break

            # Send tool list as JSON
            tools = {
                "tools": {
                    "add": "Adds two numbers",
                    "multiply": "Multiplies two numbers"
                }
            }
            yield {"event": "tools", "data": json.dumps(tools)}
            await asyncio.sleep(5)  # every 5 seconds

    return EventSourceResponse(event_generator())

@app.get("/run/{tool}")
async def run_tool(tool: str, a: int, b: int):
    """
    Endpoint to call a tool with parameters.
    Example: /run/add?a=5&b=7
    """
    if tool == "add":
        result = add(a, b)
    elif tool == "multiply":
        result = multiply(a, b)
    else:
        result = f"Unknown tool: {tool}"

    return {"tool": tool, "a": a, "b": b, "result": result}

if __name__ == "__main__":
    uvicorn.run("server_sse:app", host="127.0.0.1", port=8000, reload=True)
