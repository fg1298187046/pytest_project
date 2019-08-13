



class Search_Page:
    def __init__(self,driver):
        self.driver=driver

    def input_search(self):
        self.driver.find_element_by_id('com.android.settings:id/search').click()

    def send_text(self,text):
        self.driver.find_element_by_id('android:id/search_src_text').send_keys(text)