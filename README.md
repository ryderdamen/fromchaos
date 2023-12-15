# From Chaos
A python library for extracting organized data out of chaos using large-language-models (LLMs) like ChatGPT and Gemini-Pro.


## Installation
To install, use the following command:
```bash
pip install fromchaos
```

In order to use FromChaos, you must have the following environment variable set in the environment where your script is running:

```
OPENAI_API_KEY="<<your-openai-api-key-here>>"
```

## Using FromChaos
FromChaos uses ChatGPT as its primary LLM (though others could be incorporated if desired). It accepts at its most basic level a question (about the data you want to get back), and the context (where to extract the value from).

Depending on your use-case, there are different classes of FromChaos to use. The following are code examples.

---


### FromChaosList - Parsing Data To A List
With a block of text, using FromChaosList you can extract values as a python list.

```python
from fromchaos import FromChaosList

context = """
This is a long string of data, it could be anything you like, plain text,
html, markdown, or something else like JSON.
"""

question = "Identify all data types that are mentioned"

try:
    chaos = FromChaosList(question, context, model='gpt-4')
    print(chaos.response)
except Exception:
    print('An error occured')

```

The response is a python list object, or an exception is thrown.
```
[
    "plain text",
    "html",
    "markdown",
    "json"
]
```

---

### FromChaosShortString - Short Strings
For a quick summary of something, use the FromChaosShortString class.


```python
from fromchaos import FromChaosShortString

context = """
Some very large text that talks about a variety of different things. Canada is a really big country. Australia is also big, but there are spiders. Italy has very good food. There's really good beef noodle soup in Taiwan.
"""

question = "Summarize what is talked about in these paragraphs."

try:
    chaos = FromChaosShortString(question, context, model='gpt-4')
    print(chaos.response)
except Exception:
    print('An error occured')

```

The response is a short python string.
```
The text talks about various characteristics of Canada, Australia, Italy, and Taiwan.
```


---

### FromChaosBoolOrNone - True/False, or None values
For classifying something as either True, False, or None, use the FromChaosBoolOrNone class.

```python
from fromchaos import FromChaosBoolOrNone

context = """
Some very large text that talks about a variety of different things. Canada is a really big country. Australia is also big, but there are spiders. Italy has very good food. There's really good beef noodle soup in Taiwan.
"""

question = "Is the united states mentioned in this paragraph?."

try:
    chaos = FromChaosBoolOrNone(question, context, model='gpt-4')
    print(chaos.response)
except Exception:
    print('An error occured')

```

The response is a boolean object, or Nonetype.
```
False
```


---

### FromChaosParagraph - Get a paragraph of text
FromChaosParagraph works similar to FromChaosShortString, except instead of a succinct response, it allows the model to elaborate for a little bit for a longer response.


```python
from fromchaos import FromChaosParagraph

context = """
The working holiday visa is valid for 12 months and it cannot be renewed. Applicants must show proof of funds. To apply, visit the consolate and pay the application fee of $65 CAD, then wait 3 weeks.
"""

question = "Summarize this visa."

try:
    chaos = FromChaosParagraph(question, context, model='gpt-4', max_chars=2000)
    print(chaos.response)
except Exception:
    print('An error occured')

```

The response is returned as a long string of text, or an exception is thrown
```
This visa is a working-holiday visa, with a validity of 12 months. This visa is non-renewable. For those interested in applying, proof of sufficient funds must be shown, and the consulate must be visited. An application fee of $65 CAD will apply, and a 3-week waiting period will be required.
```


---

### FromChaosDict - Getting a dictionary
FromChaosDict allows you to pass in a dictionary of your choosing as a sample object, and get the response in the same format.

```python
from fromchaos import FromChaosDict

context = """
The working holiday visa is valid for 12 months and it cannot be renewed. Applicants must show proof of funds. To apply, visit the consolate and pay the application fee of $65 CAD, then wait 3 weeks.
"""

question = "What is the fee, if any, for applying to this visa?."

sample_obj = {
    'amount': 400,
    'currency': 'USD'
}

try:
    chaos = FromChaosDict(question, context, sample_obj=sample_obj, model='gpt-4')
    print(chaos.response)
except Exception:
    print('An error occured')

```

The response is returned as a python dictionary, or an exception is thrown
```
{
    "amount": 65,
    "currency": "CAD"
}
```
