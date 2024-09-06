import time

import allure
import pytest
from selenium import webdriver

from pages.naver_pages import NaverMainPage
from pages.naver_pages import NaverNewsPage
from pages.naver_pages import NaverSportsPage


# @allure.title("[MainPage] 테스트 시작")
@pytest.fixture(scope="class")
# setup 함수를 테스트 클래스 단위로 한 번만 실행
def setup(request):
    # Selenium의 크롬 웹드라이버를 초기화
    driver = webdriver.Chrome()

    # 테스트 클래스(TestNaverPages)에서 driver 객체에 접근할 수 있도록 함
    request.cls.driver = driver

    # 이전에 있는 코드는 테스트 시작 전에 실행되고, yield 이후의 코드는 테스트가 모두 끝난 후에 실행
    yield
    driver.quit()


@pytest.mark.usefixtures("setup")
# 클래스 내의 모든 테스트 메서드에서 setup이 적용된 상태로 테스트가 실행
class TestNaverPages:

    @allure.story("Naver Main Page")
    def test_naver_main_page(self):
        main_page = NaverMainPage(self.driver)
        main_page.load()
        assert main_page.is_loaded()

    def test_click_cafe_icon(self):
        main_page = NaverMainPage(self.driver)
        main_page.load()

        assert main_page.is_cafe_icon_present(), "Cafe icon should be present on the main page."
        main_page.click_cafe_icon()

        self.driver.switch_to.window(self.driver.window_handles[1])
        assert main_page.is_cafe_page_loaded(), "Should navigate to the Naver Cafe page."

    def test_naver_news_page(self):
        news_page = NaverNewsPage(self.driver)
        news_page.load()
        assert news_page.is_loaded()

    def test_naver_sports_page(self):
        sports_page = NaverSportsPage(self.driver)
        sports_page.load()
        assert sports_page.is_loaded()

    def test_click_cafe_town_menu(self):
        main_page = NaverMainPage(self.driver)
        main_page.load()

        assert main_page.is_cafe_icon_present(), "Cafe icon should be present on the main page."
        main_page.click_cafe_icon()

        self.driver.switch_to.window(self.driver.window_handles[-1])
        main_page.click_cafe_town_menu(), "Should navigate to the Naver Cafe page."
        self.driver.switch_to.window(self.driver.window_handles[-1])

        assert main_page.is_cafe_town_page_loaded(), 'Should town page'
        time.sleep(3)


    def test_town_tab_menu(self):
        main_page = NaverMainPage(self.driver)
        main_page.load()

        assert main_page.is_cafe_icon_present(), "Cafe icon should be present on the main page."
        main_page.click_cafe_icon()

        self.driver.switch_to.window(self.driver.window_handles[-1])
        main_page.click_cafe_town_menu(), "Should navigate to the Naver Cafe page."
        self.driver.switch_to.window(self.driver.window_handles[-1])

        assert main_page.is_cafe_town_page_loaded(), 'Should town page'

        main_page.click_cafe_town_tab_menu()

