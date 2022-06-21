from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, driver):
        url = 'https://www.ozon.ru/'
        super().__init__(driver, url)
        driver.get(url)
        self.search_form = driver.find_element(By.XPATH, "//form[@action='/search']")
        self.main_menu = driver.find_elements(By.XPATH, "//ul[@data-widget='horizontalMenu']//a")
        self.catalog_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Каталог')]")
        self.catalog_menu = driver.find_elements(By.XPATH, "//div[@data-widget='catalogMenu']//a/span")
        self.logo_button = driver.find_element(By.XPATH, "//header/div[@id='stickyHeader']/div[1]/a[1]")
        self.top_bar = driver.find_elements(By.XPATH, '//div[@data-widget="topBar"]//a/span')
        self.search_field = driver.find_element(By.XPATH, '//input[@placeholder="Искать на Ozon"]')
        self.search_button = driver.find_element(By.XPATH, '//*[@aria-label="Поиск"]/..')
        self.result_table = driver.find_elements(By.XPATH, '//a[contains(@href, "/product/")]')
        self.btn_shoes = driver.find_element(By.XPATH, "//span[contains(text(),'Обувь')]")
        self.btn_texnika = driver.find_element(By.XPATH, "//span[contains(text(),'Бытовая техника')]")
        self.btn_apteka = driver.find_element(By.XPATH, "//span[contains(text(),'Аптека')]")
        self.btn_mebel = driver.find_element(By.XPATH, "//span[contains(text(),'Мебель')]")
        self.btn_igry = driver.find_element(By.XPATH, "//span[contains(text(),'Игры и консоли')]")

    def main_search_field(self, input_text):
        self.search_field.clear()
        self.search_field.send_keys(input_text)
        self.search_button.click()
