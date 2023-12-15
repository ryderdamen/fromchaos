from fromchaos import FromChaosList


context = """
This is a long string of data, it could be anything you like, plain text,
html, markdown, or something else like JSON.
"""

question = "Split this text when there is a comma"


# chaos = FromChaosList(question, context, model='gpt-3.5-turbo')
chaos = FromChaosList(question, context, model='gemini-pro')

print(chaos.response)
print(f'cost was {chaos.get_cost()}')
