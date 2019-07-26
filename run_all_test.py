import unittest,time
from HTMLTestRunner import HTMLTestRunner
#from model.function import send_mail

#定义测试用例目录
test_dir="./testcase"
test_report="./report"

#组织测试用例

discover=unittest.defaultTestLoader.discover(test_dir,pattern="*_case.py")

if __name__=='__main__':

    times=time.strftime("%Y%m%d%H%M%S")
    #组装测试报告路径和文件名
    report_file=test_report+"/WkCRM"+times+"result.html"
    file=open(report_file,'wb')
    runner=HTMLTestRunner(stream=file,title="悟空CRM自动化测试报告",description="运行环境：windows 10, Chrome")

    #执行测试
    runner.run(discover)
    file.close()