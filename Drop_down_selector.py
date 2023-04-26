import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# yaha par selector ke help se dropdown ko control kar sakte hai
# ye 3 type se control kar sakte hai  1) select_by_index()
                                    # 2) select_by_visible_text()
#                                     3) select_by_value()   
class Demo_selector_fill():
    def diaplay_selectorfill(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://artoftesting.com/samplesiteforselenium')
        dropdown=driver.find_element(By.XPATH,"//select[@id='testingDropdown']")
        dd=Select(dropdown)
        dd.select_by_index(2)
        time.sleep(5)
        dd.select_by_visible_text("Performance Testing")
        time.sleep(3)
        dd.select_by_value("Database")
        time.sleep(2)




ddemo=Demo_selector_fill()
ddemo.diaplay_selectorfill()