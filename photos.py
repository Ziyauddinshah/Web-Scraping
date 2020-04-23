from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
import os
import requests
import urllib
if not os.path.exists("deathnote"):
    os.makedirs("deathnote")


def imagedownload(links):
    next = "https://en.wikipedia.org/"+links["href"]
    url = req(next)
    page2_soup = url.read()
    url.close()
    page2 = soup(page2_soup, "html.parser")
    img = page2.findAll('img')
    for l in range(len(img)):
        x = "https:"+img[l]["src"]
        # print(x)
        # https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Light_from_Death_Note.jpg/220px-Light_from_Death_Note.jpg
        # image_data=requests.get(x).content
        # with open("deathnote/",'wb') as handler:
        # handler.write(image_data)
        try:
            urllib.request.urlretrieve(x, "deathnote/"+str(l)+".png")
            urllib.request.urlretrieve(x, "deathnote/"+str(l)+".jpg")
        except:
            pass


url = req('https://en.wikipedia.org/wiki/List_of_Death_Note_characters')
page_soup = url.read()
url.close()
page = soup(page_soup, "html.parser")
link = page.findAll("a", attrs={"title": "Light Yagami"})
links = link[0]
imagedownload(links)
link = page.findAll("a", attrs={"title": "Japanese idol"})
links = link[0]
imagedownload(links)
link = page.findAll("a", attrs={"title": "Criminal prosecutor"})
links = link[0]
imagedownload(links)
