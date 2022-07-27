from selenium import webdriver

from bs4 import BeautifulSoup


import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




# global driver variable
driver = None



def generate_xpath(self,soup):
        "generate the xpath and assign the variable names"
        result_flag = False
        for guessable_element in self.guessable_elements:
            self.elements = soup.find_all(guessable_element)
            for element in self.elements:
                if (not element.has_attr("type")) or (element.has_attr("type") and element['type'] != "hidden"):
                    for attr in self.known_attribute_list:
                        if element.has_attr(attr):
                            locator = self.guess_xpath(guessable_element,attr,element)
                            if len(driver.find_elements_by_xpath(locator))==1:
                                result_flag = True
                                variable_name = self.get_variable_names(element)
                                # checking for the unique variable names
                                if  variable_name != '' and variable_name not in self.variable_names:
                                    self.variable_names.append(variable_name)
                                    print ("%s_%s = %s"%(guessable_element, variable_name.encode('utf-8').decode('latin-1'), locator.encode('utf-8').decode('latin-1')))
                                    break
                                else:
                                    print (locator.encode('utf-8').decode('latin-1') + "----> Couldn't generate appropriate variable name for this xpath")
                        elif guessable_element == 'button' and element.getText():
                            button_text = element.getText()
                            if element.getText() == button_text.strip():
                                locator = xpath_obj.guess_xpath_button(guessable_element,"text()",element.getText())
                            else:
                                locator = xpath_obj.guess_xpath_using_contains(guessable_element,"text()",button_text.strip())
                            if len(driver.find_elements_by_xpath(locator))==1:
                                result_flag = True
                                #Check for utf-8 characters in the button_text
                                matches = re.search(r"[^\x00-\x7F]",button_text)
                                if button_text.lower() not in self.button_text_lists:
                                    self.button_text_lists.append(button_text.lower())
                                    if not matches:
                                        # Striping and replacing characters before printing the variable name
                                        print ("%s_%s = %s"%(guessable_element,button_text.strip().strip("!?.").encode('utf-8').decode('latin-1').lower().replace(" + ","_").replace(" & ","_").replace(" ","_"), locator.encode('utf-8').decode('latin-1')))
                                    else:
                                        # printing the variable name with utf-8 characters along with language counter
                                        print ("%s_%s_%s = %s"%(guessable_element,"foreign_language",self.language_counter, locator.encode('utf-8').decode('latin-1')) + "---> Foreign language found, please change the variable name appropriately")
                                        self.language_counter +=1
                                else:
                                    # if the variable name is already taken
                                    print (locator.encode('utf-8').decode('latin-1') + "----> Couldn't generate appropriate variable name for this xpath")
                                break

                        elif not guessable_element in self.guessable_elements:
                            print("We are not supporting this gussable element")

        return result_flag
def getInputElements(form):
    inputs = form.find_elements(By.TAG_NAME, "input")
    return inputs

def saveFile(attributes):
    df = pd.DataFrame({'Attributes':attributes})
    df.to_csv('elements.csv', index=False, encoding='utf-8')

def addSearchText():
    elem = driver.find_element(By.ID, 'firstName')  # Find the search box
    elem.send_keys('seleniumhq')

def getAttributes(element):
    attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', element)
    return attrs

def initializeDriver(url):
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    driver.get(url)
    return driver

def start():
    form = driver.find_element(By.TAG_NAME,"form")
    inputs = getInputElements(form)
    attributes = []
    for i in inputs :
        attr = getAttributes(i)
        attributes.append(attr)

    saveFile(attributes)

if __name__ == "__main__":
    try :
        driver = initializeDriver('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
        time.sleep(1)
        start()
        addSearchText()
    except Exception as e:
        print(e)
    finally:
        driver.quit()


