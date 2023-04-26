from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time



# YAHA PAR KAISE PAGE KO 'LARGE' AND 'SMALL' AND 'CURRENT URL' AND 'TITLE' AND "FORWORD, BACKWORD" KAR SAKTE HAI


class demobrowser:
    def browser(self):
       driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
       driver.get("https://www.yatra.com/")
       print(driver.current_url)
       print(driver.title)
       driver.maximize_window()
       driver.refresh()
       driver.find_element(By.ID,'booking_engine_hotels').click()
       time.sleep(4)
       driver.back()
       time.sleep(3)
       driver.forward()
       driver.minimize_window()
       time.sleep(5)
       driver.quit()

dem=demobrowser()
dem.browser()       