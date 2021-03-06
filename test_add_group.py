# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_add_group(self):
        success = True
        wd = self.wd
    wd.get("https://vk.com/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()



