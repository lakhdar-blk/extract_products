import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

url     = "https://www.jumia.dz/"
result  = requests.get(url)
src     = result.content
soup    = BeautifulSoup(src, "lxml")



#==getting elements==#
products    = soup.find_all("div", {'class': 'name'})
prices      = soup.find_all("div", {'class': 'prc'})
links       = soup.find_all("a", {'class': 'core'})
#====================#

products_list   = []
prices_list     = []
links_lists     = []
fiches_list     = []


#the same list len
for i in range(len(products)):
    products_list.append(products[i].text)
    prices_list.append(prices[i].text)
    links_lists.append(links[i].attrs['href'])


for link in links_lists:
    result      = requests.get("https://www.jumia.dz/"+link)
    src         = result.content
    soup        = BeautifulSoup(src, "lxml")
    fiches_tech = soup.find("div", {'class': 'markup -pam'})
    fiches_list.append(fiches_tech.text)



file_lists = [products_list, prices_list, links_lists, fiches_list]
exported = zip_longest(*file_lists)

#strip() is used to remove spaces in strings

with open("/home/lakhdar/Desktop/jumia_info.csv", "w") as myfrile:
    wr = csv.writer(myfrile)
    wr.writerow(["product", "price", "link", "Fiche technique"])
    wr.writerows(exported)
