from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.imdb.com/chart/top/')

name_films = driver.find_elements(By.CSS_SELECTOR, 'div.ipc-title a.ipc-title-link-wrapper h3')
rating_elements = driver.find_elements(By.CSS_SELECTOR, 'span.ipc-rating-star--imdb')


titles = [element.text for element in name_films]
rating = [element.text for element in rating_elements]

for i in range(10):
    print("Рейтинг {}: {} ({}) ".format(i + 1, titles[i], rating[i]))

driver.quit()
