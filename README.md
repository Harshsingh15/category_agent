# AI Transaction Categorization Agent

This project implements a backend-only AI-powered transaction categorization service using Django REST Framework and a local LLM via Ollama.

## Architecture

API → Categorization Agent → Prompt Builder → LLM Client → Response Parser → JSON Response

## Features

- Django REST API
- AI categorization agent
- Prompt engineering for classification
- LLM abstraction layer
- Local LLM support via Ollama
- Structured JSON responses
- Error handling and response parsing

## LLM

The system uses a pluggable LLM architecture.

Current implementation uses:

Ollama + Gemma (local model)

This can easily be swapped with OpenAI or other providers.

## Setup

Clone the repository:
