from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
    #打开在线待办事项应用
        self.browser.get('http://localhost:8000')

        #网页的标题和头部都包含“to-do”这个词
        self.assertIn('to-do',self.browser.title)
        self.fail('finish the test')


        #在一个文本框中输入购买孔雀羽毛

        #选择爱好是使用假绳做钓鱼饵

        #回车后，页面更新了

        #待办事项表格中显示了1：buy peacock feathers

        #页面中显示了一个文本框，可以输入其他的待办事项

        #输入'use peacock feathers to make a fly'

        #页面再次更新，清单中显示了这两个待办事项

        #网站生成了一个唯一的url

        #页面中有一些文字解说这个功能

        #点击那个url，发现待办事项列表依然还在

        #很满意

        browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')