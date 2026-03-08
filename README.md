# CompanyInsight AI (V1)

First structured version of an automated company research tool.

## What we made?

We built a full-stack AI tool that takes a company website URL and returns structured business insights.

Output fields:
- `company_name`
- `industry`
- `summary`
- `products_services`
- `target_customers`
- `pain_points`

This project includes:
- `backend/`: FastAPI + LangGraph workflow + LLM agents
- `frontend/`: HTML/CSS/JS UI to submit URL and display results

## How?

The system uses a 2-agent workflow orchestrated with LangGraph:

1. Website Content Agent
- Receives URL
- Calls a tool (`fetch_webpage`) to extract relevant company website text

2. Company Analysis Agent
- Reads extracted content
- Produces a structured response using a schema (`ResponseSchema`)

Core technologies:
- Python
- FastAPI
- LangGraph
- LangChain OpenAI
- Pydantic
- BeautifulSoup / Requests

## Process?

End-to-end flow:

1. User enters a company URL in frontend (`index.html`).
2. Frontend calls backend endpoint: `POST /analyze-company`.
3. Backend creates `Graph()` workflow.
4. Node 1 fetches website content via tool call.
5. Node 2 analyzes content with structured output.
6. Backend returns JSON response.
7. Frontend renders fields in result cards.

## How to run this?

### 1) Clone project

```bash
git clone https://github.com/MeetSolanki530/companyinsight-ai.git
cd companyinsight-ai
```

If the local project is already initialized and you want to connect it to GitHub:

```bash
git remote add origin https://github.com/MeetSolanki530/companyinsight-ai.git
```

### 2) Setup backend environment

```bash
cd backend
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3) Configure environment variables

Create `.env` inside `backend/` (copy from `.env.example`).

```bash
copy .env.example .env
```

### 4) Start backend

From `backend/`:

```bash
uvicorn app:app --reload --port 8080
```

### 5) Open frontend

Option A:
- Open `http://127.0.0.1:8080/frontend`

Option B:
- Open `frontend/index.html` manually (if API calls are configured to backend URL)

## What to configure?

Required environment variables (`backend/.env`):

- `OPENAI_API_KEY`: your API key
- `OPENAI_MODEL`: model name (example: `gpt-4o-mini`)
- `OPENAI_BASE_URL`: API base URL

Notes:
- For official OpenAI API, base URL is typically `https://api.openai.com/v1`.
- If using another provider-compatible endpoint, set that provider base URL.

## API

Health/root:
- `GET /`

Analyze company:
- `POST /analyze-company`

Example request:

```json
{
  "url": "https://stripe.com"
}
```

## Project Structure (Current)

```text
backend/
  app.py
  requirements.txt
  src/
    agents/
    api/
    config/
    models/
    tools/
    workflow/
frontend/
  index.html
  how-it-works.html
  css/style.css
  js/script.js
```

## Version Note

This is the first structured version (V1).

Planned improvements for next versions:
- Better error handling and retries
- Async workflow performance improvements
- Optional result persistence (DB)
- Docker support
- Automated tests for agents and API
