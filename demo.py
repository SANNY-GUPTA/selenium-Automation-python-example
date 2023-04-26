import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoFindElementByIDandName():
    def locate_by_id_demo(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        # driver.get("https://secure.yatra.com/social/common/yatra/signin.htm") 
        # YE WALA LOGIN KE SEARCH BOX KE LEA THA LINE  9 KA HAI
        driver.get("https://www.yatra.com/")
        # driver.find_element(By.ID,'login-input').send_keys('test@ate.com')cle
        # driver.find_element(By.XPATH, "//input[@id='login-input']" ).send_keys('test@ate.com') YE XPATH KE LEA
        # driver.find_element(By.CSS_SELECTOR,'#login-input').send_keys('test@ate.com')   YE WALA CSS SELECTOR WALE KE LEA HAI SAB AK HI KAM KARTA HAI 
        # driver.find_element(By.PARTIAL_LINK_TEXT,'Villas &').click()   PARATIAL ME KAISE V LINK KA HALF AND FULL NAME SE V LINK KO OPEN KAR SAKTE HAI
        # driver.find_element(By.LINK_TEXT,'Yatra for Business').click()  YAHA PAR LINK_TEXT KA USE KARKE UNIQUE KE LINK KO OPEN KAR SAKTE HAI
        # driver.find_element(By.CLASS_NAME,'email-login-box').send_keys('sab@sahi.com')  YE WALA CLASS KE HELP SE SEARCH BOX KO DEKHNE KE LEA
        # driver.find_element(By.TAG_NAME,'input').send_keys('sakalsj@laj.com')  YE WALA TAG KE HELP SE SEAARCH KO DEKHNE KE LEA
        # driver.find_element(By.ID,'login-input').send_keys('sab@mast.com')
        lista=driver.find_elements(By.TAG_NAME,'a')
        print(len(lista))
        # YAHA PAR KITNA TAGS USE HUA HAI O SAB B LEN KE HELP SE SHOW KARA SAKTE
        for i in lista:
            print(i.text)
        # YAHA PAR LIST ME ANCHOR TAG KE SATH SATH JO TEXT HOGA O PRINT KARA DEGA BY USING OF for i in lista: print(i.text) 
        time.sleep(4)


findid=DemoFindElementByIDandName()
findid.locate_by_id_demo()        
