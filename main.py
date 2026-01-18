    # print(article["description"])
    # print(article["title"])

send_email(message=body)
body = body.encode("utf-8")

        body = body + article["title"] + "\n" + article["description"] + 2*"\n"
    if article["title"] is not None:
for article in content["articles"]:
body = ""
# Access the article, titles and description

content = req.json()
# Get a dictionary with data

req = requests.get(url)
# Make request

       "&apiKey=53357419416049389c34875c7def7bc5")
       "&sortBy=publishedAt"
       "&from=2025-12-18"
       "q=tesla"
url = ("https://newsapi.org/v2/everything?"
api_key = "53357419416049389c34875c7def7bc5"

from send_email import send_email
import requests