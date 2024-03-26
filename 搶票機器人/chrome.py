from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome()
                          
driver.get("https://course.nuk.edu.tw/Sel/login.asp")

alert = Alert(driver)
alert.accept() 

username_xpath = "/html/body/div/form/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/input[3]"
password_xpath = "/html/body/div/form/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/input[3]"

username_field = driver.find_element(By.XPATH, username_xpath)
password_field = driver.find_element(By.XPATH, password_xpath)

# 輸入您的帳號和密碼
username_field.send_keys('')
password_field.send_keys('')

button = driver.find_element(By.XPATH, "/html/body/div/form/table/tbody/tr[2]/td/input[1]")
button.click()

link = driver.find_element(By.XPATH, "/html/body/div/form/div/table/tbody/tr[5]/td[1]/a")
link.click()

WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "/html/frameset/frame[1]")))

button1 = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td/input[1]")
button1.click()

driver.switch_to.parent_frame()

WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "/html/frameset/frame[2]")))
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "/html/frameset/frame[1]")))

select_element = Select(driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td/select[2]"))
# 選擇 value 為 'MI' 的選項
select_element.select_by_value('CC') 

input("Press Enter to close the browser...")  # 等待使用者按 Enter 鍵
driver.quit() # 關閉瀏覽器視窗