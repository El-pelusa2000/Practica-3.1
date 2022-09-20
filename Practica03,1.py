from webbrowser import get
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
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
inf_column= driver.find_element(By.XPATH, '//*[@id="cityTable"]/div[1]/ul')
inf_column= inf_column.text

todays_weather= inf_column.split('Hoy')[0].split('\n')

horas=list()
temp=list()
v_viento=list()

for i in range (0, len (todays_weather),4):
    horas.append(todays_weather[i])
    temp.append(todays_weather[i+1])
    v_viento.append(todays_weather[i+2])

df= pd.DataFrame({'horas':horas,'Temperatura': temp, 'v_viento(km/h)': v_viento})

print (df)
df.to_csv('tiempo_hoy.csv', index=False)

driver.quit()