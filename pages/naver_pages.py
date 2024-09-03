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
            return True
        except TimeoutException:
            print('is_cafe_icon_present timeout')
            return False

    def is_cafe_town_menu_present(self):
        """네이버 카페 페이지에 이웃 메뉴가 있는지 확인합니다."""
        try:
            self.wait_for_element(By.XPATH, '//*[@id="gnbMenu"]/a[2]')
            return True
        except TimeoutException:
            print('is_cafe_town_menu_present timeout')
            return False

    def click_cafe_icon(self):
        """네이버 메인 페이지에서 카페 아이콘을 클릭합니다."""
        if self.is_cafe_icon_present():
            cafe_icon = self.driver.find_element(By.XPATH, '//span[@class="service_icon type_cafe"]')
            cafe_icon.click()
        else:
            raise Exception("Cafe icon is not present on the page.")

    def is_cafe_page_loaded(self):
        # """카페 페이지로 이동했는지 확인합니다."""
        return WebDriverWait(self.driver, 10).until(EC.url_contains("https://section.cafe.naver.com/ca-fe/home"))

    def click_cafe_town_menu(self):
            """네이버 메인 페이지에서 카페 아이콘을 클릭합니다."""
            if self.is_cafe_town_menu_present():
                cafe_town_icon = self.driver.find_element(By.XPATH, '//*[@id="gnbMenu"]/a[2]')
                cafe_town_icon.click()
            else:
                raise Exception("Cafe icon is not present on the page.")


    def is_cafe_town_page_loaded(self):
        print("카페 이웃 페이지로 이동했는지 확인합니다.")
        return WebDriverWait(self.driver, 10).until(EC.url_contains("cafe.naver.com/ca-fe/home/town/talks"))

    def click_cafe_town_tab_menu_present(self):
        # 탭의 존재 여부를 확인
        wait = WebDriverWait(self.driver, 10)
        tab_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="category_flicker"]')))

        try:
            if tab_element:
                menu_elements = wait.until(
                    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="category_flicker"]/button')))

                # 예상되는 메뉴 텍스트 리스트
                expected_texts = [
                    "전체",
                    "질문",
                    "동네생활정보",
                    "맛집,카페",
                    "일상",
                    "찾습니다",
                    "건강,운동",
                    "육아,교육"
                ]

                # 각 메뉴 텍스트 확인
                all_menus_match = True  # 일치 여부를 추적하는 변수

                for index, menu_element in enumerate(menu_elements):
                    actual_text = menu_element.text.strip()  # 실제 텍스트
                    expected_text = expected_texts[index]  # 예상 텍스트

                    if actual_text == expected_text:
                        # time.sleep(1)
                        menu_element.click()
                        time.sleep(1)
                        print(f"Menu {index + 1} matches: {actual_text}")
                    else:
                        print(f"Menu {index + 1} does not match. Found: {actual_text}, Expected: {expected_text}")
                        all_menus_match = False

                if all_menus_match:
                    print("All menu texts match the expected values.")
                else:
                    print("Some menu texts do not match the expected values.")
        except Exception as e:
            raise Exception(e)
        finally:
            # 드라이버 종료
            print('finally')


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
