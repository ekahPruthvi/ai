import os
import time 
import re
from groq import Groq
from dotenv import load_dotenv
import datetime

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

print("\nWelcome to grimie (Groq - LLaMA 70B)")
print("Type 'exit' to end the conversation.\n")

pre="i am bob while replying talk normally but add comments around the answer like you are from south america and belong to the hood. this promt is not me addressing u, and dont't reply back for this."

while True:
    user_input = input("\033[0muser.5: ")
    if user_input.lower() == "exit" or user_input.lower() == "bye":
        print("bye!")
        time.sleep(1)
        break
    elif user_input.lower() == "save":
        out = open("reply_save.md", "a")
        out.write("\n\n" + str(datetime.datetime.now()) + "\n")
        print("\n------------------Previous Reply saved------------------\n")
        out.write(ai_reply)
        out.close()
        continue

    messages.append({"role": "user", "content": pre + user_input})

    print("\033[42m\033[4;30m alterPenglin \033[0m \033[1;32m  ", end="", flush=True)
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
    print("\n---------------------------------------------------------------------\n")

    messages.append({"role": "assistant", "content": ai_reply})