from cmd.inithandler import start
from cmd.xpathhandler import init_xpath

# global driver variable
driver = None


if __name__ == "__main__":
    driver = start()
    init_xpath(driver)
    
