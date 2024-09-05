import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage

# logger 설정
logger = logging.getLogger(__name__)

class NaverMainPage(BasePage):
    URL = "https://www.naver.com"

    def load(self):
        """네이버 메인 페이지를 로드합니다."""
        logger.info("Loading Naver main page.")
        self.driver.get(self.URL)
        self.wait_for_element(By.CSS_SELECTOR, "input#query")
        return self

    def is_loaded(self):
        """네이버 메인 페이지가 로드되었는지 확인합니다."""
        return "NAVER" in self.get_page_title()

    def is_element_present(self, by, locator):
        """지정한 요소가 페이지에 있는지 확인합니다."""
        try:
            self.wait_for_element(by, locator)
            return True
        except TimeoutException:
            logger.warning(f"Element with locator {locator} not found on the page.")
            return False

    def click_element(self, by, locator):
        """지정한 요소를 클릭합니다."""
        if self.is_element_present(by, locator):
            element = self.driver.find_element(by, locator)
            element.click()
        else:
            raise Exception(f"Element with locator {locator} is not present on the page.")

    def is_cafe_icon_present(self):
        """네이버 메인 페이지에 카페 아이콘이 있는지 확인합니다."""
        return self.is_element_present(By.XPATH, '//span[@class="service_icon type_cafe"]')

    def click_cafe_icon(self):
        """카페 아이콘을 클릭합니다."""
        self.click_element(By.XPATH, '//span[@class="service_icon type_cafe"]')

    def is_cafe_page_loaded(self):
        """카페 페이지로 이동했는지 확인합니다."""
        return WebDriverWait(self.driver, 10).until(EC.url_contains("https://section.cafe.naver.com/ca-fe/home"))

    def is_cafe_town_menu_present(self):
        """카페 타운 메뉴가 있는지 확인합니다."""
        return self.is_element_present(By.XPATH, '//*[@id="gnbMenu"]/a[2]')

    def click_cafe_town_menu(self):
        """카페 타운 메뉴를 클릭합니다."""
        self.click_element(By.XPATH, '//*[@id="gnbMenu"]/a[2]')

    def is_cafe_town_page_loaded(self):
        """카페 이웃 페이지로 이동했는지 확인합니다."""
        logger.info("Checking if the cafe town page is loaded.")
        return WebDriverWait(self.driver, 10).until(EC.url_contains("cafe.naver.com/ca-fe/home/town/talks"))

    def click_cafe_town_tab_menu(self):
        """카페 타운 탭 메뉴를 클릭하고 예상되는 메뉴를 확인합니다."""
        try:
            tab_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="category_flicker"]'))
            )
            menu_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//*[@id="category_flicker"]/button'))
            )

            expected_texts = [
                "전체", "질문", "동네생활정보", "맛집,카페", "일상", "찾습니다", "건강,운동", "육아,교육"
            ]
            for index, menu_element in enumerate(menu_elements):
                actual_text = menu_element.text.strip()
                expected_text = expected_texts[index]

                if actual_text == expected_text:
                    menu_element.click()
                    time.sleep(1)
                    logger.info(f"Menu {index + 1} matches: {actual_text}")
                else:
                    logger.warning(f"Menu {index + 1} mismatch. Found: {actual_text}, Expected: {expected_text}")
        except Exception as e:
            logger.error(f"Error while interacting with the cafe town tab menu: {e}")
            raise
        finally:
            logger.info("Cafe town tab menu interaction completed.")


class NaverNewsPage(BasePage):
    URL = "https://news.naver.com"

    def load(self):
        """네이버 뉴스 페이지를 로드합니다."""
        logger.info("Loading Naver news page.")
        self.driver.get(self.URL)
        return self

    def is_loaded(self):
        """네이버 뉴스 페이지가 로드되었는지 확인합니다."""
        return "네이버 뉴스" in self.get_page_title()


class NaverSportsPage(BasePage):
    URL = "https://sports.news.naver.com"

    def load(self):
        """네이버 스포츠 페이지를 로드합니다."""
        logger.info("Loading Naver sports page.")
        self.driver.get(self.URL)
        return self

    def is_loaded(self):
        """네이버 스포츠 페이지가 로드되었는지 확인합니다."""
        return "네이버 스포츠" in self.get_page_title()
