from selenium.webdriver.common.by import By


class HomeBakeryPage:
    def __init__(self, browser):
        self.browser = browser

    def open_honey_roll_recipe(self):
        honey_roll = self.browser.find_element(By.CSS_SELECTOR, "a[href='http://ugotowac.blogspot.com/2015/05/buki-na-miodzie.html']")
        honey_roll.click()
