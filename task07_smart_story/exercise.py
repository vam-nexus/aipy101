# Task 7 - Smart Story (Exercise File)
#
# 🧩 CHALLENGE: Create an AI-powered interactive story system
#
# Requirements:
# - Use the provided prompt_llm function to generate dynamic story content
# - Create a story that adapts based on user choices and input
# - Implement a conversation system where the AI responds to user questions
# - Save all generated content to the results/ folder
# - Include error handling for API failures
# - Make the story interactive with multiple branching paths
#
# Advanced Features to Consider:
# - Create a character that the AI can roleplay as
# - Implement a memory system that remembers previous interactions
# - Add different story genres (mystery, fantasy, sci-fi, etc.)
# - Create a story generator that can create multiple story variations
# - Implement a rating system for generated stories
# - Add voice-to-text or text-to-voice capabilities
#
# 💡 TIP: You can use an AI assistant to help you with this task!
# Ask questions like:
# - "How do I create branching story paths with LLM responses?"
# - "What's the best way to handle API errors in Python?"
# - "How can I make an AI character that remembers previous conversations?"
# - "How do I create different story genres with prompt engineering?"
# - "What are some techniques for making AI responses more consistent?"
#
# Your code goes here:
# TODO: Create your AI-powered story system below this line

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
