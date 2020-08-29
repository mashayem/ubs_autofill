# coding=utf-8
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation'])
#option.add_argument("--headless")
#option.add_argument("disable-gpu")

PATH = '../chromedriver'
url = 'https://docs.google.com/forms/d/e/1FAIpQLSdUaF7SFrrrdtYA0CUjDP1QfEdx46IAEeKijCl86O_qo2FN7g/viewform?fbclid' \
      '=IwAR0s9aOb1hGYG-A7RRFxw7Fklbm-0xh6OtjKaE5dmfeN5TyvtGnF_w20YvE '

#locators
# surname_locator = '(//input[@type = \'text\'])[1]'
# surname_locator = '(//input[1])[1]'
# surname_locator = '(//div[contains(text(), "Ваша відповідь")])[1]'
# phone_locator = '(//input[1])[3]'
# email_locator = '(//input[1])[4]'
# address_locator = '(//input[1])[5]'
# entrance_locator = '(//input[1])[6]'
# district_dropdown_locator = '//span[text() = "Choose"]'
# district_list_popup_locator = 'div[soy-server-key="5:pZtlf"]'
# district_item_locator = '(//span[contains(text(), "Печ")])[2]'
# bags_quantity_radiobutton_locator = '(//label)[1]'
# no_goods_from_store_radiobutton_locator = '(//label)[21]'
# personal_data_agreement_radiobutton_locator = '(//label)[22]'
# submit_button_locator = '(//span)[46]'

#data
fio = 'Ємельянова Марія Євгенівна'
phone_number = '0958221220'
email = 'yemelianova.me@gmail.com'
address = 'вул. Предславинська, 49, кутовий під\'їзд'
entrance = '3'

driver = webdriver.Chrome(PATH)
driver.get(url)

text_inputs = driver.find_elements_by_class_name('quantumWizTextinputPaperinputInput')
radiobuttons = driver.find_elements_by_class_name('appsMaterialWizToggleRadiogroupRadioButtonContainer')
dropdown = driver.find_element_by_class_name('quantumWizMenuPaperselectOptionList')
# submit_button = driver.find_elements_by_class_name('')


# surname_input = driver.find_element(By.XPATH, surname_locator)
# if surname_input.is_displayed():
#     surname_input.click()
#     surname_input.send_keys()
#
# phone_input = driver.find_element(By.XPATH, phone_locator)
# phone_input.click()
# phone_input.send_keys("text")
#
# email_input = driver.find_element(By.XPATH, email_locator)
# phone_input.click()
# phone_input.send_keys("text")
#
# district_dropdown = driver.find_element(By.XPATH, district_dropdown_locator)
# district_dropdown.click()
# if driver.find_element(By.CSS_SELECTOR, district_list_popup_locator).is_displayed():
#     driver.find_element(By.XPATH, district_item_locator).click()

# address_input = driver.find_element(By.XPATH, address_locator)
# address_input.click()
# address_input.send_keys("text")








