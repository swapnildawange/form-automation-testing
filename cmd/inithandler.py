import time
from models.model import URL
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def start():
    try:
        driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()))
        driver.get(URL)
        time.sleep(1)
        return driver
    except Exception as e:
        print(e)
