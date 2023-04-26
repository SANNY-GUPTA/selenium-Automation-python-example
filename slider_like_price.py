import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import  ActionChains


# single single v run kara sakte hai AND DONO AK sath me v RUN kara sakte HAI



class Demo_slider_price():
    def diaplay_likepriceslider(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.snapdeal.com/products/mens-footwear-sports-shoes?sort=plrty&q=Price%3A947%2C2794%7C')
        driver.maximize_window()
        left=driver.find_element(By.XPATH,"//a[@class='price-slider-scroll left-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")
        right =driver.find_element(By.XPATH,"//a[@class='price-slider-scroll right-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")
        time.sleep(3)
        ActionChains(driver).drag_and_drop_by_offset(left, 60, 0).perform()
        # ActionChains(driver).click_and_hold(left).pause(1).move_by_offset(50, 0).release().perform()
        time.sleep(3)
        ActionChains(driver).drag_and_drop_by_offset(right, -50, 0).perform()
        time.sleep(3)



slider=Demo_slider_price()
slider.diaplay_likepriceslider()