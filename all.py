#importing

from bs4 import BeautifulSoup
import requests
import pandas as pd

pages = ["http://books.toscrape.com/",
         "http://books.toscrape.com/catalogue/page-2.html",
         "http://books.toscrape.com/catalogue/page-3.html",
         "http://books.toscrape.com/catalogue/page-4.html",
         "http://books.toscrape.com/catalogue/page-5.html",
         "http://books.toscrape.com/catalogue/page-6.html"]
prices=[]
products=[]
ratings=[]
ident=[]
r=[]
#parsing
for i in pages:
    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(products)
#print(soup.prettify()) 
#class is 'col-xs-6 col-sm-4 col-md-3 col-lg-3'
#Now, we can use the find_all method to search for items by class or by id.
#In our case, we are looking for all li elements with this specific class.

    #def retrieve_first_product_price():
        #print(soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3'))
    for a in soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3'):
        product_price=a.find(class_="price_color")
        product_name=a.find('h3')
        product_rating=a.p['class']
        #print(product_rating)
        price=product_price.get_text().strip().strip('Â£')
        name=product_name.get_text()
        #rating=product_rating.strip().strip('star rating')
        #print(rating)
        prices.append(price)
        products.append(name)
        ratings.append(product_rating)
        #print(ratings)
    #print(products),  .strip().strip('$')
#print(products)
#print(prices)
    #product_one = all_products[0]
    #product_one_price = product_one.find(class_="price_color")
    #print(product_one_price)
    #try:
     #   print(product_price.get_text())
    #except AttributeError:
     #   print("none")

for i in range(0, len(prices)):
	ident.append(i)
#print(ident)
for i in range(0, len(ratings)):
    r.append(ratings[i][1])
#print(r)

for i in range(0, len(ratings)):
    if r[i]=='One':
        r[i]=1
    elif r[i]=='Two':
        r[i]=2
    elif r[i]=='Three':
        r[i]=3
    elif r[i]=='Four':
        r[i]=4
    elif r[i]=='Five':
        r[i]=5



df = pd.DataFrame({'id':ident,'Product Name':products,'Price':prices, 'Rating':r}) 
df.to_csv('all.csv', index=False, encoding='utf-8')

#if __name__ == '__main__':
    #retrieve_first_product_price()
