import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

response = requests.get(url)

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

content_div = soup.find("div", id="mw-content-text")

#Gets all the headings inside the main content from above
h2_tags = content_div.find_all("h2")

exclude_words = {"references", "external links", "see also", "notes"}

headings = []

for h2 in h2_tags:
    headline_span = h2.find("span", class_="mw-headline")

    if headline_span:
        heading_text = headline_span.get_text(strip=True)
    else:
        heading_text = h2.get_text(" ", strip=True).replace("[edit]", "").strip()


    if not heading_text:
        continue

    #gets rid of unwanted headlines
    if any(word in heading_text.lower() for word in exclude_words):
        continue

    headings.append(heading_text)

#Saves to headings.txt and makes itone heading per line
with open("headings.txt", "w", encoding="utf-8") as f:
    for heading in headings:
        f.write(heading + "\n")

print(f"Saved {len(headings)} headings to headings.txt")
