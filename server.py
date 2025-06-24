import os, json
import requests
from fastapi import FastAPI, Query
from sse_starlette.sse import EventSourceResponse

app = FastAPI()

EXA_API_KEY = "fc26237b-f65c-465d-b1d7-4b8bc3f76e8a"

@app.get("/mcp")
async def mcp_stream(query: str = Query(...)):
    async def event_gen():
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer fc26237b-f65c-465d-b1d7-4b8bc3f76e8a"
        }
        url = "https://api.exa.ai/search"
        data = {
            "query": query,
            "numResults": 5,
            "contents": {"text": True}  # 🔥 Request actual content!
        }

        try:
            response = requests.post(url, json=data, headers=headers, timeout=15)
            response.raise_for_status()
            api_response = response.json()
            results = api_response.get("results", [])
            
            # Debug: Show what fields are available
            if results:
                first_result_keys = list(results[0].keys())
                yield {"data": json.dumps({"debug": "Available fields", "fields": first_result_keys})}
            
        except Exception as e:
            yield {"data": json.dumps({"error": f"API Error: {str(e)}"})}
            return

        if not results:
            yield {"data": json.dumps({"message": "No results found"})}
            return

        for i, result in enumerate(results):
            # Try multiple content fields
            content = (
                result.get("text", "") or 
                result.get("snippet", "") or 
                result.get("summary", "") or 
                result.get("content", "") or
                result.get("description", "") or
                "Content not available"
            )
            
            yield {
                "data": json.dumps({
                    "title": result.get("title", f"Result {i+1}"),
                    "url": result.get("url", ""),
                    "snippet": content[:500] + "..." if len(content) > 500 else content,
                    "full_content": content
                })
            }

    return EventSourceResponse(event_gen())

@app.get("/")
async def root():
    return {"message": "Exa MCP Server with FULL CONTENT is running! Use /mcp?query=your_search_query"}

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting ENHANCED Exa MCP Server with Full Content...")
    uvicorn.run(app, host="0.0.0.0", port=8001)