from selenium.webdriver.common.by import By


class NewComment:
    def __init__(self, browser):
        self.browser = browser

    def verify_comments_count(self):
        comments = self.browser.find_elements(By.CLASS_NAME, 'comment-block')
        list_of_comments = []
        for comment in comments:
            list_of_comments.append(comment)
        assert len(comments) == len(list_of_comments)

    def comments_are_displayed(self):
        comment = self.browser.find_element(By.CSS_SELECTOR, 'h4')
        assert comment.is_displayed()
