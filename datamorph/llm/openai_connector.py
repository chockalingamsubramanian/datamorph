# Example connector using OpenAI API (can be replaced with Claude/OpenRouter/etc.)

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def call_llm(prompt, model="gpt-3.5-turbo"):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful pipeline planner."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"LLM call failed: {e}")
        return "error"
