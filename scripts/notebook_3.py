import nbformat as nbf

# Create a new notebook
nb = nbf.v4.new_notebook()

# Define the content for each cell
cells = [
    nbf.v4.new_markdown_cell(
        """
# 🖥️ Build an AI-Powered Python App with a User Interface

## Introduction
- In this series of exercises, you'll learn how to 
    - make LLM API calls via Together.AI.
    - create user interfaces for AI applications using Gradio
- We'll combine the power of Gradio's simple UI components with large language models to build interactive AI applications.
- Each section includes a **Try This** explanation followed by a **Task** for you to complete.

## Submission Instructions
- Perform Exercise 5 at the end of the notebook and share your demo with the group.
"""
    ),
    nbf.v4.new_markdown_cell(
        """
To get started, we'll need to an api key from Together.AI. 

Sign up here https://together.ai/ and you will get a free dollar to start experimenting with their API. 

They have many models to choose from such as DeepSeek, Qwen and Flux, but we'll be using the meta-llama/Meta-Llama-3-8B-Instruct-Lite model.

Once you have your api key, you can paste it into the cell below.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your Together.ai API Key Here
your_api_key = ""
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## 👀 Define a Function for Prompting LLaMA 🦙

### 📝 What does this cell do?
- Installs the Together library
- This code creates two functions for us that makes it easy for us to interact with Llama.
- Llama is a large language model much like ChatGPT
"""
    ),
    nbf.v4.new_code_cell(
        """
# import libraries
import requests
from PIL import Image

try:
    from together import Together
    
except ImportError:
    !pip install -q together

# Get Client
your_api_key = "9806a2601560024637df1e4acd804862faa67e08637db6598d920b64eebba43e"
client = Together(api_key=your_api_key)

def prompt_llm(prompt, show_cost=False):
    # This function allows us to prompt an LLM via the Together API
    
    # Calculate the number of tokens
    tokens = len(prompt.split())
    
    # Get pricing information from Together API
    models = client.models.list()
    pricing = {}
    for model in models:
        if hasattr(model, 'pricing') and model.pricing:
            # Convert to per million tokens
            pricing[model.name] = model.pricing.input_price_per_token * 1_000_000  
    
    # Calculate and print estimated cost for each model
    if show_cost:
        print(f"Number of tokens: {tokens}")
        for model, price in pricing.items():
            cost = (price / 1_000_000) * tokens
        print(f"Estimated cost for {model}: ${cost:.10f}")
    
    # Make the API call
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3-8B-Instruct-Lite",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content

def gen_image(prompt, width=256, height=256):
    # This function allows us to generate images from a prompt
    response = client.images.generate(
        prompt=prompt,
        model="stabilityai/stable-diffusion-xl-base-1.0",  # Using a supported model
        steps=30,
        n=1,
    )
    image_url = response.data[0].url
    image_filename = "image.png"

    # Download the image using requests instead of wget
    response = requests.get(image_url)
    with open(image_filename, "wb") as f:
        f.write(response.content)
    img = Image.open(image_filename)
    img = img.resize((height, width))

    return img

print("LLM Ready!")
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## **Exercise 1: Using Together.AI with LLaMA 🦙**  
### **👀 Try this first!**  
_(Press **Shift + Enter** to test the AI response!)_  
📝 **What does this cell do?**  
It asks **LLaMA** a question about Python for AI development.  

This exercise introduces you to the basics of interacting with a language model using API calls. You'll learn how to send a prompt to the model and receive a response, which is a fundamental skill for leveraging AI in applications.

Task Modify the prompt to ask the AI about something completely unrelated to Python (e.g., **travel tips, cooking, history, or music**).
"""
    ),
    nbf.v4.new_code_cell(
        '''
response = prompt_llm("""
What are the key benefits of learning Python for AI development?

in 3 bullet points one sentence each
""")
print(response)
'''
    ),
    nbf.v4.new_markdown_cell(
        """
## **Task 1: Modify the Prompt**
Ask the AI about something completely unrelated to Python (e.g., **travel tips, cooking, history, or music**).  
"""
    ),
    nbf.v4.new_code_cell(
        """
Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## **Exercise 2: Generate Image with Flux**  
### **👀 Try this first!**  
_(Press **Shift + Enter** to generate an image using Flux!)_  
📝 **What does this cell do?**  
It uses the Together.AI API to generate an image based on a given prompt.  

This exercise demonstrates how to interact with the Together.AI API to create images. 
You'll learn how to send a prompt to the model and receive an image in response, which is a fundamental skill for 
leveraging AI in creative applications.
"""
    ),
    nbf.v4.new_code_cell(
        """
img = gen_image(prompt="crazy rabbit with a sword", width=256, height=256)
img.show()
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## **Task 2: Modify the Prompt to generate an image**
Ask the AI to generate an image with a **different style** (e.g., a cartoon, a painting, a photo, etc.).  
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your Code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## **Exercise 3: Create your own Chatbot with Gradio🤖**  
### **👀 Try this first!**  
_(Press **Shift + Enter** to create your own chatbot with Gradio!)_  
📝 **What does this cell do?**  
It guides you through creating a chatbot using Gradio.  

Creating a chatbot with Gradio is an essential skill for building interactive AI applications. 
This exercise demonstrates how to set up a chatbot interface, which is useful for engaging users in conversational AI experiences.

Modify
"""
    ),
    nbf.v4.new_code_cell(
        """
        def chat_interface(user_message, chat_history):
    # Generate a response
    response = "Hello I am a naive bot"
  
    chat_history.append((user_message, response))
    return "", chat_history, None


with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown("## 🤖 AI Chatbot")
    gr.Markdown("Enter your message below and let the chatbot respond!")

    chatbot = gr.Chatbot()
    image_output = gr.Image(label="Generated Image")
    user_input = gr.Textbox(
        placeholder="Type your message here...", label="Your Message"
    )
    send_button = gr.Button("Send")

    send_button.click(
        chat_interface,
        inputs=[user_input, chatbot],
        outputs=[user_input, chatbot, image_output],
    )
    user_input.submit(
        chat_interface,
        inputs=[user_input, chatbot],
        outputs=[user_input, chatbot, image_output],
    )

app.launch()
        """
    ),
    nbf.v4.new_markdown_cell(
        """
## **Exercise 4: Add AI to your Chatbot with Gradio🤖**  
### **👀 Try this first!**  
_(Press **Shift + Enter** to create your own chatbot with Gradio!)_  
📝 **What does this cell do?**  
It guides you through creating a chatbot using Gradio.  

Creating a chatbot with Gradio is an essential skill for building interactive AI applications. 
This exercise demonstrates how to set up a chatbot interface, which is useful for engaging users in conversational AI experiences.
"""
    ),
    nbf.v4.new_code_cell(
        '''
    chapter = "erwerwer"
    # First generate text response
    chatbot_prompt = f"""
    You are a senior singer who gives advice to new singers

    respond to this {user_message} following these instructions:
    * be very concise
    * always start with ahhhhhhh
    * then sing something after your advice
    * Ground all your answers based on this {chapter}
    
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3-8B-Instruct-Lite",
        messages=[{"role": "user", "content": chatbot_prompt}],
    )
    response = response.choices[0].message.content

    # Generate image based on the response
    image_prompt = f"A {response} in a pop art style"
    image = get_image(image_prompt)
    chat_history.append((user_message, response))
    return "", chat_history, image


with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown("## 🤖 AI Chatbot")
    gr.Markdown("Enter your message below and let the chatbot respond!")

    chatbot = gr.Chatbot()
    image_output = gr.Image(label="Generated Image")
    user_input = gr.Textbox(
        placeholder="Type your message here...", label="Your Message"
    )
    send_button = gr.Button("Send")

    send_button.click(
        chat_interface,
        inputs=[user_input, chatbot],
        outputs=[user_input, chatbot, image_output],
    )
    user_input.submit(
        chat_interface,
        inputs=[user_input, chatbot],
        outputs=[user_input, chatbot, image_output],
    )

app.launch()
'''
    ),
    nbf.v4.new_markdown_cell(
        """
## **Your Project Here**
Modify the following code below to create your own specialized Chatbot
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here for Project 1
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Challenge
Create a video of your Chatbot running for 10-60 seconds and share it as a demowith the group.

## 🎉 Congratulations! 🎉
You've successfully created an AI-powered Python application with a user-friendly interface!
"""
    ),
]

# Assign cells to the notebook
nb.cells.extend(cells)

# Save the notebook
with open("ai_chatbot.ipynb", "w") as f:
    nbf.write(nb, f)
