from openai import OpenAI

client = OpenAI(
    api_key="sk-mnopqrstijkl5678mnopqrstijkl5678mnopqrst"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messeges=[
        {"role":"system","content":"You Are The Virtual Assistance like Alexa and google."},
        {"role":"user","content":"What is Coding"}
    ]
)

print(completion.choices[0].messege.content)