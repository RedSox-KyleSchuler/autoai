import openai
import os
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to send a message to the OpenAI API and receive a response
def ask(message):

    # Send the request to the OpenAI API
    response = openai.ChatCompletion.create(
        model= "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ],
        max_tokens=1024,
        temperature=0.7,
    )

    # Return the response
    return response.choices[0].message.text.strip()