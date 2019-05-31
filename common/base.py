from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

class Base():
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def findElement(self, locator):
        if not isinstance(locator, tuple):
            print("参数类型必须为元组，例如('id','value1')")
        else:
            print("正在查找元素，查找类型%s，对应值为%s" % (locator[0], locator[1]))
            a = self.driver.find_element(*locator)

            try:
                ele = WebDriverWait(self.driver, self.timeout)\
                    .until(lambda x: x.find_element(*locator))
                return ele
            except:
                return ''

    def move_to_element(self, locator):

        ele = self.findElement(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def select_by_index(self, locator, index=0):

        ele = self.findElement(locator)
        res = Select(ele).select_by_index(index)

    def select_by_value(self, locator, value):

        ele = self.findElement(locator)
        res = Select(ele).select_by_value(value)

    def select_by_text(self, locator, text):
        ele = self.findElement(locator)
        res = Select(ele).select_by_visible_text(text)

    def is_scroll_top(self):
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def is_scroll_down(self, x=0):
        js = "window.scrollTo(%s,document.body.scrollHeight)"% x
        self.driver.execute_script(js)

    def is_scroll_view(self, locator):
        ele = self.findElement(locator)
        js = "arguments[0].scrollIntoView()"
        self.driver.execute_script(js, ele)

    def click(self, locator):
        ele = self.findElement(locator)
        ele.click()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    # driver.get("http://www.baidu.com")
    # base1 = Base(driver)
    # locator = ('link text', '设置')
    # base1.move_to_element (locator)


    driver.get("https://blog.csdn.net/u011541946/article/details/70184079")
    driver.maximize_window()
    locator = ("xpath",'//*[@id="mainBox"]/main/div[4]/div[10]/div')
    locator1 = ("link text","展开阅读全文")
    base2 = Base(driver)
    base2.click(locator1)
    base2.is_scroll_down(100)