import openai 

openai.api_key = 'Replace_your_api_key'

def chat_completion():
    response = openai.Completion.create(
        engine='gpt-3.5.turbo',
        prompt='prompt',
        max_tokens=100,
        temparature=0.7,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

chat_prompt = "what is the meaning of life?"
completion = chat_completion(chat_prompt)
print(completion)