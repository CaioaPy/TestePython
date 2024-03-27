import openai

openai.api_key = "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"

def chat(prompt):
    response = openai.ChatCompletion(
        model ="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat(user_input)
        print("Chatbot: ", response)
