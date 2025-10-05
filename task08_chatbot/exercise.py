# Task 8 - Chatbot (Exercise File)
#
# 🧩 CHALLENGE: Create your own specialized chatbot
#
# Requirements:
# - Create a chatbot with a specific personality or purpose
# - Use the provided template to customize the system prompt
# - Add your own knowledge base relevant to your chatbot's purpose
# - Implement chat history saving functionality
# - Make your chatbot respond in a unique way (different instructions)
#
# Ideas for your chatbot:
# - A cooking assistant that helps with recipes
# - A study buddy that helps with homework
# - A travel guide for a specific city
# - A fitness coach that gives workout advice
# - A pet care expert
# - A coding tutor
# - A movie recommendation bot
#
# 💡 TIP: You can use an AI assistant to help you with this task!
# Ask questions like:
# - "How do I create a good system prompt for a chatbot?"
# - "What should I include in a knowledge base for a cooking bot?"
# - "How do I make my chatbot have a specific personality?"
# - "What are some good instructions for a helpful chatbot?"
#
# Your code goes here:
# TODO: Create your specialized chatbot below this line

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


def respond(user_message, chat_history):
    prompt = f"""
    YOUR SYSTEM PROMPT HERE

    Instructions:
    - YOUR INSTRUCTIONS HERE

    Knowledge base:
    - THE KNOWLEDGE BASE OF YOUR APP HERE

    Respond to the user's message below:
    {user_message}
    """
    # Generate a response
    response = prompt_llm(prompt)

    chat_history.append((user_message, response))
    return response


# TODO: Create your chatbot main function here and make save the chat history
# def my_chatbot():
#     # Your chatbot implementation
#     pass

# TODO: Uncomment to run your chatbot
# my_chatbot()
