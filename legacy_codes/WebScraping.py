import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Bhimavaram"

res = requests.get(url)
if res.status_code == 200:
    print(res.headers["Content-Type"])
    html_page = res.text
    soup = BeautifulSoup(html_page, "html.parser")

    print("Title: ", soup.title)
    print("First Unordered List: ", soup.ul)
    print("First Link: ", soup.a)
    print("Link Attributes: ", soup.a.attrs)
    print("Link Attributes Value: ", soup.a["href"])
    print("All Links: ", soup.find_all("a"))

