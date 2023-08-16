import requests
from bs4 import BeautifulSoup
import pandas

url = "https://www.reddit.com/r/programming/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
soup.prettify()

posts = soup.find_all('shreddit-post')

postInfos = []

for post in posts[:3]:
    title = post.get('post-title')
    upvotes = post.get('score')
    link = post.get('content-href')
    postInfos.append([title, upvotes, link])

dataFrame = pandas.DataFrame(postInfos, columns=["Title", "Upvotes", "Link"])

dataFrame.to_excel("posts_reddit.xlsx", index=False)

print("Arquivo gerado!")