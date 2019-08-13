import os,sys

import pytest

sys.path.append(r'D:\\python自动化测试')
from PO.page.search_page import *
from PO.base_driver.dirver_init import base_driver
from PO.base_driver.base_yaml import find_yaml_data


def data_with_key(key):
    return find_yaml_data('yaml_data')[key]

class Test_Search(object):

    def setup(self):
        self.driver = base_driver()
        self.page=Search_Page(self.driver)

    @pytest.mark.parametrize('keys',data_with_key('data'))
    def test_click(self,keys):
        self.page.input_search()
        self.page.send_text(text=keys)




