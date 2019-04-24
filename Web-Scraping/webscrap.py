from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

my_url='https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

# opening up connection, grabbing the page
uClient = uReq(my_url)

# offloads the content into a variable
page_html = uClient.read()

# close
uClient.close()

# html parsing
page_soup=soup(page_html, "html.parser")

# grab each product
containers=page_soup.findAll("div",{"class":"item-container"})
filename="products.csv"
f=open(filename,"w")
headers="Brand, Product_Name, Shipping"
f.write(headers)
for container in containers:
	brand =container.find("div", "item-branding").a.img["title"]

	title_container = container.findAll("a",{"class":"item-title"})

	product_name=title_container[0].text
	shipping_container=container.findAll("li",{"class":"price-ship"})
	shipping = shipping_container[0].text.strip()
	# price_container= container.find('span',{'class':'price-was-data'})
	# price=price_container.text

	print("Brand: " +brand)
	print("Product_Name: "+product_name)
	print("Shipping mode: "+ shipping)
	# print("price: "+ price)

	f.write(brand + "," +product_name.replace(",","|")+","+shipping+"\n")
	
f.close()	