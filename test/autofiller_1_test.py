# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.actions_with_elements import ActionsWithElements


class MyTestForm:

    def test(self, path):
        url = 'https://docs.google.com/forms/d/e/1FAIpQLSfe81h4Ht3fasSzpnQKNU5imZU-hZ_RdWGzkjYc-WGylipepg/viewform?usp=sf_link'
        confirmation_text_expected = 'Thank you for your interest.\nSomeone will be contacting you shortly.'

        # locators
        dropdown_menu_option_locator = '(//span[contains(text(), \'Lut\')])[2]'
        radiobutton_option_locator = '(//div[contains(@class,\'exportOuterCircle\')])[2]'
        checkbox_option_locator_2 = '(//div[contains(@class,\'exportInnerBox\')])[2]'
        checkbox_option_locator_4 = '(//div[contains(@class,\'exportInnerBox\')])[4]'
        checkbox_option_locator_5 = '(//div[contains(@class,\'exportInnerBox\')])[5]'
        cover_letter_input_locator = '//textarea'
        submit_button_locator = '//span[contains(@class,\'PaperbuttonLabel\')]'
        confirmation_message_locator = '//div[contains(@class,\'ConfirmationMessage\')]'



        # data
        fio = 'Lina Lamont'
        phone_number = '0958221220'
        email = 'yemelianova.me@gmail.com'
        address = 'вул. Предславинська, 49, кутовий під\'їзд'

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(path, chrome_options=chrome_options)
        driver.implicitly_wait(20)
        actions = ActionsWithElements(driver)
        driver.get(url)

        text_inputs = driver.find_elements_by_class_name('quantumWizTextinputPaperinputInput')
        dropdown_menu = driver.find_element_by_class_name('quantumWizMenuPaperselectOptionList')
        dropdown_menu_options = driver.find_elements_by_class_name('quantumWizMenuPaperselectContent')
        radiobuttons = driver.find_elements_by_class_name('appsMaterialWizToggleRadiogroupRadioButtonContainer')

        name_input = text_inputs[0]
        actions.enter_text(name_input, fio)

        email_input = text_inputs[1]
        actions.enter_text(email_input, email)

        phone_number_input = text_inputs[2]
        actions.enter_text(phone_number_input, phone_number)

        dropdown_expand = dropdown_menu_options[0]
        actions.click_on_element(dropdown_expand)

        dropdown_city_option = driver.find_element(By.XPATH, dropdown_menu_option_locator)
        actions.click_on_element(dropdown_city_option)

        time.sleep(2)

        # body = driver.find_element_by_css_selector('body')
        # body.send_keys(Keys.PAGE_DOWN)

        desired_position = driver.find_element(By.XPATH, radiobutton_option_locator)
        actions.click_on_element(desired_position)

        checkbox_option_2 = driver.find_element(By.XPATH, checkbox_option_locator_2)
        checkbox_option_2.click()

        checkbox_option_4 = driver.find_element(By.XPATH, checkbox_option_locator_4)
        checkbox_option_4.click()

        checkbox_option_5 = driver.find_element(By.XPATH, checkbox_option_locator_5)
        checkbox_option_5.click()

        cover_letter_input = driver.find_element(By.XPATH, cover_letter_input_locator)
        cover_letter_input.send_keys("hello! how are you?")

        initial_url = driver.current_url

        submit_button = driver.find_element(By.XPATH, submit_button_locator)
        submit_button.click()

        url_upon_submit = driver.current_url
        assert url_upon_submit != initial_url

        confirmation_message = driver.find_element(By.XPATH, confirmation_message_locator)
        confirmation_message_text_actual = confirmation_message.text

        assert confirmation_message_text_actual == confirmation_text_expected

        print(confirmation_message_text_actual)


        # confirmation_text_1 = 'Thank you for your interest.'
        # confirmation_text_2 = 'Someone will be contacting you shortly.'

        #todo: assert url has changed
        # assert text displayed: 'Thank you for your interest.'

        # driver.quit()

#todo: add asserts to make an actual test

#setup jenkins
