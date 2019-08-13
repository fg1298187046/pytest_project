from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self,driver):
        self.driver=driver

    def find_element(self,loc,timeout=10,poll=0.5):
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x:x.find_element(*loc))

    def find_elements(self,loc,timeout=10,poll=0.5):
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def click_element(self, loc):
        # 元组类型 (By.XPATH，"xpath语句") (By.ID, "id属性值")
        self.find_element(loc).click()

    # 输入
    def input_element(self, loc, text):
        """
        :param text: 输入内容
        """
        self.find_element(loc).send_keys(text)