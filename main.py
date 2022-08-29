import time

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# global driver variable
driver = None


def start():
    form = driver.find_element(By.TAG_NAME, "form")
    inputs = getInputElements(form)
    attributes = []
    for i in inputs:
        attr = getAttributes(i)
        attributes.append(attr)
    print(attributes)
    saveFile(attributes)


if __name__ == "__main__":
    pass
    # driver = webdriver.Chrome(service=Service(
    #     ChromeDriverManager().install()))
    # driver.get(
    #     'https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
    # time.sleep(1)
    # start()
