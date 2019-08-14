import os, sys

import pytest

sys.path.append(r'D:\\python自动化测试')
from PO.page.search_page import *
from PO.base_driver.dirver_init import base_driver
from PO.base_driver.base_yaml import find_yaml_data


class Test_Search(object):

    # def setup(self):
    #     self.driver = base_driver()
    #     self.page = Search_Page(self.driver)

    @pytest.mark.parametrize('args', find_yaml_data('yaml_data', 'data'))
    def test_click(self,args):
        # self.page.input_search()
        print(args['username'],args['password'])
