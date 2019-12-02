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
        self.driver = webdriver.Chrome ( executable_path="..//drivers//chromedriver.exe" )
        self.driver.maximize_window ()
        self.driver.implicitly_wait ( 15 )
        self.driver.get("https://tiki.vn/")
        #print(self.driver.title)

    @classmethod
    def test_search_with_keyword(self):
        elem = self.driver.find_element_by_css_selector (
            '#__next > div > header > div.Container-sc-1fnsswg-0.itgICN > div > div.Middle__LeftContainer-sc-1poi789-2.iXVTaA > div.FormSearch__Root-hwmlek-0.eqgiix > div > input' )
        elem.click ()
        elem.send_keys ( 'Dell laptop' )
        elem = self.driver.find_element_by_css_selector (
            '#__next > div > header > div.Container-sc-1fnsswg-0.itgICN > div > div.Middle__LeftContainer-sc-1poi789-2.iXVTaA > div.FormSearch__Root-hwmlek-0.eqgiix > div > button' )
        elem.click ()
        elem = self.driver.find_element_by_css_selector (
            '#ants-product-list > div:nth-child(1) > a > div.content > span > img' )
        elem.click ()

        elem = self.driver.find_element_by_css_selector ( '#\#mainAddToCart' )
        time.sleep ( 2 )
        elem.click ()
        elem = self.driver.find_element_by_css_selector ( '#header-cart > a > div > button' )
        elem.click ()
        elem = self.driver.find_element_by_css_selector (
            '#shopping-cart > div > div.col-right > div.box-info-product > p.action > a.btn.btn-link.btn-item-delete' )
        elem.click ()
        elem = self.driver.find_element_by_css_selector (
            'body > div.wrap > div > div:nth-child(3) > div > div > a' )
        elem.click ()
        self.driver.save_screenshot ( 'C:/Selenium/Python/Project_Tiki/Screenshots/SearchDone.png' )
        print ( "Search Product Successfully" )

    @classmethod
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner ( output='C:/Selenium/Python/Project_Tiki/ReportsHTML' ))