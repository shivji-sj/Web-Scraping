# Project Name : scraping flipkart data 
import requests
from bs4 import BeautifulSoup
import pandas as pd
import  re


# scraping important things
item = []
price = []
description = []
rating = []

# print("Length of Items : ",len(item))
# print("Length of Price : ",len(price))
# print("Length of Description : ",len(description))
# print("Length of Rating : ",len(rating))

def scrape_data(url, page_no):
	for i in range(1,page_no+1):
		url = url+str(i)

		#request gt
		page = requests.get(url)

		# check response
		# if page.status_code == 200:print("Scrapable")
		# else:print("Not Scrapable")

		#parsing the html page
		soup = BeautifulSoup(page.text , "html.parser")

	######################################
		page = soup.find_all("div", class_="_4rR01T")
		for i in page:
			name = i.text
			item.append(name)
	######################################
		page = soup.find_all("div", class_="_30jeq3 _1_WHN1")
		for i in page:
			pr = i.text
			price.append(pr)
	######################################
		page = soup.find_all("ul", class_="_1xgFaf")
		for i in page:
			desc = i.text
			description.append(desc)
	######################################
		major_box = soup.find("div", class_= "_1YokD2 _3Mn1Gg")
		page = major_box.find_all("div", class_="_3LWZlK")
		for i in page:
			rt = i.text
			rating.append(rt)

scrape_data(url="https://www.flipkart.com/search?q=mobile+phone+under+10000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_19_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_19_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobile+phone+under+10000%7CMobiles&requestId=a429682e-1875-41cb-a17b-0e64f34bec7d&as-backfill=on", page_no=20)

# # creating empty dataframe
df = pd.DataFrame({"product Name": item,
				   "price": price,
				   "description":description,
				   "rating":rating}
				   )
# print(df)
# replacing rupee symbol to null character 
df["price"] = df["price"].replace(to_replace=r"₹", regex=True, value="")
# # saving file into excel
df.to_csv("flipkart_data_mobile_under_10000rs.csv")

print(df)
print("All columnns in dataframe : ", df.columns)