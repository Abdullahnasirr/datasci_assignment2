import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

#Downloads page
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

#gets title

page_title = soup.find("title").text.strip()
print("Page title:" + page_title)

#gets content
content_div = soup.find("div", id="mw-content-text")

#gets first 50 letterd

paragraphs = content_div.find_all("p")
for p in paragraphs:
    text = p.text.strip()
    if len(text) >= 50:
        print("First paragraph with 50+ characters:")
        print(text)
        break