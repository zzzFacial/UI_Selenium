import unittest
from model.driver import browser_chrome

class Mytest(unittest.TestCase):
    """测试类基类"""


    def setUp(self):
        self.driver=browser_chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
