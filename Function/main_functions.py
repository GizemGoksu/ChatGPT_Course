import openai
import os

# Python dotenv is a powerful tool that makes it easy to handle environment variables in Python applications from start to finish.
# The library reads from a .env file at the root of your project and loads them into os.environ. These environment variables can then be accessed in your code.

# Buradan oku --> https://medium.com/@sujathamudadla1213/what-is-the-use-of-env-8d6b3eb94843
# A .env file is a text file containing key value pairs of all the environment variables required by your application. This file is included with your project locally but not saved to source control so that you aren't putting potentially sensitive information at risk.
# The .env file is particularly useful for storing sensitive information such as API keys, access tokens, and passwords. By keeping this information in a separate file, you can share the main codebase without exposing sensitive details. This is crucial for security, especially when collaborating on projects or sharing code repositories.

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file and load environment variables from .env file


client = openai.OpenAI(api_key="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")

def get_completion(prompt,model="gpt-3.5-turbo",temperature=0):
    messages = [{"role": "user", "content": prompt}] # dictionary list
    response = client.chat.completions.create(
        model = model,
        messages = messages,
        temperature = temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content

# Temperature artarsa randomluk artar ve yaratcılık artabilir.