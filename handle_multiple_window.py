import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Demo_multiple_window_handle():
    def diaplay_multiplewindowhandle(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.yatra.com/')
        driver.maximize_window()
        parent_handle=driver.current_window_handle
        print(parent_handle)
        time.sleep(4)
        driver.find_element(By.XPATH,"//img[@alt='Flat 14% OFF (upto Rs.1,800)+ no cost emi']").click()
        all_handle=driver.window_handles
        print(all_handle)
        time.sleep(4)
        for handle in all_handle:
            if handle!=parent_handle:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH,"//i[@class='sprite-footer ico-tgFooter_family']").click()
                time.sleep(4)
                driver.close()
                time.sleep(2)
                break

        driver.switch_to.window(parent_handle)
        driver.find_element(By.XPATH,"//img[@alt='Flat 14% OFF (upto Rs.1,800)+ no cost emi']")  
        time.sleep(4)  



multiplewind=   Demo_multiple_window_handle()
multiplewind.diaplay_multiplewindowhandle()     