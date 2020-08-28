import random
import requests
import json

response = requests.get(
        "http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en"
    )
response = json.loads(response.text)
quote = response["quoteText"]
author = response["quoteAuthor"] 

print(quote)
print(author)
