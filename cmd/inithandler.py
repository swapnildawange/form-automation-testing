class InitHandler:
    def __init__(self):
        try:
            driver = webdriver.Chrome(service=Service(
                ChromeDriverManager().install()))
            driver.get(
                'https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
            time.sleep(1)
            return driver
            # start()
            # addSearchText()
        except Exception as e:
            print(e)
        # finally:
        # # driver.quit()
        # pass
