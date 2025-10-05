"""
Concept: Chatbot

This example demonstrates creating chatbots with different levels of intelligence.
Students will learn about conversation handling, prompt engineering, and chat history management.
"""

# Task 8 - Chatbot (Example File)
# This file demonstrates creating simple and smart chatbots

# suppress warnings
import warnings
from dotenv import load_dotenv

warnings.filterwarnings("ignore")

# import libraries
import requests, os

from together import Together
import textwrap

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
client = Together(api_key=TOGETHER_API_KEY)


## FUNCTION 1: This Allows Us to Prompt the AI MODEL
# -------------------------------------------------
def prompt_llm(prompt, with_linebreak=False):
    # This function allows us to prompt an LLM via the Together API

    # model
    model = "meta-llama/Meta-Llama-3-8B-Instruct-Lite"

    # Make the API call
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    output = response.choices[0].message.content

    if with_linebreak:
        # Wrap the output
        wrapped_output = textwrap.fill(output, width=50)

        return wrapped_output
    else:
        return output


# Simple dummy chatbot
def dummy_chatbot():
    """A simple chatbot that always responds the same way"""
    print("=== Dummy Chatbot ===")
    print("Type 'quit' to exit")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "quit":
            print("Bot: Goodbye!")
            break
        print("Bot: I am just a bot")


# Run the dummy chatbot
dummy_chatbot()


# Smart chatbot with LLM (Uncomment Below)
# -------------------------------------------
def smart_chatbot():
    """A smart chatbot that uses LLM to respond"""
    print("=== Smart Chatbot ===")
    print("Type 'quit' to exit")

    chat_history = []

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "quit":
            print("Bot: Goodbye!")
            break

        response = respond(user_input, chat_history)
        print(f"Bot: {response}")


def respond(user_message, chat_history):
    prompt = f"""
    You are a General, Funny AI Chatbot that loves to help people

    Instructions:
    - Make your answers at most 10 words
    - Always start with saying 'Thank you for Responding'
    - Only give the response to the message
    - Please use the knoweldge base to answer the question if relevant

    Knowledge base:
    - I only work from 10am to 5pm

    Question Answers Examples

    Respond to the user's message below:
    {user_message}
    """
    # Generate a response
    response = prompt_llm(prompt)

    chat_history.append((user_message, response))
    return response


smart_chatbot()
