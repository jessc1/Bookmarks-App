from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://127.0.0.1:8000/account/login/')
        #header_text = self.brownser.find_element_by_tag_name('h1').text
        #self.assertIn('Log-in', header_text)



if __name__ == '__main__':
    unittest.main(warnings='ignore')
 