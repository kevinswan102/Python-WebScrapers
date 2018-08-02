from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url='https://www.bodybuilding.com/store/top50.htm'

#opening the connection, grabbing the page
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

#parse as html file
page_soup = soup(page_html, "html.parser")
#grab all product information
containers = page_soup.findAll("div",{"class":"top10__product-inner"})

#writing information to a csv file
filename="supplements.csv"
f = open(filename, "w")
headers = "Product, Product Brand, Product Rating, Product Size\n"
f.write(headers)

#loops through top 50 products collecting the product name, brand, and special sale
for container in containers:
	product = container.a["title"]

	#stores all information about the brand in a container
	brand_container = container.findAll("div", {"class":"product__brand"})
	#holds only the product brand and strips whitespace
	product_brand = brand_container[0].text.strip()

	rating_container = container.findAll("div", {"class":"product__rating-n-view-product"})
	product_rating = rating_container[0].div.span.text.strip()

	sale_container = container.findAll("span", {"class":"vio-text vio-text--vio-green product__vio-text"})
	
	#check if there is a sale or not (empty box)
	if sale_container:
		product_sale = sale_container[0].text.strip()
	else: 
		product_sale = 'Unavailable'

	print("Product: " + product)
	print("Brand: " + product_brand)
	print("Rating: " + product_rating)
	print("Sale: " + product_sale)

	f.write(product + ", " + product_brand + ", " + product_rating + ", "  +  product_sale + "\n")

f.close()