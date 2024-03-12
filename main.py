
import pandas as pd
import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# driver = "C:\\\\chromedriver.exe"
url = "https://finance.yahoo.com/quote/PAYTM.NS/financials"

def getYearlyIncomeStatement(url: str):

    print("Getting Yearly Data!")

    driver = webdriver.Chrome()

    driver.get(url)
    yearlyIncome = {}

    delay = 3 # seconds
    try:
        expand_all_btn = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/button/div/span')))
        print ("Yearly Income Statement Page is ready!")
        time.sleep(1)
        print("Clicking Expand All button for full data! ")
        expand_all_btn.click()
        print("Waiting for data to load! ")
        time.sleep(1)

    except TimeoutException:
        print ("Page Load Time Exceeded!")


    # table = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[3]/div[1]/div/div[2]")
    tableElements = driver.find_elements(by=By.CLASS_NAME, value='rw-expnded')
    for i in tableElements:
        particulars = i.text.splitlines()[0]
        values = i.text.splitlines()[1].replace(",", "").split(" ")
        yearlyIncome[particulars] = values

    driver.close()
    driver.quit()
    return yearlyIncome


def getQuarterlyIncomeStatement(url: str):

    print("Getting Quarterly Data!")

    driver = webdriver.Chrome()

    driver.get(url)
    quarterlyIncome = {}

    delay = 3 # seconds
    try:
        quarterly_btn = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[1]/div[2]/button/div/span')))
        print("Yearly Income Statement Page is ready!")
        print("Clicking Quarterly Statement button!")
        quarterly_btn.click()
        print('Waiting for Quarterly Statement Page!')
        time.sleep(2)
        expand_all_btn = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/button/div/span')))
        print("Clicking Expand All button for full data! ")
        expand_all_btn.click()
        print("Waiting for data to load! ")
        time.sleep(1)

    except TimeoutException:
        print ("Page Load Time Exceeded!")


    # table = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[3]/div[1]/div/div[2]")
    tableElements = driver.find_elements(by=By.CLASS_NAME, value='rw-expnded')
    for i in tableElements:
        particulars = i.text.splitlines()[0]
        values = i.text.splitlines()[1].replace(",", "").split(" ")
        quarterlyIncome[particulars] = values

    driver.quit()
    return quarterlyIncome


print(getYearlyIncomeStatement(url))
time.sleep(1.5)
print(getQuarterlyIncomeStatement(url))







