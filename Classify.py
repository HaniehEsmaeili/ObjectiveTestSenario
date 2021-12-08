from typing import Iterator
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, ElementNotVisibleException, WebDriverException, NoSuchElementException

class Digikala:
    def __init__(self, url) :
        self.driver = webdriver.Firefox()
        self.url = url

    
    def Login(self, username, password):
        self.driver.get('https://www.digikala.com/users/login-register/?_back=https://www.digikala.com/')
        try:
            username_field= self.driver.find_element_by_name('login[email_phone]')
            username_field.send_keys(username)
            enter=self.driver.find_element_by_xpath("//button[contains(@class,'o-btn o-btn--contained-red-lg')]")
            enter.click()
            password_field = self.driver.find_element_by_name('login[password]')
            password_field.send_keys(password)
            continueing=self.driver.find_element_by_xpath("//button[contains(@class,'o-btn o-btn--full-width')]")
            continueing.click()
        except NoSuchElementException or WebDriverException or ElementClickInterceptedException or ElementNotInteractableException or ElementNotVisibleException:
            print("*******************Incorrect Information***********************")


        observing_info= self.driver.find_element_by_xpath("//a[@class='c-header__btn-profile js-dropdown-toggle']")
        observing_info.click()



DK = Digikala('https://www.digikala.com')
DK.Login('hanieesmaeili324@gmail.com', '889900Mt')