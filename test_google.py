from selenium import webdriver
import unittest
import time
class GoogleSearchDemo(unittest.TestCase):
    def setUp(self):
        global driver
        driver=webdriver.Firefox(executable_path='D:\sele\geckodriver.exe')
        driver.get('http://www.google.com')
        driver.maximize_window()


    def test(self):
        driver.find_element_by_name('q').send_keys('mahesh babu')
        time.sleep(5)
        driver.find_element_by_name('btnK').click()
        time.sleep(5)
        driver.find_element_by_class_name('LC20lb').click()
        time.sleep(5)


    def tearDown(self):
        driver.close()

unittest.main()
