from selenium import webdriver

try:
    driver = webdriver.Chrome()  # 初始化Chrome WebDriver
    print("Selenium 正确安装！")
except Exception as e:
    print("Selenium 安装失败：", e)
