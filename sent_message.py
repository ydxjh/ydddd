from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def test1(self):
        self.driver.find_element_by_id('kw').send_keys('QQ邮箱')
        sleep(2)
        self.driver.find_element_by_id('su').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
        sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.switch_to.frame("login_frame")
        self.driver.find_element_by_xpath('//*[@id="qlogin_list"]/a').click()
        sleep(2)
        self.driver.find_element_by_id('composebtn').click()
        sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[3]/div[6]/iframe'))
        self.driver.find_element_by_xpath('/html/body/form[2]/div[2]/div[3]/div[2]/table[2]/tbody/tr/td[2]/div[1]/div[2]/input').send_keys("198624")
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="subject"]').send_keys("主题")
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[7]/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td/iframe"))
        self.driver.find_element_by_xpath('/html/body').send_keys("没有内容，发来玩玩")
        self.driver.switch_to.parent_frame()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/form[2]/div[3]/div/a[1]').click()
        sleep(2)
    def test2(self):
        self.driver.find_element_by_id('kw').send_keys('QQ邮箱')
        sleep(2)
        self.driver.find_element_by_id('su').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
        sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.switch_to.frame("login_frame")
        self.driver.find_element_by_xpath('//*[@id="qlogin_list"]/a').click()

    def tearDown(self):
        sleep(2)
        self.driver.quit()










