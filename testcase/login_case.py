from page.login_page import LoginPage
from testcase import mytest


class LoginTest(mytest.Mytest):

    def test_login_sussful(self):
        """测试登录成功"""
        login=LoginPage(self.driver)
        login.openUrl()
        login.login("admin","admin123")