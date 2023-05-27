from selenium import webdriver
import json
from selenium.webdriver.common.by import By
import csv
import time

items=[]
driver=webdriver.Chrome("C:/Users/alina/Downloads/chromedriver_win32")
driver.get('https://www.youtube.com/watch?v=iFPMz36std4')
driver.execute_script('window.scrollTo(1, 500);')
#now wait let load the comments
time.sleep(5)
q = 0
while q < 12:
    time.sleep(1)
    q += 1
    driver.execute_script(f'window.scrollTo(1, {q * 3000});')

time.sleep(4)
username_elems = driver.find_elements(By.XPATH, '//*[@id="author-text"]')
comment_elems = driver.find_elements(By.XPATH, '//*[@id="content-text"]')

for username, comment in zip(username_elems, comment_elems):
    item = {}
    item['Author'] = username.text
    item['Comment'] = comment.text
    items.append(item)

with open('C:\PYTHON PROJECT\python selenium practic\commentlist.json', 'w', newline='', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False)
    