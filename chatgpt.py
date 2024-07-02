import openai

openai.api_key = "sk-proj-iXxLR1Lko1rHYWOHcyljT3BlbkFJF3xTaritqx50xrtGOEBB"

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text