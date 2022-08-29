from faker import Faker

# class to get the
fake = Faker()


class Elements:
    def __init__(self) -> None:
        fake = Faker()

    def getAttributes(element):
        attrs = driver.execute_script(
            'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', element)
        return attrs

    def addSearchText():
        elem = driver.find_element(By.ID, 'firstName')
        elem.send_keys('seleniumhq')

    def getInputElements(form):
        inputs = form.find_elements(By.TAG_NAME, "input")
        return inputs

    def defaultHandler(self):
        pass

    def handleButton(self):
        pass

    def addName():
        return fake.name()

    def handleText(self,):
        switcher = {
            "name": addName(),
            "address": addAddress(),
        }

    def addValue(self, inputElement):
        switcher = {
            "button": handleButton(),
            "checkbox": handleCheckbox(),
            "color": handleColor(),
            "date": handleDate(),
            "datetime-local": handleDateTime(),
            "email": handleEmail(),
            "file": handleFile(),
            "hidden": handleHidden(),
            "image": handleImage(),
            "month": handleMonth(),
            "number": handleNumber(),
            "password": handlePassword(),
            "radio": handleRatio(),
            "range": handleRange(),
            "reset": handleReset(),
            "search": handleSearch(),
            "submit": handleSubmit(),
            "tel": handleTel(),
            "text": handleText(),
            "time": handleTime(),
            "url": handleUrl(),
            "week": handleWeek(),
        }

        switcher.get(inputElement, defaultHandler())
