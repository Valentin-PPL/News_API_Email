import requests
from send_email import send_email

topic = input("Enter topic: ")

api_key = "53357419416049389c34875c7def7bc5"
url = ("https://newsapi.org/v2/everything?"
       f'q="{topic}"&'
       "from=2025-12-18&"
       "sortBy=publishedAt&"
       "apiKey=53357419416049389c34875c7def7bc5&"
       "language=en")

# Make request
req = requests.get(url)

# Get a dictionary with data
content = req.json()

# Construim corpul emailului ca text, nu bytes
body = "Today's news\n\n"

# Verificăm că există articole
articles = content.get("articles", [])

for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

send_email(body)

    # print(article["title"])
    # print(article["description"])