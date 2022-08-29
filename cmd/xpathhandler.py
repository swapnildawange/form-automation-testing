
import time
from bs4 import BeautifulSoup
from utils.xpathUtils import Xpath_Util
from elements.elements import Elements
def init_xpath(driver):
    xpath_obj = Xpath_Util(driver)
    elements_obj = Elements(driver)
    #Parsing the HTML page with BeautifulSoup
    page = driver.execute_script("return document.body.innerHTML").\
    encode('utf-8').decode('latin-1')#returns the inner HTML as a string
    soup = BeautifulSoup(page, 'html.parser')

    #execute generate_xpath
    isXpathGenerated , elementToXpath =  xpath_obj.generate_xpath(soup)
    if isXpathGenerated is False:
        print ("No XPaths generated for the URL:%s"%url)
    else:
        for variableName,xpath in elementToXpath.items():
            element = elements_obj.getElement(xpath)
            element.send_keys('seleniumhq')
            print("element",element)
            time.sleep(2)
        print("variableNames",elementToXpath)
