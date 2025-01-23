from bs4 import BeautifulSoup #this module helps in web scraping
import requests #this module helps us to download a web page

#Storing the link under the object "html"
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

#Creating soup object out of "html". html5lib is the parser
soup=BeautifulSoup(html, "html.parser")

#built in "prettify" displays the nested "html"
print(soup.prettify())

#Retrive the title and display
tag_object=soup.title
print("tag_object:", tag_object)

#Check the tag type
print("tag_type:", type(tag_object))

#Incase there is more than one Tag with the same name, first element is called
tag_object=soup.h3
print(tag_object)

#Accessing the tag children
tag_child=tag_object.b
print(tag_child)

#Accessing the Parent(identical to tag_object in this case)
parent_tag=tag_child.parent
print(parent_tag)

#Accesing under tag_object
sibling_1=tag_object.next_sibling
print(sibling_1)

#tag id type
print(tag_child['id'])
#or
print(tag_child.attrs)
#or
print(tag_child.get('id'))

#Tag displayed without any extra text - just the name of the player. It is called NavigableString by BeautifulSoup.
tag_string=tag_child.string
print(tag_string)

#type of tag string
print(type(tag_string))

#Turn NavigableString object into Unicode string
unicode_string=str(tag_string)
print(unicode_string)

#FILTER
#storing the table
table="<table><tr><td id='flight' >Flight No</td><td>Launch site</td><td>Payload mass</td></tr><tr><td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a> </td><td>80 kg</td></tr></table>"

table_bs=BeautifulSoup(table, "html.parser")
print(table_bs)

#find_all
table_rows=table_bs.find_all('tr')
print(table_rows)

#iterate through rows - 
for i, row in enumerate(table_rows):
    print("row",i,"is",row)
    
#As row is a cell object, we can apply the method find_all to it and extract table cells in the object cells using the tag td, this is all the children with the name td. 
#The result is a list, each element corresponds to a cell and is a Tag object, we can iterate through this list as well. 
#We can extract the content using the string attribute.

for i, row in enumerate(table_rows):
    print("row", i)
    cells=row.find_all('td')
    for j, cell in enumerate(cells):
        print('column',j,"cells",cell)  
    
#Downloading and scraping
