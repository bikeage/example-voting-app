import unittest
import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

ip = os.getenv('IP')
sl_username = os.getenv('SAUCE_USERNAME')
sl_access_key = os.getenv('SAUCE_ACCESS_KEY')

# Give Selenium Hub time to start
time.sleep(15)

class VoteTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Remote(
      command_executor='http://{}:{}@ondemand.saucelabs.com:80/wd/hub'.format(sl_username, sl_access_key),
      desired_capabilities={'browserName': 'chrome'}
    )

  def tearDown(self):
    with open('test1.txt', 'a') as test_results:
      test_results.write("https://saucelabs.com/beta/tests/" + self.browser.session_id+ ",")

  def test_confirm_title(self):
    browser = self.browser
    browser.get("http://{}:80".format(ip))
    self.assertIn("Cats vs Dogs!", browser.title)
    browser.quit()

  def test_confirm_choice_form(self):
    browser = self.browser
    browser.get("http://{}:80".format(ip))
    self.assertTrue(self.browser.find_element_by_id('choice'))
    browser.quit()

  def test_confirm_button_a(self):
    browser = self.browser
    browser.get("http://{}:80".format(ip))
    self.assertTrue(self.browser.find_element_by_id('a'))
    browser.quit()

  def test_confirm_button_b(self):
    browser = self.browser
    browser.get("http://{}:80".format(ip))
    self.assertTrue(self.browser.find_element_by_id('b'))
    browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)