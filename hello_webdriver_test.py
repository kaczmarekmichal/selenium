# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import time




class GoogleTest(unittest.TestCase):

        def setUp(self):
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()

        def tearDown(self):
            self.driver.quit()

        def test_google_pl_(self):
            driver = self.driver
            driver.get("http://google.pl")
            input = driver.find_element_by_name('q')
            input.send_keys("wsb katowice")
            input.submit()

            time.sleep(3)



if __name__ =='__main__':
    unittest.main()
