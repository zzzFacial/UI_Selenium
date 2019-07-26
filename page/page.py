class Page(object):
    '''页面类基类'''
    base_url="http://localhost/v0.5.5"

    def __init__(self,driver,url=base_url):
        self.driver=driver
        self.timeout=30
        self.url=url


    def openUrl(self):
        """打开url"""
        driver=self.driver.get(self.url)
        self.driver.implicitly_wait(self.timeout)#设置隐性等待
        return driver


    def find_element(self,loc):
        return self.driver.find_element(*loc)