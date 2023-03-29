from selenium.webdriver.common.by import By


class AboutMePage:

    def __init__(self, browser):
        self.browser = browser

    def verify_facebook_link(self):
        facebook_link = self.browser.find_element(By.LINK_TEXT, 'fanpage')
        assert facebook_link.get_attribute('href') == 'https://www.facebook.com/ugotowac?ref=hl'

    def verify_instagram_link(self):
        instagram_link = self.browser.find_element(By.LINK_TEXT, 'instagram')
        assert instagram_link.get_attribute('href') == 'https://www.instagram.com/mariola_blog_ugotowac/'

