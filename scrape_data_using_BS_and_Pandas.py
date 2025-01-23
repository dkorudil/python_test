from bs4 import BeautifulSoup #this module helps in web scraping
import requests #this module helps us to download a web page
import pandas as pd

#The below url contains html tables with data about world population.
url = "https://en.wikipedia.org/wiki/World_population"

# get the contents of the webpage in text format and store in a variable called data
data=requests.get(url).text
soup=BeautifulSoup(data,"html.parser")

#find all html tables in the web page
tables=soup.find_all('table') #tables are presented as <table> in html

#total amount of tables found
print(len(tables))

population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])


for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)

print(tables[table_index].prettify())

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if col != []:
        rank = col[0].text.strip()
        country = col[1].text.strip()
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        
        # Create a new DataFrame for the row
        new_row = pd.DataFrame([{
            "Rank": rank, 
            "Country": country, 
            "Population": population, 
            "Area": area, 
            "Density": density
        }])
        
        # Concatenate the new row with the existing DataFrame
        population_data = pd.concat([population_data, new_row], ignore_index=True)
print(population_data)