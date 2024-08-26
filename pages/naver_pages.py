from .base_page import BasePage
from selenium.webdriver.common.by import By


class NaverMainPage(BasePage):
    URL = "https://www.naver.com"

    def load(self):
        self.driver.get(self.URL)
        self.wait_for_element(By.CSS_SELECTOR, "input#query")
        return self

    def is_loaded(self):
        return "NAVER" in self.get_page_title()


class NaverNewsPage(BasePage):
    URL = "https://news.naver.com"

    def load(self):
        self.driver.get(self.URL)
        return self

    def is_loaded(self):
        return "네이버 뉴스" in self.get_page_title()


class NaverSportsPage(BasePage):
    URL = "https://sports.news.naver.com"

    def load(self):
        self.driver.get(self.URL)
        return self

    def is_loaded(self):
        return "네이버 스포츠" in self.get_page_title()
