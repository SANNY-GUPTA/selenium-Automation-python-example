import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



# yaha par implict me jab sab sahi ho to turant run karke off ho jaiega screen 
#  ak v galat hoga to minimum implict time tak wait karege


class Demo_implict_wait():
    def display_implictwait(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://login.salesforce.com/?locale=in')
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element(By.ID,'username').send_keys("alsj")
        driver.find_element(By.ID,'password').send_keys("sda;")
        




implictcheck=Demo_implict_wait()
implictcheck.display_implictwait()