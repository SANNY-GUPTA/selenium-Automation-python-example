import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# yaha par "_self" laga dene se same page me khulega 

class Demo_jv():
    def diaplay_javascripts(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        # driver.get('https://www.rcvacademy.com/')
        driver.execute_script("window.open('https://www.rcvacademy.com/' ,'_self');")
        time.sleep(4)
        demo=driver.execute_script("return document.getElementsByTagName('p')[13];")
        driver.execute_script("arguments[1] .click();",demo)



java=Demo_jv()
java.diaplay_javascripts()