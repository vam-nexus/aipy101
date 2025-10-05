"""
Concept: Smart Story

This example demonstrates LLM integration for dynamic story generation.
Students will learn about API calls, environment variables, and AI-powered content creation.
"""

# Task 7 - Smart Story (Example File)
# This file demonstrates LLM integration for dynamic story generation

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


# Basic LLM interaction
if __name__ == "__main__":
    ### Task 1: YOUR CODE HERE - Write a prompt for the LLM to respond to the user
    prompt = "what are the tourist attractions in morocco?"

    # Get Response
    response = prompt_llm(prompt)

    print("\nResponse:\n")
    print(response)
    print("-" * 100)

    # save response under results/
    with open("results/response.txt", "w") as f:
        f.write(response)

# Interactive story with LLM (Uncomment Below)
# -------------------------------------------
# def smart_story():
#     """Create an interactive story using LLM"""
#     print("=== AI-Powered Story Generator ===")
#
#     # Get user input
#     name = input("What's your character's name? ")
#     setting = input("What setting do you want? (e.g., 'space', 'medieval', 'modern') ")
#
#     # Create a prompt for the LLM
#     story_prompt = f"""
#     Create a short interactive story about a character named {name} in a {setting} setting.
#     The story should be engaging and include some adventure elements.
#     Keep it to about 3-4 paragraphs.
#     """
#
#     print("\nGenerating your story...")
#     story = prompt_llm(story_prompt, with_linebreak=True)
#
#     print("\n" + "="*50)
#     print("YOUR STORY:")
#     print("="*50)
#     print(story)
#
#     # Save the story
#     with open("results/generated_story.txt", "w") as f:
#         f.write(f"Character: {name}\n")
#         f.write(f"Setting: {setting}\n")
#         f.write(f"Story:\n{story}")
#
#     print(f"\nStory saved to 'results/generated_story.txt'")

# smart_story()

# Dynamic story continuation (Uncomment Below)
# -------------------------------------------
# def continuing_story():
#     """Create a story that continues based on user choices"""
#     print("=== Dynamic Story Continuation ===")
#
#     # Initial story setup
#     setup_prompt = """
#     Create the beginning of an adventure story. Include:
#     1. A main character introduction
#     2. A problem or quest they need to solve
#     3. Two clear choices they can make
#     Keep it to 2-3 paragraphs and end with "What do you choose: A or B?"
#     """
#
#     print("Generating story beginning...")
#     story_beginning = prompt_llm(setup_prompt, with_linebreak=True)
#     print("\n" + story_beginning)
#
#     # Get user choice
#     choice = input("\nYour choice (A or B): ").upper()
#
#     # Generate continuation based on choice
#     continuation_prompt = f"""
#     Continue the story based on the user choosing option {choice}.
#     Make it exciting and include the consequences of their choice.
#     End with another choice: "What do you choose: A or B?"
#     Keep it to 2-3 paragraphs.
#     """
#
#     print("\nGenerating story continuation...")
#     story_continuation = prompt_llm(continuation_prompt, with_linebreak=True)
#     print("\n" + story_continuation)
#
#     # Save the full story
#     full_story = story_beginning + "\n\n" + story_continuation
#     with open("results/continuing_story.txt", "w") as f:
#         f.write(f"Choice made: {choice}\n\n")
#         f.write(full_story)
#
#     print(f"\nFull story saved to 'results/continuing_story.txt'")

# continuing_story()
