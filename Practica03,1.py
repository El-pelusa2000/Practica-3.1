from webbrowser import get
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome("./chromedriver.exe")
driver.maximize_window()
driver.get("https://www.clima.com")
driver.find_element(By.XPATH, "//a[contains(@href, \'https://www.clima.com/mexico\')]").click()
time.sleep(2)
#con esto pondremos el estado al que queremos buscar
driver.find_element(By.XPATH, "//input[@id=\'term\']").send_keys("Jalisco")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"li:nth-child(1) .item-name").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(),\'Por horas\')]").click()
