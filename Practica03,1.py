from webbrowser import get
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.clima.com")
driver.find_element(By.XPATH, "//a[contains(@href, \'https://www.clima.com/mexico\')]").click()
time.sleep(2)
#con esto pondremos el estado al que queremos buscar
driver.find_element(By.XPATH, "//input[@id=\'term\']").send_keys("Jalisco")
time.sleep(2)
driver.find_element_by_xpath("//span[contains(text(),'Lagos de Moreno, Estado de Jalisco')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(),\'Por horas\')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(),\'Días\')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(),\'Fin de semana\')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(),\'Más info\')]").click()
print ("Done")