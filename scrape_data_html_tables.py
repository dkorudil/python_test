#Scrape data from html tables

import requests
from bs4 import BeautifulSoup #this module helps in web scraping
import requests #this module helps us to download a web page

#The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

# get the contents of the webpage in text format and store in a variable called data
data=requests.get(url).text

#create Soup object
soup=BeautifulSoup(data, "html.parser")

#find a html table in the web page
table=soup.find('table') #in html tables are presented by <table>

#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))