# coding=utf-8
import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.actions_with_elements import ActionsWithElements


class UbsAutofill:
    def autofill(self, path):
        url = 'https://docs.google.com/forms/d/e/1FAIpQLSdUaF7SFrrrdtYA0CUjDP1QfEdx46IAEeKijCl86O_qo2FN7g/viewform?fbclid' \
              '=IwAR0s9aOb1hGYG-A7RRFxw7Fklbm-0xh6OtjKaE5dmfeN5TyvtGnF_w20YvE '
        confirmation_text_expected = 'some text'

        # locators
        dropdown_menu_option_locator = '(//span[contains(text(), \'Печ\')])[2]'
        district_item_locator = '(//span[contains(text(), "Печ")])[2]'
        bags_quantity_radiobutton_locator = '(//label)[1]'
        no_goods_from_store_radiobutton_locator = '(//label)[21]'
        personal_data_agreement_radiobutton_locator = '(//label)[22]'
        submit_button_locator = '(//span)[46]'

        # data
        fio = 'Ємельянова Марія'
        phone_number = '0958221220'
        email = 'yemelianova.me@gmail.com'
        address = 'вул. Предславинська, 49, кутовий під\'їзд'
        entrance = '3'

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

        # dropdown = driver.find_element_by_class_name('quantumWizMenuPaperselectOptionList')

        # enter name
        name_input = text_inputs[0]
        actions.enter_text(name_input, fio)

        # enter phone no.
        phone_input = text_inputs[1]
        actions.enter_text(phone_input, phone_number)

        # enter email
        email_input = text_inputs[2]
        actions.enter_text(email_input, email)

        # select district
        dropdown_expand = dropdown_menu_options[0]
        actions.click_on_element(dropdown_expand)
        district_option = driver.find_element(By.XPATH, dropdown_menu_option_locator)
        actions.click_on_element(district_option)

        # wait to make sure dropdown list is hidden
        time.sleep(2)

        # enter address
        address_input = text_inputs[3]
        actions.enter_text(address_input, address)

        # enter no. of entrance
        entrance_input = text_inputs[4]
        actions.enter_text(entrance_input, entrance)

        # select number of bags to be picked up
        option_2_bags = radiobuttons[2]
        option_2_bags.click()

        # select number of bags with old clothes to be picked up
        option_0_bags_clothes = radiobuttons[4]
        option_0_bags_clothes.click()

        # select if you have or have not ordered any goods in the UBS store
        option_ordered_goods = radiobuttons[8]
        option_no_goods = radiobuttons[9]

        option_no_goods.click()

        # accept personal data usage agreement
        accept_agreement = radiobuttons[10]
        accept_agreement.click()

        # time.sleep(3)
        # driver.quit()

