# _*_ coding: utf-8 _*_

from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.maximize_window()
driver.get("http://wsb.pl")

print (driver.title)

time.sleep(5)
driver.quit()
