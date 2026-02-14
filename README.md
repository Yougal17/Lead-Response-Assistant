📌 Overview

This project implements a modular AI Lead Response Assistant that reads a customer property-related enquiry and generates a structured, safe, and human-like response.

The system is designed with a strong focus on:

Structured reasoning

Reliability

Hallucination control

Guardrails against false claims

Modular AI workflow design

The solution uses an open-source LLM (Llama 3.1 8B Instruct via Ollama) running locally.

🎯 Objective

Given a customer query such as:

“I am getting damp patches on my bedroom wall after heavy rain.”

The system:

Understands the issue category

Extracts structured information

Detects missing details

Generates targeted clarifying questions

Provides safe next steps

Validates output for risky language

Composes a final professional response

🏗 System Architecture

The assistant is built as a multi-step modular workflow, not a single LLM call.

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

🔍 Design Philosophy
1️⃣ Structured Before Generative

Instead of directly generating a reply, the system first extracts structured fields:

{
  "location": "",
  "trigger": "",
  "symptoms": "",
  "duration": "",
  "urgency": ""
}


This enables:

Controlled reasoning

Missing data detection

Targeted clarification

Reduced hallucination risk

2️⃣ Deterministic + LLM Hybrid Design

The system combines:

LLM-based reasoning (classification, extraction, generation)

Deterministic Python logic (missing field detection, validation, composition)

This improves reliability and control.

3️⃣ Guardrails & Safety

A validation layer checks for:

Absolute claims (e.g., “definitely”, “must be”)

Diagnostic statements

Guarantees or promises

Risky certainty language

This ensures the assistant avoids hallucinated or misleading advice.

🛠 Technologies Used

Llama 3.1 8B Instruct (quantized)

Ollama (local model serving)

Python

Requests library

Model used:

llama3.1:8b-instruct-q4_0


The quantized model ensures compatibility with limited GPU resources.

📂 Project Structure
lead_response_assistant/
│
├── main.py           # Orchestrates the workflow
├── llm_engine.py     # Handles model API calls
├── prompts.py        # Stores structured prompt templates
├── validator.py      # Validation & guardrail logic
└── README.md

▶ How to Run
1️⃣ Install Ollama

https://ollama.com

2️⃣ Pull Model
ollama pull llama3.1:8b-instruct-q4_0

3️⃣ Activate Virtual Environment
python -m venv venv
venv\Scripts\activate
pip install requests

4️⃣ Run
python main.py


Enter a customer query when prompted.

✅ Example Output

Input:

I am getting damp patches on my bedroom wall after heavy rain for the past two weeks.

Output:

Professional acknowledgement

Targeted clarification questions

Safe homeowner guidance

No diagnosis

No promises

Human tone

🔒 Reliability Features

Strict JSON extraction format

Explicit “Not Available” handling

Deterministic missing field detection

Targeted clarifying questions

Guardrail validation layer

Deterministic final response composition

⚠ Limitations

Open-source model may require prompt refinement for edge cases

No conversation memory (single-turn assistant)

No confidence scoring or retry logic (can be added)

No frontend interface (CLI-based interaction)

🚀 Possible Improvements

With more time, I would:

Add automatic retry if JSON parsing fails

Add confidence scoring for extracted fields

Add multi-turn conversation memory

Add evaluation test suite

Deploy via FastAPI endpoint

Add logging system for production monitoring

🎥 Demonstration

A 3–5 minute Loom video explains:

Architecture decisions

Reliability design

Guardrails

Limitations

Future improvements

🏁 Conclusion

This solution demonstrates:

Structured AI workflow design

Reliability-focused architecture

Hallucination mitigation strategies

Hybrid deterministic + LLM reasoning

Production-oriented modular system thinking
