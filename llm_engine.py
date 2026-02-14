import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.1:8b-instruct-q4_0"


def call_llm(prompt, temperature=0.2):
    """
    Sends a prompt to the Ollama model and returns the response.
    """

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": temperature
                }
            },
            timeout=120
        )

        response.raise_for_status()

        return response.json()["response"].strip()

    except requests.exceptions.RequestException as e:
        return f"LLM Error: {str(e)}"
