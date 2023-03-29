from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, browser):
        self.find_newest_post = None
        self.browser = browser

    def verify_post_count(self):
        titles = self.browser.find_elements(By.CLASS_NAME, 'post-title')
        list_of_titles = []
        for title in titles:
            list_of_titles.append(title)
        assert len(titles) == len(list_of_titles)

    def search(self, search_term):
        search_bar = self.browser.find_element(By.ID, 'sbox')
        search_bar.send_keys(search_term + Keys.ENTER)

    def click_on_label(self, label):
        label = self.browser.find_element(By.LINK_TEXT, label)
        label.click()

    def open_first_post(self):
        post_titles = self.browser.find_elements(By.CLASS_NAME, 'post-title')
        post_titles[0].click()

    def click_on_image(self, image):
        image = self.browser.find_element(By.ID, image)
        image.click()








