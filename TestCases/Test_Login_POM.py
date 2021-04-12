from selenium import webdriver
import HtmlTestRunner
import unittest
import time
from Pages.LoginPage import Login
import sys
sys.path.append("../Pages")


class TestDemo(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(
            executable_path="..//drivers//chromedriver.exe")
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login_as_normal_user(self):
        driver = self.driver
        driver.get("https://tiki.vn/")
        assert "Tiki" in driver.title
        driver.implicitly_wait(15)
        log_in = Login(self.driver)
        log_in.click_1()
        log_in.click_2()
        log_in.input_1()
        log_in.input_2()
        time.sleep(2)
        log_in.click_ok_btn()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='ReportsHTML'))
