#importing

from bs4 import BeautifulSoup
import requests
import pandas as pd

pages = ["http://books.toscrape.com/",
         "http://books.toscrape.com/catalogue/page-2.html",
         "http://books.toscrape.com/catalogue/page-3.html"]
prices=[]
products=[]
ident=[]
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
        #print(product_name)
        price=product_price.get_text().strip().strip('Â£')
        name=product_name.get_text()
        prices.append(price)
        products.append(name)
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
print(ident)
     
     
df = pd.DataFrame({'id':ident,'Product Name':products,'Price':prices}) 
df.to_csv('allproducts.csv', index=False, encoding='utf-8')

#if __name__ == '__main__':
    #retrieve_first_product_price()
