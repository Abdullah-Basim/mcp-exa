import os, json
from fastapi import FastAPI, Query
from sse_starlette.sse import EventSourceResponse

app = FastAPI()

@app.get("/mcp")
async def mcp_stream(query: str = Query(...)):
    async def event_gen():
        # Mock search results for testing
        mock_results = [
            {
                "title": f"Result 1 for '{query}'",
                "url": "https://example.com/1",
                "text": f"This is a mock result about {query}. It demonstrates the SSE streaming functionality."
            },
            {
                "title": f"Result 2 for '{query}'",
                "url": "https://example.com/2", 
                "text": f"Another mock result about {query}. This shows how multiple results are streamed."
            },
            {
                "title": f"Result 3 for '{query}'",
                "url": "https://example.com/3",
                "text": f"Final mock result for {query}. The streaming works perfectly!"
            }
        ]

        for result in mock_results:
            yield {
                "data": json.dumps({
                    "title": result["title"],
                    "url": result["url"],
                    "snippet": result["text"]
                })
            }

    return EventSourceResponse(event_gen())

@app.get("/")
async def root():
    return {"message": "Exa MCP Server is running! Use /mcp?query=your_search_query", "status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting Exa MCP Test Server...")
    uvicorn.run(app, host="0.0.0.0", port=8001) 