from bs4 import BeautifulSoup #this module helps in web scraping
import requests #this module helps us to download a web page

#Downloading the webpage
url = "https://web.archive.org/web/20230224123642/https://www.ibm.com/us-en/"
data=requests.get(url).text

#Create BeautifulSoup object
soup=BeautifulSoup(data, "html.parser")

#Scrape all links
for link in soup.find_all('a', href=True):  #in html anchor/link is presented by the tag <a>
    print(link.get('href'))
    
#Scrape all images tags
for link in soup.find_all('img'):  #in html images are presented by the tag <img>
    print(link)
    print(link.get('src'))


    
