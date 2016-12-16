import unittest
import bell

import pyth_couch

from base_case import on_platforms
from base_case import browsers
from base_case import BaseCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@on_platforms(browsers)
class LoginTestCouchDB(BaseCase):
	
	
	def test_login_bycouchdb(self):
		pyth_couch.create_member()
		driver = self.driver
        
        # login
		bell.login_test(self.driver, "q", "q")
        
        # wait for the next page
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dashboard")))
		self.logout_test()
		
	def logout_test(self):
		""" NoneType -> NoneType

		Helper function testing a correct logout operation.
		"""
		driver = self.driver
		# test logout
		bell.logout(driver)
		# ensure logout was successful
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "login")))
		actual = driver.current_url
		expected = "http://127.0.0.1:5981/apps/_design/bell/MyApp/index.html#login"
		self.assertEqual(actual, expected)	
		
if __name__ == "__main__":
    unittest.main()
