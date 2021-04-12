from selenium import webdriver
import HtmlTestRunner
import unittest
import time


class TestHomePage(unittest.TestCase):
    @classmethod
    def setUp(self):
        #     # Initiate in "headless mode", where the browser saves time by not rendering the page:
        #     # from selenium.webdriver.chrome.options import Options
        #     #
        #     # options = Options ()
        #     # options.headless = True
        #     # driver = webdriver.Chrome ( executable_path=EXE_PATH, chrome_options=options )
        #     # driver.set_window_size ( 1440, 900 )
        #     self.driver.get ( BASE_URL )
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-infobars")
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(
            executable_path="drivers//chromedriver.exe", options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.set_page_load_timeout(30)
        self.driver.get("https://tiki.vn/")

    def test_search_with_keyword(self):
        elem = self.driver.find_element_by_xpath(
            "//*[@id='__next']/div[1]/header/div[1]/div/div[1]/div[2]/div/input"
        )
        elem.click()
        elem.send_keys("Dell laptop")
        elem = self.driver.find_element_by_xpath(
            "//*[@id='__next']/div[1]/header/div[1]/div/div[1]/div[2]/div/button/img"
        )
        elem.click()
        time.sleep(3)
        
        # Chọn Hàng mới của Dell laptop
        elem_hangmoi = self.driver.find_element_by_xpath(
            "//*[@id='__next']/div[1]/main/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/a[3]"
        )
        elem_hangmoi.click()
        time.sleep(3)
        lst_products = self.driver.find_elements_by_xpath(
            "//*[@id='__next']/div[1]/main/div[2]/div/div[2]/div/div[2]//a[@class='product-item']"
        )
        get_products = [item for item in lst_products]
        print(get_products)
        get_products[1].click()
        time.sleep(4)
        chonmua_btn = self.driver.find_element_by_xpath(
            "//*[@id='__next']/div[1]/main/div[4]/div/div[3]/div[2]/div/div[1]/div[4]/div[2]/button"
        )
        chonmua_btn.click()
        time.sleep(2)
        xem_gio_hang_btn = self.driver.find_element_by_xpath(
            "//*[@id='__next']/div[1]/header/div[1]/div/div[2]/div[2]/div/a[2]"
        )
        xem_gio_hang_btn.click()
        time.sleep(3)
        check_price = self.driver.find_element_by_xpath("//*[@id='__next']/div[1]/main/div/div/div/div[1]/div/div/div/ul/li/div/div[2]/div/div[2]/div[1]/p")
        if check_price.text >= '17.000.000':
            print('Real price:', check_price.text.encode("utf-8"))
        self.driver.save_screenshot("Screenshots/SearchDone.png")
        print("Search Product Successfully")

    @classmethod
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="ReportsHTML"))
