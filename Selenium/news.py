import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:

    driver.get("https://news.ycombinator.com/")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.titleline a")))

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    links = driver.find_elements(By.CSS_SELECTOR, "span.titleline a")
    articles = [{'title': link.text.strip(), 'link': link.get_attribute('href')} for link in links]

    with open('hacker_news_articles.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)

    print("Данные успешно сохранены в файл 'hacker_news_articles.json'.")

finally:

    driver.quit()
