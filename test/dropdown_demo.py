import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utils.actions_with_elements import ActionsWithElements


class WebelementsDemo:
    start_url = 'https://rahulshettyacademy.com/AutomationPractice/'
    select_locator = ''

    def __init__(self, path):
        self.driver = webdriver.Chrome(path)
        self.driver.implicitly_wait(10)
        self.driver.get(self.start_url)
        # self.actions = ActionsWithElements(self.driver)

    def dropdownDemo(self):
        dropdown = self.driver.find_element(By.ID, 'dropdown-class-example')
        s = Select(dropdown)
        s.select_by_value('option2')

    #     # self.driver.quit()









