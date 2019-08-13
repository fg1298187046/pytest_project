

import os,sys
sys.path.append(r'D:\\python自动化测试')
from PO.page.network_page import *
from PO.base_driver.dirver_init import base_driver


class Test_T:
    def setup(self):
        self.driver=base_driver()
        self.action = NetworkPage(self.driver)

    def test_network(self):
        import time

        self.action.find_mobile_network()
        time.sleep(2)
        self.action.switch_network()
       
    def test_network2(self):
        import time

        self.action.find_mobile_network()
        time.sleep(2)
        self.action.switch_network()
