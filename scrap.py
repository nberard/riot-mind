import bs4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

# Set path to ChromeDriver (Replace this with the correct path)
CHROMEDRIVER_PATH = "C:\\chromedriver-win64\\chromedriver.exe"

# Initialize WebDriver with Service
service = Service(CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()


options.add_argument("--window-size=1920,1080")  # Set window size


driver = webdriver.Chrome(service=service, options=options)

# Open Google Search URL
search_url = "https://op.gg/lol/summoners/euw/Touplitoui-EUW"

driver.get(search_url)

# Wait for the page to load
time.sleep(2)

page_html = driver.page_source
soup = bs4.BeautifulSoup(page_html, features="html.parser")

# print(page_html)
content = soup.select_one('#content-container')
print(content)
gap = content.find_all("div", {"class": "gap-3"})
print(gap)

exit()
with open('profile.template.html', 'w') as f:
    f.write(str(content))