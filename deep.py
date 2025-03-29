from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)
def chat_ai(prompt):
    completion = client.chat.completions.create(
    model="deepseek/deepseek-chat-v3-0324:free",
    messages=[
        {
        "role": "user",
        "content": prompt
        }
    ],
    stream=False
    )
    return(completion.choices[0].message.content)

while True:
        user_input=input("You: ")
        if user_input.lower()in["bye","goodbye","end","exit"]:
            print("ChatBot: Goodbye")
            break
        message=chat_ai(user_input)
        print("ChatBot: ", message)