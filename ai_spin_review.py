import openai

openai.api_key = "your-openai-api-key"

def spin_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "You are an AI writer. Rewrite this content in a unique way."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

def review_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "You are an AI reviewer. Make small improvements and fix grammar."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

with open("chapter1.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

spun = spin_text(raw_text)
reviewed = review_text(spun)

with open("final_output.txt", "w", encoding="utf-8") as f:
    f.write(reviewed)

print("AI writing and review done.")