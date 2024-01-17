from pathlib import Path
import google.generativeai as genai
genai.configure(api_key="AIzaSyAzUsyadce88Rm8QQLjQStnUhP43b0evz4")
generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 32,
  "max_output_tokens": 4096,
}
safety_settings = []
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
while 1:
    text=input("Enter Your Text:")
    response = chat.send_message(text)
    for chunk in response:
        print(chunk.text)
        print("_"*80)