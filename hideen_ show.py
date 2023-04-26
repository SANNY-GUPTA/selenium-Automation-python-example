import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Demo_hidden_convert_normal():
    def diaplay_hiddden(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp')
        se=driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(se)
        time.sleep(4)
        # YAHA PAR HMM LINK JO KI HIDDEN HAI USKO UNHIDE KARNE KA TARIKA USE KARTE HAI(matlab ki jo link ko click karne par koi hide data show kare and usko unhide karne ka tarika hia ye)
        #   "yaha par data link ke help se show and hide kara rahe hai link ko"
        driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']").click()
        se1=driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(se1)
        time.sleep(4) 

    def display_yatra(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.yatra.com/hotels')
        driver.find_element(By.XPATH,"//span[normalize-space()='Traveller']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
        time.sleep(3)
        em=driver.find_element(By.XPATH,"//select[@class='ageselect']").is_displayed()
        print(em)
        driver.find_element(By.XPATH,"//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[1]").click()
        time.sleep(3)
        em1=driver.find_element(By.XPATH,"//select[@class='ageselect']").is_displayed()
        print(em1)
        time.sleep(3)





hiddenkelea=Demo_hidden_convert_normal()
# hiddenkelea.diaplay_hiddden()
hiddenkelea.display_yatra()