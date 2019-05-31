import unittest
from common import HTMLTestRunner_cn

casePath = 'C:\\Users\\PC\\PycharmProjects\\web_auto\\case'
rule = "test*.py"

discover = unittest.defaultTestLoader.discover(start_dir=casePath, pattern=rule)

reportPath = "C:\\Users\\PC\\PycharmProjects\\web_auto\\report"+"\\report.html"
fp = open(reportPath, "wb")

runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                          title='报告的title',
                                          description='报告的description',
                                          retry=1)

runner.run(discover)

fp.close()

'''
'defaultTestLoader':测试用例加载器，其包括多个加载测试用例的方法。返回一个测试套件

测试套件收集测试用例，discover方法加载多个测试用例的集合

discover = unittest.defaultTestLoader.discover(start_dir=casePath, pattern=rule) #返回一个测试套件
fp=fopen(reportPath+"\\report.html", 'wb')
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title='', description='')
runner.run(discover)
'''
