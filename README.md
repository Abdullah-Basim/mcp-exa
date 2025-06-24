# 🔥 Exa MCP Server

A **real remote MCP Server** using the **Exa Search API** that streams real-time web search context via Server-Sent Events (SSE).

## ✅ Features

- 🌐 **Real-time web search** via Exa API
- 📡 **SSE streaming** for live results
- 🚀 **FastAPI** backend with async support
- 🔌 **MCP protocol** compatible
- 🌍 **Deployable** to Railway, Heroku, etc.

## 🚀 Quick Start

### 1. Setup

```bash
# Clone and setup
git clone <your-repo>
cd exa-mcp

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

Update `.env` with your Exa API key:

```env
EXA_API_KEY=your_actual_exa_api_key_here
```

### 3. Run Locally

```bash
uvicorn server:app --reload
```

### 4. Test

Visit: http://localhost:8000/mcp?query=What is MCP protocol?

## 🔌 MCP Integration

### Claude Desktop

Add to your Claude tool config:

```json
{
  "tools": [
    {
      "name": "exa_mcp",
      "description": "Streams search results from Exa",
      "endpoint": "https://your-domain.com/mcp?query={{query}}",
      "protocol": "sse"
    }
  ]
}
```

### Cursor

```yaml
tools:
  - name: exa_mcp
    description: "Real-time web search via Exa"
    endpoint: https://your-domain.com/mcp?query={{query}}
    protocol: sse
```

## 🚀 Deploy to Railway

1. Push to GitHub
2. Go to [railway.app](https://railway.app)
3. Deploy from GitHub repo
4. Add environment variable: `EXA_API_KEY`
5. Get your custom domain!

## 📡 API Endpoints

- `GET /` - Server status
- `GET /mcp?query=<search_query>` - Stream search results

## 🛠️ Built With

- **FastAPI** - Web framework
- **SSE-Starlette** - Server-Sent Events
- **Exa API** - AI-powered search
- **Python-dotenv** - Environment management

---

**Happy searching! 🔍** 