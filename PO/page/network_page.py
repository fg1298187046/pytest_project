import os,sys
sys.path.append(os.getcwd())
from appium import webdriver

class NetworkPage:
    def __init__(self,driver):
        self.driver=driver

    def find_mobile_network(self):
        self.driver.find_element_by_xpath("//*[@text='双卡与移动网络']").click()

    def switch_network(self):
        self.driver.find_element_by_id("android:id/switch_widget").click()

