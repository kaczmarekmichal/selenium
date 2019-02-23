# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select




class WsbPlCheck(unittest.TestCase):

    def tearDown(self):
        self.driver.quit()



    #przed kazdym testem - TCsetup
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

#    metody rozpoczynajace sie od slowa test - nasze testy
    def test_wsb_pl(self):
        driver = self.driver
        driver.get("http://wsb.pl")
        self.assertIn("Wyższe Szkoły Bankowe".decode("utf-8"), driver.title)

    def test_wsb_link(self):
        driver = self.driver
        driver.get("http://wsb.pl")
        driver.find_element_by_link_text("Czym jest sukces?").click()
        #time.sleep(5)

    def test_wsb_link_partial(self):
        driver = self.driver
        driver.get("http://wsb.pl")
        driver.find_element_by_partial_link_text("Czym jest s").click()
        #time.sleep(5)

    def test_wsb_link_city_id(self):
        driver = self.driver
        driver.get("http://wsb.pl")
        #driver.find_element_by_id("edit-city")
        select_university=Select(driver.find_element_by_id("edit-city"))
        self.assertEqual(11, len(select_university.options))

        act_options =[]

        for option in select_university.options:
            act_options.append(option.get_attribute("text"))

        exp_options =[u'Wybierz miasto', u'Bydgoszcz',u'Chorzów/Katowice',u'Gdańsk',
        u'Gdynia',u'Opole',u'Poznań',u'Szczecin',u'Toruń',u'Warszawa',u'Wrocław']

        self.assertEqual(act_options, exp_options)

        #time.sleep(5)





if __name__ =='__main__':
    unittest.main()
