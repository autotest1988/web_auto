"""
unittest框架(可以用作单元测试/自动化测试)

目的：keep the bar green to the code clear

功能测试用例包含的列：功能点，用例编号，测试输入（操作步骤），期望结果，测试结果pass/fail
自动化测试用例包含的列：测试类，编号，前置条件，操作步骤（查找元素），测试输入，检查点，后置条件（后置是为了不影响下个测试用例的执行），测试结果pass/fail


 每条测试用例必须是独立的，不依赖其他用例
 每个Testcase都必须有断言assert-----自动化测试的灵魂

"""
#coding:utf-8

from selenium import webdriver
import time
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        print("先打开浏览器")
        self.driver = webdriver.Chrome()
        self.driver.get('')

    def tearDown(self):
        print("关闭浏览器")
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def is_login(self):
        try:
            res = self.driver.find_element_by_xpath('//div[@id="usermenu"]/a').text()
            return res

        except:
            return ''

    def test_01(self):
        print("111111111111111111")

        time.sleep(2)

        self.driver.find_element_by_id('account').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('123456')
        self.driver.find_element_by_id('submit').click()
        time.sleep(2)
        # 判断是否登陆成功
        res = self.is_login()
        print(res)

        self.assertTrue(res == 'admin')

    def test_02(self):
        print("22222222222222")

        time.sleep(2)

        self.driver.find_element_by_id('account').send_keys('admin111')
        self.driver.find_element_by_name('password').send_keys('123456')
        self.driver.find_element_by_id('submit').click()
        time.sleep(2)
        # 判断是否登陆成功
        res = self.is_login()
        print(res)

        self.assertTrue(res == '')




if __name__ == '__main__':
    unittest.main()
    print("test")


