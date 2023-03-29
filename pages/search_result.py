from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SearchResultPage:

    def __init__(self, browser):
        self.browser = browser

    def wait_for_load(self):
        wait = WebDriverWait(self.browser, 10)
        grey_status_bar = (By.CLASS_NAME, 'status-msg-body')
        wait.until(expected_conditions.presence_of_element_located(grey_status_bar))

    #def verify_post_count(self, post_count):
        #titles = self.browser.find_elements(By.CLASS_NAME, 'post-title')
        #assert len(titles) == post_count



