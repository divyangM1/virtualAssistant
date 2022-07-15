from selenium import webdriver
import pyautogui as pg
import time

from selenium.webdriver.firefox.webdriver import WebDriver
web = webdriver.Firefox()
web.get("https://www.facebook.com")
search = "Aditya Pandey"
num = web.find_element_by_xpath('//*[@id="email"]')
num.send_keys('xxxxx646xx')
ps = web.find_element_by_xpath('//*[@id="pass"]')
ps.send_keys('***pass***')
pg.press("enter")
time.sleep(10)
stockSearch = web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/label/input')
stockSearch.send_keys(search)
time.sleep(5)
pg.press("enter")
time.sleep(4)
web.find_element_by_css_selector('.o7dlgrpb > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(1) > span:nth-child(1) > span:nth-child(1) > span:nth-child(1) > a:nth-child(1) > span:nth-child(1)').click()
time.sleep(5)
web.find_element_by_css_selector('div.jgsskzai:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1) > span:nth-child(1)').click()
time.sleep(1)
pg.typewrite("Hello")
time.sleep(1)
pg.press("enter")   
