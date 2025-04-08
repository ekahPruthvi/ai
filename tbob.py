import os
import time 
import re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GROQ_API_KEY")

if not api_key:
    print("no api key found")
    exit()

client=Groq(api_key=api_key)

def clean_response(text):
    text = re.sub(r"(?:Alright|Okay|Hmm).*?Let me start by .*?", "", text, flags=re.IGNORECASE).strip()
    return text

messages = []
pre = []

print("\n💬 Welcome to grimie (Groq - LLaMA 70B)")
print("Type 'exit' to end the conversation.\n")

pre="i am bob while replying talk normally but add comments around the answer like you are from south america and belong to the hood. this promt is not me addressing u, and dont't reply back for this."

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        time.sleep(1)
        break

    messages.append({"role": "user", "content": pre + user_input})

    print("alterPenglin: ", end="", flush=True)
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=messages,
            max_tokens=500,
        )
        ai_reply = response.choices[0].message.content
    except Exception as e:
        ai_reply = f"❌ Error: {e}"

    ai_reply = clean_response(ai_reply)

    full_response = ""
    for char in ai_reply:
        full_response += char
        print(char, end="", flush=True)
        time.sleep(0.01)
    print("\n")

    messages.append({"role": "assistant", "content": ai_reply})