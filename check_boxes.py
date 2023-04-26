import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Demo_check_boxes():
    def diaplay_checkingboxes(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://artoftesting.com/samplesiteforselenium')
        ree=driver.find_element(By.XPATH,"//input[@value='Automation']").is_selected()
        print(ree)
        driver.find_element(By.XPATH,"//input[@value='Automation']").click()
        driver.find_element(By.XPATH,"//input[@value='Performance']").click()
        re=driver.find_element(By.XPATH,"//input[@value='Automation']").is_selected()
        print(re)
        time.sleep(4)



 

obj=Demo_check_boxes()
obj.diaplay_checkingboxes()