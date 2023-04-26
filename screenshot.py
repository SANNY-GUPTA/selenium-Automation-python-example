import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# yaha par screenshot 1) screenshot(".\\test.png") only jis link par click hua ho wahi wala
#                     2)  get_screenshot_as_file(".\\test1.png") yaha par pura full screen-shot click kar leta hai
#                     3)  save_screenshot(".\\testfull.png")    ye v full screenshot leta hai
#                                                                   ye tino ke help se le sakte hai
class Demo_screenshot():
    def diaplay_screenshotbycode(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        screen=driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
        screen.screenshot(".\\test.png")
        time.sleep(3)
        screen.click()
        time.sleep(2)
        driver.get_screenshot_as_file(".\\test1.png")
        driver.save_screenshot(".\\testfull.png")



demoscreenshot=Demo_screenshot()
demoscreenshot.diaplay_screenshotbycode()