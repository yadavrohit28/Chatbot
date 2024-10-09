import openai
openai.api_key='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'
def chat_with_gpt(promt):
    response=openai.ChatCompletion.create(
        model="gemi",
        messages=[{"role":"user","content":promt}]
    )
    return response.choices[0].message.content.strip()
if __name__=="_main_":
    while True:
        user_input=input("you: ")
        if user_input.lower() in ["quit","exit","bye"]:
            break
        response =chat_with_gpt(user_input)
        print("chatbots:", response)
