import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import  ActionChains


# Mouse hover karke uske under ke link ko control kar sakte hai
#    ye wala import phale karna padega    "from selenium.webdriver import  ActionChains"
# sabse 1) phale import then open the train wala link 
#        2) then jaha par hover karna hai uske xpath ko kisse v (a)name se allocate kar lena
#         3) then again kisse v (b)name se Actionchains(driver) ko call kar lena hai
#          4) then us (b)name ko .move_to_element(a).perforn() se call kar lena
#           5) then phir jis link ko open karna hai us link ka xpath de kar open kar lena hai



class Demo_Mouse_hover():
    def diaplay_hoveringMouse(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.yatra.com/')
        driver.maximize_window()
        morebuttom=driver.find_element(By.XPATH,"//span[@class='more-arr']")
        achains=ActionChains(driver)
        achains.move_to_element(morebuttom).perform()
        time.sleep(4)
        driver.find_element(By.XPATH,"//a[@id='booking_engine_xplore']").click()
        time.sleep(3)

    def demo_double_click(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://artoftesting.com/samplesiteforselenium')
        driver.maximize_window()
        achains1=ActionChains(driver)
        doubleclick=driver.find_element(By.XPATH,"//button[@id='dblClkBtn']")
        achains1.double_click(doubleclick).perform()
        time.sleep(4)    

        

hover=Demo_Mouse_hover()
# hover.diaplay_hoveringMouse()     
hover.demo_double_click()