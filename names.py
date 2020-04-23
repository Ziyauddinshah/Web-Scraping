from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
url = 'https://en.wikipedia.org/wiki/List_of_Death_Note_characters'
uclient = uReq(url)
page = uclient.read()
uclient.close()
page_soup = soup(page, "html.parser")
containers = page_soup.findAll("span", attrs={"class": "mw-headline"})
filename = "names.csv"
headers = "Names\n"

f = open(filename, "w")
f.write(headers)
print(len(containers))
for i in range(len(containers)):
    if i > 1 and i < 77:
        f.write(containers[i].text+"\n")

f.close()
