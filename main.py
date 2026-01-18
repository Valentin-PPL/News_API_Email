import requests
from send_email import send_email

api_key = "53357419416049389c34875c7def7bc5"
url = ("https://newsapi.org/v2/everything?"
       "q=tesla"
       "&from=2025-12-18"
       "&sortBy=publishedAt"
       "&apiKey=53357419416049389c34875c7def7bc5")

# Make request
req = requests.get(url)

# Get a dictionary with data
content = req.json()

# Access the article, titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)

    # print(article["title"])
    # print(article["description"])