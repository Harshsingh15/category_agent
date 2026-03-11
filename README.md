# AI Transaction Categorization Agent

This project implements a **backend-only AI-powered transaction categorization service** using **Django REST Framework** and a **local Large Language Model (LLM)** via **Ollama**.

The service receives a transaction and company context, then uses an AI agent to classify the transaction into the most appropriate accounting category.

---

# Architecture

The system follows a **modular agent-based architecture**.

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

### Components

**API Layer**

* Handles HTTP requests
* Validates input
* Invokes the categorization agent

**Categorization Agent**

* Orchestrates the classification workflow
* Builds prompts
* Invokes the LLM
* Parses responses

**Prompt Builder**

* Constructs structured prompts for the LLM
* Includes company context and chart of accounts

**LLM Client**

* Abstract interface for interacting with LLM providers
* Current implementation uses **Ollama**

**Response Parser**

* Extracts structured JSON from model responses
* Handles malformed responses safely

---

# Features

* Django REST API
* AI-powered transaction categorization
* Agent-based architecture
* Prompt engineering
* LLM abstraction layer
* Local model execution via Ollama
* Structured JSON responses
* Input validation
* Health check endpoint

---

# Project Structure

```
trans_agent/
│
├── api/
│   ├── serializers.py
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

## 1. Clone the Repository

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

# Download the Model

Pull the **Gemma model**:

```
ollama pull gemma:2b
```

---

# Start Ollama Server

```
ollama serve
```

This runs the local LLM server used by the application.

---

# Run the Django Server

Apply migrations:

```
python manage.py migrate
```

Start server:

```
python manage.py runserver
```

Server will run at:

```
http://127.0.0.1:8000/
```

---

# API Endpoints

## Health Check

### Request

```
GET /health
```

Example:

```
curl http://127.0.0.1:8000/health/
```

### Response

```
{
 "status": "ok",
 "service": "transaction-categorization-agent"
}
```

---

# Transaction Categorization

## Endpoint

```
POST /categorize
```

---

# Example Request

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

# Another Example

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

Each component is separated for clarity and maintainability.

### LLM Abstraction

The system uses an abstract LLM client, allowing easy switching between providers such as:

* OpenAI
* Anthropic
* Azure OpenAI
* Local models via Ollama

### Prompt Engineering

Prompts include:

* Industry context
* Chart of accounts
* Example transactions

This improves classification accuracy for smaller models.

### Robust Response Parsing

The parser extracts valid JSON from LLM responses and provides fallback behavior if parsing fails.

---

# Future Improvements

* Add automated evaluation metrics
* Support multiple LLM providers
* Add transaction history context
* Implement caching for repeated queries
* Add unit tests

---

# Requirements

```
django
djangorestframework
requests
```

---

# Author

Backend AI Transaction Categorization Agent Implementation
