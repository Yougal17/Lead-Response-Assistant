from llm_engine import call_llm
from prompts import intent_prompt, extraction_prompt, clarification_prompt, advice_prompt
from validator import validate_response
import json


if __name__ == "__main__":
    query = input("Enter customer query: ")

    #Step 1: Intent Classification
    category = call_llm(intent_prompt(query))
    
    DEBUG = False
    if DEBUG:
        print("\n--- Intent Classification ---")
        print("Detected Category:", category)

    # print("\n--- Intent Classification ---")
    # print("Detected Category:", category)
    
    #Step 2: Structured Extraction
    raw_extraction = call_llm(extraction_prompt(query))
    
    # print("\n--- Raw Extraction ---")
    # print(raw_extraction)
    
    # Trying parsing JSON
    try:
        structured_data = json.loads(raw_extraction)
        # print("\n--- Parsed Structured Data ---")
        # print(structured_data)
    except json.JSONDecodeError:
        print("\n ⚠️ Failed to parse JSON. Model didn't return valid JSON")


    #Step 3: Detect Missing Information
    missing_fields = [
        key for key, value in structured_data.items()
        if value == "Not Available"
    ]
    
    # print("\n--- Missing Information Detected ---")
    # if missing_fields:
    #     print(missing_fields)
    # else:
    #     print("No missing fields detected.")
        
    # Step 4: Generate Clarifying Questions
    if missing_fields:
        clarifying_questions = call_llm(
            clarification_prompt(structured_data, missing_fields)
        )

        # print("\n--- Clarifying Questions ---")
        # print(clarifying_questions)
    else:
        clarifying_questions = "No clarification needed."
        
    # Step 5: Generate Safe Advice
    safe_advice = call_llm(advice_prompt(structured_data))

    # print("\n--- Safe Advice ---")
    # print(safe_advice)

    # Step 6: Validate Advice
    is_safe = validate_response(safe_advice)

    # print("\n--- Validation Check ---")
    # if is_safe:
    #     print("Advice passed validation.")
    # else:
    #     print("⚠️ Advice contains risky language.")
        
    clarifying_questions = clarifying_questions.strip()
    safe_advice = safe_advice.strip()
    
    # Step 7: Compose Final Response (Deterministic)

    final_response = f"""
Hi, thank you for reaching out.

Damp patches after heavy rain can certainly be concerning, and it’s good that you’re monitoring it.

From what you've described, this appears to be related to {category}.

To better understand the situation, I’d like to ask a few quick questions:

{clarifying_questions}

In the meantime, you may consider the following steps:

{safe_advice}

Once you share a bit more detail, I’ll be happy to guide you further.
"""

print("\n================ RESPONSE ================\n")
print(final_response.strip())
