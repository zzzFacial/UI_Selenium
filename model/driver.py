from selenium import webdriver

def browser_chrome():
    """启动chrome浏览器"""
    driver=webdriver.Chrome()
    return driver