# AI Transaction Categorization Agent

This project implements a **backend-only AI-powered transaction categorization service** using **Django REST Framework** and a **local Large Language Model (LLM)** via **Ollama**.

The system accepts transaction data and company context, then uses an LLM-powered agent to determine the most appropriate accounting category.

---

# Architecture Overview

The system follows a modular agent-based architecture:

```
Client Request
      ↓
Django REST API (/categorize)
      ↓
Categorization Agent
      ↓
Prompt Builder
      ↓
LLM Client (Ollama)
      ↓
Response Parser
      ↓
Structured JSON Response
```
Architecture follows an agent-based pattern with a pluggable LLM client.
### Components

**API Layer**

* Handles HTTP requests
* Validates input
* Calls the categorization agent

**Categorization Agent**

* Orchestrates the workflow
* Builds prompts
* Calls the LLM client
* Parses model responses

**Prompt Builder**

* Constructs contextual prompts for the LLM
* Includes company industry and chart of accounts

**LLM Client**

* Interface for interacting with the LLM
* Current implementation uses **Ollama**

**Response Parser**

* Extracts and validates structured JSON from LLM output
* Provides fallback for malformed responses

---

# Features

* Django REST API
* AI-powered transaction categorization
* Modular agent-based architecture
* Prompt engineering with contextual inputs
* LLM abstraction layer
* Local model support via Ollama
* Structured JSON outputs
* Robust response parsing

---

# LLM Model

This implementation uses a **local LLM via Ollama**.

Current model used:

```
gemma:2b
```

Advantages:

* Runs locally
* No API keys required
* Free to use
* Easily swappable with other models

---

# Project Structure

```
trans_agent/
│
├── api/
│   ├── views.py
│   ├── urls.py
│
├── services/
│   ├── categorization_agent.py
│   ├── prompt_builder.py
│   ├── response_parser.py
│
├── llm/
│   ├── base_client.py
│   ├── ollama_client.py
│
├── config/
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Setup Instructions

## 1. Clone Repository

```
git clone https://github.com/Harshsingh15/category_agent.git
cd trans_agent
```

---

## 2. Create Virtual Environment

```
python -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

# Install Ollama

Install Ollama:

```
curl -fsSL https://ollama.com/install.sh | sh
```

Verify installation:

```
ollama --version
```

---

# Download Model

Pull the Gemma model:

```
ollama pull gemma:2b
```

---

# Start Ollama

Run:

```
ollama serve
```

This starts the local LLM server.

---

# Run Django Server

Apply migrations:

```
python manage.py migrate
```

Start server:

```
python manage.py runserver
```

Server runs at:

```
http://127.0.0.1:8000
```

---

# API Endpoint

## POST `/categorize`

Categorizes a transaction using the provided company context.

---

# Example API Request

```
curl -X POST http://127.0.0.1:8000/categorize/ \
-H "Content-Type: application/json" \
-d '{
"transaction": {
"description": "Adobe Creative Cloud subscription"
},
"company_context": {
"industry": "Software",
"chart_of_accounts": [
"Office Supplies",
"Travel",
"Software Subscriptions",
"Meals & Entertainment"
]
}
}'
```

---

# Example Response

```
{
  "category": "Software Subscriptions",
  "confidence": 1,
  "reasoning": "The description describes a subscription to Adobe Creative Cloud."
}
```

---

# Additional Example

### Request

```
curl -X POST http://127.0.0.1:8000/categorize/ \
-H "Content-Type: application/json" \
-d '{
"transaction": {
"description": "Uber ride to airport"
},
"company_context": {
"industry": "Software",
"chart_of_accounts": [
"Office Supplies",
"Travel",
"Software Subscriptions",
"Meals & Entertainment"
]
}
}'
```

### Response

```
{
  "category": "Travel",
  "confidence": 0.92,
  "reasoning": "Uber rides to airports are typically categorized as travel expenses."
}
```

---

# Design Decisions

### Modular Architecture

Each component has a clear responsibility, making the system easy to extend and maintain.

### LLM Abstraction Layer

The LLM client is abstracted so the system can easily switch to:

* OpenAI
* Anthropic
* Azure OpenAI
* Other local models

### Prompt Engineering

The prompt builder includes:

* Industry context
* Chart of accounts
* Examples for improved classification accuracy.

### Robust Response Parsing

The parser extracts valid JSON from model responses and handles malformed outputs gracefully.

---

# Future Improvements

* Add unit tests
* Implement evaluation metrics
* Add transaction history context
* Support multiple LLM providers
* Add caching for repeated queries

---

# Example Workflow

1. Client sends transaction data
2. API receives request
3. Agent constructs prompt
4. Prompt sent to LLM
5. LLM generates classification
6. Parser extracts JSON response
7. API returns structured result

---

# Requirements

```
django
djangorestframework
requests
```

---

# Author

AI Transaction Categorization Agent – Backend Assignment Implementation
