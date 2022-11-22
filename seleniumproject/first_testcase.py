# test case
# open browser
# open site https://admin-demo.nopcommerce.com/admin/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("D:\QA\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(by=By.NAME,value="Email").clear()
driver.find_element(by=By.NAME,value="Email").send_keys("admin@yourstore.com")
driver.find_element(by=By.ID,value="Password").clear()
driver.find_element(by=By.ID,value="Password").send_keys("admin")
driver.find_element(by=By.XPATH,value="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()

act_title=driver.title
exp_title="Dashboard / nopCommerce administration"
if act_title==exp_title:
    print("login test pass")
else:
    print("fail")
driver.close()

 
