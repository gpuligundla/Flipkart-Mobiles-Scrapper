import requests
from bs4 import BeautifulSoup
import csv
import pandas

url = "https://www.flipkart.com/search?q=mobiles" 

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

mobile_names = soup.find_all('div', class_='_4rR01T')

mobile_rating = soup.find_all('div', class_='_3LWZlK')

mobile_price = soup.find_all('div', class_='_30jeq3 _1_WHN1')

MobileNames = []
MobileRating = []
MobilePrice = []

for names, rating, price in zip(mobile_names, mobile_rating, mobile_price):
    MobileNames.append(names.text)
    MobileRating.append(rating.text)
    MobilePrice.append(price.text)

model = pandas.DataFrame(data={'names': MobileNames, 'ratings': MobileRating, 'prices': MobilePrice})

model.to_csv('mobileslist.csv')
