import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# this apporach are normal and not use on large scale
#  another way are also but apporach are awosome but it's hard and it's in my phone where i click the picture


class Demo_calender_handle():
    def diaplay_calenderhandle(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.yatra.com/')
        datee=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']")
        datee.click()
        time.sleep(4)
        driver.find_element(By.XPATH,"//td[@id='16/05/2023']").click()
        time.sleep(4)


calend=Demo_calender_handle()
calend.diaplay_calenderhandle()      