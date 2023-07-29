from fromchaos import FromChaosList

context = """
This is a long string of data, it could be anything you like, plain text,
html, markdown, or something else like JSON.
"""

question = "Split this text by comma"


chaos = FromChaosList(question, context, model='gpt-3.5-turbo')
print(chaos.response)
