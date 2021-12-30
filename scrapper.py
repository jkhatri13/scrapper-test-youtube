import requests
from bs4 import BeautifulSoup

TARGET_URL = "https://www.gst.gov.in"

response = requests.get(TARGET_URL)

print('status code', response.status_code)

with open('trending.html','w') as f: f.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser')

print('Page Title ', doc.title)

