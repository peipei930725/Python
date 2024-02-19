from selenium import webdriver
driver = webdriver.Chrome('C:\Users\peipe\OneDrive\桌面\chromedriver\chromedriver.exe')
driver.get('https://www.google.com/')

# 定位搜尋框
element = driver.find_element_by_class_name(“gLFyf.gsfi”)
# 傳入字串
element.send_keys(“Selenium Python”)