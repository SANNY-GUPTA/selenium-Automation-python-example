import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Demo_radio_buttom():
    def diaplay_radioclilck(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://artoftesting.com/samplesiteforselenium')
        driver.find_element(By.XPATH,"//input[@id='male']").click()
        time.sleep(4)
        driver.find_element(By.XPATH,"//input[@id='female']").click()
        time.sleep(4)


radio=Demo_radio_buttom()
radio.diaplay_radioclilck()