import pandas as pd
import requests 
from bs4 import BeautifulSoup

response = requests.get("https://d23.com/list-of-disney-films/")
html_string = response.text
print(html_string)

    