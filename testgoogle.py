import chromedriver_binary # nopa
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv

# WebDriver のオプションを設定する
options = webdriver.ChromeOptions()
options.add_argument('--headless')

print('connectiong to remote browser...')
driver = webdriver.Chrome(options=options)

driver.get('https://www.google.co.jp/')
print(driver.current_url)

elem = driver.find_element(By.XPATH, '//input[@title="検索"]')
elem.send_keys("検索")
elem.send_keys(Keys.ENTER)
print(driver.current_url)

gelems = driver.find_elements(By.XPATH, '//div[@class="g"]')
print(gelems)
with open('test.csv','a',newline='', encoding='UTF-8') as f:
    cw = csv.writer(f, quoting=csv.QUOTE_ALL)

    for e in gelems:
        link = e.find_element(By.XPATH, 'div/div[@class="yuRUbf"]/a').get_attribute("href")
        print(link)
        text = e.find_element(By.XPATH, 'div/div[@class="yuRUbf"]//h3/span').text
        print(text)
        cw.writerow([link, text])

driver.quit()
