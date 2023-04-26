import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import  ActionChains



class Demo_drag_drop():
    def diaplay_dropdrag(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.w3schools.com/html/html5_draganddrop.asp')
        driver.maximize_window()
        em1=driver.find_element(By.ID,'drag1')
        em2=driver.find_element(By.ID,'div2')
        # ActionChains(driver).drag_and_drop(em1, em2).perform()
        ActionChains(driver).drag_and_drop_by_offset(em1, 30, 00).perform()
        time.sleep(3)


dragdrop= Demo_drag_drop()
dragdrop.diaplay_dropdrag()       