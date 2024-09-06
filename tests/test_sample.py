import time

import allure
import pytest
from selenium import webdriver

import utils.conf as conf
from pages.sample_pages import SampleMainPage


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
class TestSamplePages:

    @allure.story("Naver Main Page")
    def test_naver_main_page(self):
        print(conf.shortcut_email)
        main_page = SampleMainPage(self.driver)
        main_page.load()
        assert main_page.is_loaded()
