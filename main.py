
import pandas as pd
import time
import csv
from functions import *

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# driver = "C:\\\\chromedriver.exe"
url = "https://finance.yahoo.com/quote/PAYTM.NS/financials"


# Config

driver = webdriver.Chrome()
driver.get(url)
# driver.implicitly_wait(3)
print("Browsing for Site!")
time.sleep(3)

# end of Config

def expand():
    try:
        print("Clicking Expand Button if not already expanded!")
        global_expand_all_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                                        '//*[@id="Col1-1-Financials-Proxy"]/section/div[2]/button/div/span')))
        button_text = global_expand_all_btn.text
        print("Button Text: ", button_text)
        if str(button_text) != "Expand All":
            print("Columns Already Expanded!")
            pass
        else:
            print("Columns not expanded. Clicking Expand All!")
            global_expand_all_btn.click()

    except TimeoutException:
        print("Page Load Time Exceeded!")


# expand()


def getAllData():

    delay = 3


    print("Getting Yearly Income Statement!")
    expand()
    print("Waiting for data to load!")
    time.sleep(2)
    yearlyIncome = {}
    print("Getting Yearly Income Statement!")

    tableElements = driver.find_elements(by=By.CLASS_NAME, value='rw-expnded')
    for i in tableElements:
        particulars = i.text.splitlines()[0]
        values = i.text.splitlines()[1].replace(",", "").split(" ")
        yearlyIncome[particulars] = values



    print("Getting Quarterly Income Statement!")
    quarterlyIncome = {}

    delay = 3  # seconds
    try:
        quarterly_btn = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[1]/div[2]/button/div/span')))
        print("Yearly Income Statement Page is ready!")
        print("Clicking Quarterly Statement button!")
        quarterly_btn.click()
        time.sleep(2)
        expand()
        print("Waiting for data to load! ")
        time.sleep(2)

    except TimeoutException:
        print("Page Load Time Exceeded!")

    tableElements = driver.find_elements(by=By.CLASS_NAME, value='rw-expnded')
    for i in tableElements:
        particulars = i.text.splitlines()[0]
        values = i.text.splitlines()[1].replace(",", "").split(" ")
        quarterlyIncome[particulars] = values



    print("Getting Yearly Balance Sheet!")
    yearlyBalanceSheet = {}

    delay = 3  # seconds
    try:
        balance_sheet_button = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[1]/div[1]/div/div[2]/a/div/span')))
        print("Clicking Balance Sheet Button!")
        balance_sheet_button.click()
        time.sleep(2)
        expand()
        print("Waiting for data to load")
        time.sleep(2)
    except TimeoutException:
        print("Page Load Time Exceeded!")

    tableElements = driver.find_elements(by=By.CLASS_NAME, value='rw-expnded')
    for i in tableElements:
        particulars = i.text.splitlines()[0]
        values = i.text.splitlines()[1].replace(",", "").split(" ")
        yearlyBalanceSheet[particulars] = values



    print("Getting Yearly Cash Flow!")
    yearlyCashFlow = {}

    delay = 3  # seconds
    try:
        cash_flow_button = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/div/div[3]/a/div/span')))
        print("Clicking Cash Flow Button!")
        cash_flow_button.click()
        time.sleep(2)
        expand()
        print("Waiting for data to load")
        time.sleep(2)
    except TimeoutException:
        print("Page Load Time Exceeded!")

    tableElements = driver.find_elements(by=By.CLASS_NAME, value='rw-expnded')
    for i in tableElements:
        particulars = i.text.splitlines()[0]
        values = i.text.splitlines()[1].replace(",", "").split(" ")
        yearlyCashFlow[particulars] = values



    driver.close()

    return {
        "yearlyIncome": yearlyIncome,
        "quarterlyIncome": quarterlyIncome,
        "yearlyBalanceSheet": yearlyBalanceSheet,
        "yearlyCashFlow": yearlyCashFlow
    }




a = getAllData()
for title, data in a.items():
    toCSV(title=title, data=data)











