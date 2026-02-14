🧠 AI Lead Response Assistant

A modular AI workflow that reads customer property enquiries and generates safe, structured, and human-like responses using an open-source LLM.

🚀 Overview

This project implements a structured AI pipeline for handling customer property issues such as:

“I am getting damp patches on my bedroom wall after heavy rain.”

Instead of a single LLM call, the system follows a multi-step reasoning workflow to ensure reliability and reduce hallucinations.

🏗 Architecture
User Query
   ↓
Intent Classification
   ↓
Structured Information Extraction (JSON)
   ↓
Missing Information Detection (Deterministic)
   ↓
Clarifying Question Generation
   ↓
Safe Advice Generation
   ↓
Validation Guard (Rule-based)
   ↓
Deterministic Final Response Composition

🔍 Key Design Decisions
✅ Structured Before Generative

The system first extracts structured data:

{
  "location": "",
  "trigger": "",
  "symptoms": "",
  "duration": "",
  "urgency": ""
}


This enables:

Targeted clarification

Missing data detection

Reduced hallucination risk

✅ Hybrid AI Design

LLM → reasoning & generation

Python logic → validation & control

This improves safety and reliability.

✅ Guardrails

A validation layer checks for:

Absolute claims

Diagnoses

Guarantees

Risky certainty language

🛠 Tech Stack

Llama 3.1 8B Instruct (quantized)

Ollama (local model serving)

Python

Requests

Model used:

llama3.1:8b-instruct-q4_0

📂 Project Structure
lead_response_assistant/
│
├── main.py           # Workflow orchestration
├── llm_engine.py     # LLM communication layer
├── prompts.py        # Structured prompt templates
├── validator.py      # Guardrail logic
└── README.md

▶ How to Run
1️⃣ Install Ollama

https://ollama.com

2️⃣ Pull Model
ollama pull llama3.1:8b-instruct-q4_0

3️⃣ Setup Environment
python -m venv venv
venv\Scripts\activate
pip install requests

4️⃣ Run
python main.py

💡 Example Behavior

Input

I am getting damp patches on my bedroom wall after heavy rain.


Output

Professional acknowledgement

Relevant clarifying questions

Safe homeowner advice

No diagnosis

No false promises

🔒 Reliability Features

Strict JSON extraction

Deterministic missing field detection

Targeted clarifying questions

Safety validation layer

Deterministic final response composition

Debug vs production mode

⚠ Limitations

Single-turn interaction (no memory)

Open-source model may require prompt tuning for edge cases

CLI-based interface (no frontend)

🔮 Future Improvements

Add automatic retry for malformed JSON

Add confidence scoring

Add conversation memory

Deploy via FastAPI

Add evaluation test suite

🎯 Why This Matters

This project demonstrates:

Applied AI workflow design

Hallucination mitigation

Hybrid deterministic + LLM architecture

Production-oriented system thinking
