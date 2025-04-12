import os
from openai import OpenAI

#from dotenv import load_dotenv
# Load environment variables from .env
#load_dotenv() <<-- use this for local development
#api_key=os.getenv("OPENAI_API_KEY") <<-- use this for local development

#def getapikey():
#    with open('/run/secrets/my_secret') as f:
#        api_key = f.read().strip()
#    return api_key
# Initialize OpenAI client
#client = OpenAI(api_key=getapikey())

def call_llm(prompt, model="gpt-3.5-turbo"):
    try:
        # ECS injects this secret into the container as an environment variable
        api_key = os.getenv("OPENAI_API_KEY")
        client = OpenAI(api_key)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful pipeline planner."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"[❌] LLM call failed: {e}")
        return "error"
