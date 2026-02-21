# Architecture Diagram

This document provides a high-level overview of the system architecture. Replace with a proper diagram file (e.g. `architecture.png`) when available.

```
User Browser
    |
    | POST /generate (form)
    v
Flask Server (app.py)
    |
    | calls Groq Chat Completions API
    v
Groq LLM Service
    |
    | returns itinerary text
    v
Flask Server renders result.html
    |
    | response HTML
    v
User Browser
```
