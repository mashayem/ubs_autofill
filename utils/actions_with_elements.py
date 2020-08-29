from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementNotVisibleException, InvalidElementStateException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ActionsWithElements:
    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, element: WebElement, text: str):
        try:
            element.click()
            element.clear()
            element.send_keys(text)
            print('text was entered')
        except ElementNotVisibleException:
            print('element not visible')
        except ElementNotInteractableException:
            print('unable to interact with element')
        except InvalidElementStateException:
            print('unable to interact with element')

    def click_on_element(self, element: WebElement):
        try:
            element.click()
            print("element was clicked")
        except ElementNotVisibleException:
            print('element not visible')
        except ElementNotInteractableException:
            print('unable to interact with element')
        except InvalidElementStateException:
            print('unable to interact with element - invalid element state')

    def click_with_execute_script(self, element: WebElement):
        try:
            element.click()
            print("element was clicked")
        except ElementNotVisibleException:
            print('element not visible')
        except ElementNotInteractableException:
            print('unable to interact with element')
        except InvalidElementStateException:
            print('unable to interact with element - invalid element state')

    def move_to_element(self, element: WebElement):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
