import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Demo_alert_pop():
    def diaplay_popupalert(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://artoftesting.com/samplesiteforselenium')
        driver.maximize_window()
        driver.find_element(By.XPATH,"//button[normalize-space()='Generate Confirm Box']").click()
        time.sleep(4)
        driver.switch_to.alert.accept()
        time.sleep(3)
        driver.switch_to.alert.dismiss()
        time.sleep(3)
        # driver.switch_to.alert.send_keys("sanny")
        # time.sleep(4)         YE JAB KOI ALERT ME SEND KARWANA HO THEN THAT TIME YE WALA USE KARENGE 
        #   1) ALERT(driver).accept()   2) driver.switch_to.alert.accept()   BOTH ARE SAME WORK BUT IN 1 IMPORT ALERT FROM SELENIUM.webdriver.COMMON.ALERT IMPORT ALERT
 


popalert=Demo_alert_pop()        
popalert.diaplay_popupalert()