import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# yaha par ak sath me ak se jada drop_down ko selector kar sakte hai
# and deselector ka use karke delete v kar sakte hai "dd_multi.Select_by_index/values/visible_text" se karte hai
#  ak sabse "all" laga dene se sab delete ho jata hia



class Demo_selector_fill():
    def diaplay_selectorfill(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://artoftesting.com/samplesiteforselenium')