import openai

openai.api_key = "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"

model_engine = "text-davinci-003"
prompt = "Hello, how are you today?"

completion = openai.Completion.create(
    engine = model_engine,
    prompt = prompt,
    max_tokens = 1024,
    n = 1,
    stop = None,
    temperature = 0.5
)

response = completion.choices[0].text
print(response )