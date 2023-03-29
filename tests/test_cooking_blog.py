import pytest
from selenium.webdriver import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.aboutme import AboutMePage
from pages.archive import ArchivePage
from pages.home import HomePage
from pages.homebakery import HomeBakeryPage
from pages.new_comment import NewComment
from pages.search_result import SearchResultPage


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    browser = Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
    browser.get('http://ugotowac.blogspot.com/')
    yield browser
    browser.quit()


def test_post_count(browser):
    home_page = HomePage(browser)
    home_page.verify_post_count()


def test_post_count_after_search(browser):
    home_page = HomePage(browser)
    home_page.search('pizza')

    search_result_page = SearchResultPage(browser)
    search_result_page.wait_for_load()

    home_page.verify_post_count()


def test_post_count_on_2021_label(browser):
    home_page = HomePage(browser)
    home_page.click_on_label('2021')

    archive_page = ArchivePage(browser)
    archive_page.wait_for_load()

    home_page.verify_post_count()


def test_social_links_on_about_me(browser):
    home_page = HomePage(browser)
    home_page.click_on_label('O mnie...')

    about_me_page = AboutMePage(browser)
    about_me_page.verify_facebook_link()
    about_me_page.verify_instagram_link()


def test_comment_count_on_new_post(browser):
    home_page = HomePage(browser)
    home_page.click_on_label('Brownie z kremem twarogowym nadziane owocami leśnymi')

    new_comment_page = NewComment(browser)
    new_comment_page.verify_comments_count()


def test_comments_on_first_post_are_displayed(browser):
    home_page = HomePage(browser)
    home_page.open_first_post()

    new_comment_page = NewComment(browser)
    new_comment_page.comments_are_displayed()


def test_verify_recipe(browser):
    home_page = HomePage(browser)
    home_page.click_on_image('Image9_img')

    home_bakery_page = HomeBakeryPage(browser)
    home_bakery_page.open_honey_roll_recipe()
