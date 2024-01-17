from pathlib import Path
import google.generativeai as genai

genai.configure(api_key="AIzaSyAzUsyadce88Rm8QQLjQStnUhP43b0evz4")

# Set up the model
generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}

safety_settings = []

model = genai.GenerativeModel(model_name="gemini-pro-vision",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Validate that an image is present
if not (img := Path("image0.jpeg")).exists():
    raise FileNotFoundError(f"Could not find image: {img}")

image_parts = [
    {
        "mime_type": "image/jpeg",
        "data": Path("image0.jpeg").read_bytes()
    },
]

previous_responses = []

while True:
    text = input("Enter next prompt:")
    
    # Include previous responses in the prompt
    prompt_parts = [
        image_parts[0],
        {"mime_type": "text/plain", "data": f"{text}"},  # Include the current input as text
    ] + previous_responses

    response = model.generate_content(prompt_parts)
    print(response.text)

    # Append the current response to previous_responses
    previous_responses.append({
        "mime_type": "text/plain",
        "data": response.text,
    })
