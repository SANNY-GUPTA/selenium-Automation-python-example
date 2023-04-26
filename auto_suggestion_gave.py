import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Demo_Auto_suggest():
    def diaplay_autosuggest(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.yatra.com/')
        sa=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        sa.click()
        time.sleep(2)
        sa.send_keys("New")
        time.sleep(4)
        sa.send_keys(Keys.ENTER)
        time.sleep(3)
        


autosugg=Demo_Auto_suggest()
autosugg.diaplay_autosuggest()