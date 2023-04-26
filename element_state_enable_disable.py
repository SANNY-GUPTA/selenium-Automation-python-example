from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


# HERE BASICALLY HMM KISSE V LOGIN OR ANY JO DISABLE HAI(SIGN,LOGIN) USKO ENABLE KAR SAKTE HAI


class element_enable_disable:
    def enable_disable(self):
       driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
       driver.get('https://makaut1.ucanapply.com/smartexam/public/')
       driver.find_element(By.XPATH,"//input[@id='username']").send_keys('askj.com')
       driver.find_element(By.XPATH,"//input[@id='password']").send_keys('saldj')
       time.sleep(5)
    #    driver.find_element(By.ID,'user_name').send_keys('sab@lasj.com')
    #    time.sleep(4)
    #    driver.find_element(By.ID,'user_pass').send_keys('al;j.com')
    #    time.sleep(3)
    #    s=driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
    #    print(s)


obj=element_enable_disable()
obj.enable_disable()