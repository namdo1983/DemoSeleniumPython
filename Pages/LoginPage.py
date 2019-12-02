from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Pages.Locators import Locator


class Login():

    def __init__(self, driver):
        self.driver = driver

    def click_1(self):
        self.driver.find_element(By.XPATH, Locator.LOGIN_MENU).click()

    def click_2(self):
        self.driver.find_element(By.CSS_SELECTOR, Locator.LOGIN_SUBMENU).click()

    def input_1(self):
        self.driver.find_element ( By.CSS_SELECTOR, Locator.EMAIL_FIELD ).send_keys ('namdd_aptech@yahoo.com')

    def input_2(self):
        self.driver.find_element ( By.CSS_SELECTOR, Locator.PASSWORD_FIELD ).send_keys ( 'bobo2407' )

    def click_ok_btn(self):
        elem = self.driver.find_element ( By.XPATH, Locator.LOGIN_BTN )
        hover = ActionChains ( self.driver ).move_to_element (elem)
        hover.perform()
        elem.click()

