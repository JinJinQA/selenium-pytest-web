import time

from selenium.webdriver.common.selenium_manager import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

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

    def is_cafe_icon_present(self):
        """네이버 메인 페이지에 카페 아이콘이 있는지 확인합니다."""
        try:
            self.wait_for_element(By.XPATH, '//span[@class="service_icon type_cafe"]')
            # self.wait_for_element(By.CSS_SELECTOR, "a.nav.cafe")
            return True
        except TimeoutException:
            print('is_cafe_icon_present timeout')
            return False

    def is_cafe_town_menu_present(self):
        """네이버 카페 페이지에 이웃 메뉴가 있는지 확인합니다."""
        try:
            self.wait_for_element(By.XPATH, '//*[@id="gnbMenu"]/a[2]')
            # self.wait_for_element(By.CSS_SELECTOR, "a.nav.cafe")
            return True
        except TimeoutException:
            print('is_cafe_town_menu_present timeout')
            return False

    def click_cafe_icon(self):
        """네이버 메인 페이지에서 카페 아이콘을 클릭합니다."""
        if self.is_cafe_icon_present():
            cafe_icon = self.driver.find_element(By.XPATH, '//span[@class="service_icon type_cafe"]')
            # cafe_icon = self.driver.find_element(By.CSS_SELECTOR, "a.nav.cafe")
            cafe_icon.click()
        else:
            raise Exception("Cafe icon is not present on the page.")

    def is_cafe_page_loaded(self):
        """카페 페이지로 이동했는지 확인합니다."""
        print("카페 페이지로 이동했는지 확인합니다.")
        # self.wait_for_element(By.CSS_SELECTOR, "div.cafe_home")
        # self.wait_for_element(By.XPATH, '//*[@id="gnbMenu"]/a[1]')
        # return "카페" in self.get_page_title() or "cafe.naver.com" in self.driver.current_url
        return WebDriverWait(self.driver, 10).until(EC.url_contains("https://section.cafe.naver.com/ca-fe/home"))

    def click_cafe_town_menu(self):
            """네이버 메인 페이지에서 카페 아이콘을 클릭합니다."""
            if self.is_cafe_town_menu_present():
                cafe_town_icon = self.driver.find_element(By.XPATH, '//*[@id="gnbMenu"]/a[2]')
                # cafe_icon = self.driver.find_element(By.CSS_SELECTOR, "a.nav.cafe")
                cafe_town_icon.click()
                print('1111')
            else:
                print('2222')
                raise Exception("Cafe icon is not present on the page.")


    def is_cafe_town_page_loaded(self):
        print("카페 이웃 페이지로 이동했는지 확인합니다.")
        print(self.get_page_title())
        current_url = self.driver.current_url
        print(f"현재 페이지의 URL: {current_url}")

        # 계속 실패함
        return WebDriverWait(self.driver, 10).until(EC.url_contains("cafe.naver.com/ca-fe/home/town/talks"))


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
