from webbrowser import get
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://github.com/login")

usuario = driver.find_element(By.ID,"login_field")
#time.sleep(3)
usuario.send_keys("El-pelusa")
password=driver.find_element(By.ID,"password")
password.send_keys("wenas")
usuario.send_keys(Keys.ENTER)