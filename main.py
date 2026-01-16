import requests

api_key = "53357419416049389c34875c7def7bc5"
url = ("https://newsapi.org/v2/everything?q=tesla"
       "&from=2025-12-16&sortBy=publishedAt&apiKey"
       "=53357419416049389c34875c7def7bc5")

# Make request
req = requests.get(url)

# Get a dictionary with data
content = req.json()

# Access the article, titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])