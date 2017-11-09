# -*- coding: UTF-8 -*-
'自动化测试，模拟浏览器登录'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
CHROME_DRIVER="d:/driver/chromedriver.exe";
def no01():
    browser = webdriver.Chrome(CHROME_DRIVER)
    browser.get('http://www.baidu.com/')
def no02():
    driver = webdriver.Chrome(CHROME_DRIVER)
    #隐式等待，设置一个等待时间
    driver.implicitly_wait(10) # seconds
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    print driver.page_source

def no03():
    driver = webdriver.Chrome(CHROME_DRIVER)
    #显式等待
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID,'someid')))
    driver.get("http://www.python.org")
    driver.quit()
no02()