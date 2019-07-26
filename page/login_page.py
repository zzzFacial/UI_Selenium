from selenium.webdriver.common.by import By
from .page import Page
from screenshot import Screenshot

class LoginPage(Page):
    """登录页面类"""

    #定位器
    login_username_text_loc=(By.NAME,"name")
    login_passwoed_text_loc=(By.NAME,"password")
    login_button_loc=(By.NAME,"submit")



    def login_username(self,text):
        """用户名输入框"""
        self.find_element(self.login_username_text_loc).clear()
        self.find_element(self.login_username_text_loc).send_keys(text)


    def login_password(self,text):
        """密码输入框"""
        self.find_element(self.login_passwoed_text_loc).clear()
        self.find_element(self.login_passwoed_text_loc).send_keys(text)

    def login_button(self):
        """登录按钮"""
        self.find_element(self.login_button_loc).click

    @Screenshot.screenshot()
    def login(self,username,password):
        self.login_username(username)
        self.login_password(password)
        self.login_button()