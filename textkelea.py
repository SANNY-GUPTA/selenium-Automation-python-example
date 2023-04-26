from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time





class textfind:
    def findtext(self):
       driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
       driver.get("https://www.yatra.com/")
       re=driver.find_element(By.XPATH,"//span[normalize-space()='Popular International Flight Routes']").text
       print(re)
       # kisee v particular link or any ka text pata karne ke lea use karte hai "text" LINE ----14 & 15
       print(driver.title)
       time.sleep(4)
       sse=driver.find_element(By.XPATH,"//a[@id='booking_engine_flights']").get_attribute("rel class")
       print(sse)
       # iske help se hmm kisse v particular attribute ka value and bahut se bate jan sakte hia LINE -----19 & 20
       
    


text=textfind()
text.findtext()       