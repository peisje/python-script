from bs4 import BeautifulSoup
import requests


# get url
url = input('Enter a URL (include `http://`): ')
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
print(html)

links = []
for i in soup.find_all("a",href= True):
    links.append(i)
    print("leitud link: ", i)

# print the number of links in the list
# print("\nFound {} links".format(len(links)))
# for email in emails:
#     print(email)
