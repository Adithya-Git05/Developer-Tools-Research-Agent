# Developer-Tools-Research-Agent

## Overview

**Developer Tools Research Agent** is an AI-powered research assistant for developer tools and technology companies. It leverages LLMs and web scraping to extract, analyze, and recommend developer-focused products, platforms, and services. The project features a modular workflow, Streamlit web interface, and integration with Groq and Firecrawl APIs.

---

## Features

- **Automated Tool Extraction:** Finds and lists developer tools from articles and web content.
- **Company Analysis:** Gathers and structures information about tech companies, including pricing, tech stack, API availability, and more.
- **Developer Recommendations:** Provides concise, actionable recommendations for developers.
- **Web Scraping:** Uses Firecrawl for targeted web searches and content extraction.
- **LLM Integration:** Supports Groq-hosted models for advanced language understanding.
- **Streamlit UI:** User-friendly web interface for interactive research.

---

## Technologies Used

- **Python 3.13+**
- **LangGraph** (workflow orchestration)
- **LangChain-Groq** (LLM integration)
- **Firecrawl-Py** (web scraping)
- **Streamlit** (web app)
- **Pydantic** (data modeling)
- **python-dotenv** (environment management)

---

## Getting Started

### Prerequisites

- Python 3.13 or higher
- Groq API key
- Firecrawl API key

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Adithya-Git05/Developer-Tools-Research-Agent
   cd Advanced-Agent
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -e .
   ```

4. **Set up your `.env` file:**
   ```
   GROQ_API_KEY=your_groq_api_key
   FIRECRAWL_API_KEY=your_firecrawl_api_key
   ```

---

## Usage

### Command Line

```bash
uv run main.py
```

### Streamlit Web App

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## Project Structure

```
Advanced-Agent/
├── app.py                # Streamlit web interface
├── main.py               # CLI entry point
├── src/
│   ├── models.py         # Data models
│   ├── workflow.py       # Workflow orchestration
│   ├── firecrawl.py      # Firecrawl integration
│   ├── prompts.py        # LLM prompt templates
├── pyproject.toml        # Project dependencies
├── .env                  # API keys (not committed)
```

---

## License

Apache-2.0 License – Users are free to use, modify, and distribute the tool under the terms of this license.


---


Project activity: no published releases or packages yet.

