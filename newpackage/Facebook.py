from selenium import webdriver
import time

browser='Chrome'
if browser=='Chrome':
    driver=webdriver.Chrome(executable_path="E:/chromedriver/chromedriver.exe")
elif browser=='FF':
    driver=webdriver.Firefox(executable_path="E:/chromedriver/chromedriver.exe")
elif browser=='Ie':
    driver=webdriver.Ie(executable_path="E:\chromedriver/IEDriverServer.exe")
driver.get("https://www.monsterindia.com/")
time.sleep(5)
driver.maximize_window()
driver.find_element_by_css_selector("#themeDefault > section:nth-child(2) > div > div > div > div.search-content-holder.pr > div.row.search-content > div.col-lg-5 > div > div:nth-child(1) > div > div.signinModal > a").click()




