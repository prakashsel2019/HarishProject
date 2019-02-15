from selenium import webdriver

driver=webdriver.Chrome(executable_path="E:/chromedriver/chromedriver.exe")
driver.get("file:///C:/Users/prakash.periyasamy/Desktop/Loginform.html")
driver.find_element_by_id("uid").send_keys("prakash")
driver.find_element_by_name("pass").send_keys("prakash")
driver.find_element_by_class_name("btnclass").click()