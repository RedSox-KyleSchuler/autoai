from dotenv import load_dotenv
import os
import openai
import re

# Load OpenAI API credentials
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set the GPT-3.5 Turbo model
model_engine = "gpt-3.5-turbo"

def generate_text(prompt):
    try:
        response = openai.ChatCompletion.create(
            engine=model_engine,
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}],
            max_tokens=1024,
            temperature=0.7,
        )
        message = response.choices[0].message.text.strip()
        return message
    except Exception as e:
        print(f"Error: {e}")
        return None

def generate_code(prompt):
    prompt = f"```python\n{prompt}\n```"
    response = generate_text(prompt)
    if response:
        return re.sub("```python\n|```", "", response).strip()
    else:
        return None