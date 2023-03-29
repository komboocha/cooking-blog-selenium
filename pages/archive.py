from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ArchivePage:

    def __init__(self, browser):
        self.browser = browser

    def wait_for_load(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(expected_conditions.url_contains('2021'))

    #def verify_post_count(self, post_count):
        #titles = self.browser.find_elements(By.CLASS_NAME, 'post-title')
        #assert len(titles) == post_count
