# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome("./chromedriver.exe")
driver.maximize_window()
driver.get("https://www.demoblaze.com/index.html")

class TestActividad05():
#   def setup_method(self, method):
#     self.driver = webdriver.Chrome()
#     self.vars = {}
  
#   def teardown_method(self, method):
#     self.driver.quit()
  
  def test_actividad05(self):
    self.driver.get("https://www.demoblaze.com/index.html")
    self.driver.set_window_size(1936, 1066)
    self.driver.find_element(By.ID, "login2").click()
    time.sleep(2)
    self.driver.find_element(By.ID, "loginusername").click()
    time.sleep(2)
    self.driver.find_element(By.ID, "loginusername").send_keys("1234567890")
    time.sleep(2)
    self.driver.find_element(By.ID, "loginpassword").click()
    time.sleep(2)
    self.driver.find_element(By.ID, "loginpassword").send_keys("1234567890")
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "#logInModal .btn-primary").click()
    time.sleep(2)
    self.driver.find_element(By.ID, "itemc").click()
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
    time.sleep(2)
    assert self.driver.switch_to.alert.text == "Product added."
    self.driver.find_element(By.ID, "nava").click()
    time.sleep(2)
    self.driver.find_element(By.ID, "itemc").click()
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Iphone 6 32gb").click()
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
    time.sleep(2)
    assert self.driver.switch_to.alert.text == "Product added."
    self.driver.find_element(By.ID, "nava").click()
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Laptops").click()
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Sony vaio i5").click()
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
    time.sleep(2)
    assert self.driver.switch_to.alert.text == "Product added."
    self.driver.find_element(By.ID, "nava").click()
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Laptops").click()
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "MacBook Pro").click()
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
    time.sleep(2)
    assert self.driver.switch_to.alert.text == "Product added."
    self.driver.find_element(By.ID, "nava").click()
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Monitors").click()
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Apple monitor 24").click()
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
    time.sleep(2)
    assert self.driver.switch_to.alert.text == "Product added."
    self.driver.find_element(By.ID, "nava").click()
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Monitors").click()
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "ASUS Full HD").click()
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
    time.sleep(2)
    assert self.driver.switch_to.alert.text == "Product added."
    self.driver.find_element(By.ID, "nava").click()
    time.sleep(2)
    self.driver.find_element(By.ID, "cartur").click()
    
  driver.quit()
