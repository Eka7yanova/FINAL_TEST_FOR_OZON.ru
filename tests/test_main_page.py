import pytest
from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_logo_button_visible(driver):
    """Проверяем наличие логотипа OZON"""
    page = MainPage(driver)
    assert page.logo_button.is_displayed()


def test_catalog_button_visible(driver):
    """Проверяем наличие кнопки КАТАЛОГ"""
    page = MainPage(driver)
    assert page.catalog_button.is_displayed()


def test_search_form_visible(driver):
    """Проверяем наличие формы поиска на странице"""
    page = MainPage(driver)
    assert page.search_form.is_displayed()


def test_catalog_menu_clickable(driver):
    """Проверяем корректность работы каталога"""
    page = MainPage(driver)
    page.catalog_button.click()
    page.btn_shoes.click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Обувь"
    assert page.get_relative_link() == '/category/obuv-17777/'
    driver.implicitly_wait(3)


def test_catalog_menu_clickable_tehnika(driver):
    """Проверяем корректность работы каталога"""
    page = MainPage(driver)
    page.catalog_button.click()
    page.btn_texnika.click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Бытовая техника"
    assert page.get_relative_link() == '/category/bytovaya-tehnika-10500/'
    driver.implicitly_wait(3)


def test_catalog_menu_clickable_apteka(driver):
    """Проверяем корректность работы каталога"""
    page = MainPage(driver)
    page.catalog_button.click()
    page.btn_apteka.click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Аптека"
    assert page.get_relative_link() == '/category/apteka-6000/'
    driver.implicitly_wait(3)


def test_catalog_menu_clickable_mebel(driver):
    """Проверяем корректность работы каталога"""
    page = MainPage(driver)
    page.catalog_button.click()
    page.btn_mebel.click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Мебель"
    assert page.get_relative_link() == '/category/mebel-15000/'
    driver.implicitly_wait(3)


def test_catalog_menu_clickable_igpy(driver):
    """Проверяем корректность работы каталога"""
    page = MainPage(driver)
    page.catalog_button.click()
    page.btn_igry.click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Игры и консоли"
    assert page.get_relative_link() == '/category/igry-i-soft-13300/'
    driver.implicitly_wait(3)


@pytest.mark.parametrize('name', ['Музыка'], ids={'Music'})
def test_check_main_search(driver, name):
    """Проверяем корректность работы формы поиска"""
    page = MainPage(driver)
    assert page.search_field.is_displayed()
    page.main_search_field(name)
    assert driver.find_element(By.XPATH, "//a[contains(text(),'Рок')]")


@pytest.mark.parametrize('name', ['TOP Fashion', 'Premium', 'Билеты и Отели', 'Ozon fresh', 'Ozon Счёт', 'Рассрочка',
                                  'Акции', 'Бренды', 'Express', 'Электроника', 'Одежда и обувь', 'Детские товары',
                                  'Дом и сад', 'Зона лучших цен'
                                  ],
                         ids=['top', 'premium', 'tickets', 'fresh', 'ozon', 'instalments', 'stocks', 'brands',
                              'express', 'electronica', 'clothes', 'kids', 'home', 'super prise'])
def test_main_menu_visible(driver, name):
    """Проверяем корректность отображения основного меню"""
    page = MainPage(driver)
    menu = []
    for i in range(len(page.main_menu)):
        menu.append(page.main_menu[i].text)
    assert name in menu


@pytest.mark.parametrize('name', ['Аксессуары', 'Музыка и видео', 'Алкогольная продукция', 'Спорт и отдых'],
                         ids=['Accessories', 'Music', 'Alcohol', 'Sport'])
def test_catalog_menu(driver, name):
    """Проверяем наличие категорий товаров в каталоге"""
    page = MainPage(driver)
    page.catalog_button.click()
    catalog = []
    for i in range(len(page.catalog_menu)):
        catalog.append(page.catalog_menu[i].text)
    assert name in catalog


@pytest.mark.parametrize('name', ['Ozon для бизнеса', 'Мобильное приложение', 'Пункты выдачи'],
                         ids=['Business', 'Mobile', 'Points'])
def test_top_bar(driver, name):
    """Проверяем корректность работы ссылок верхней плашкe меню"""
    page = MainPage(driver)
    top_bar_links = page.top_bar
    top_bar = []
    for i in range(len(top_bar_links)):
        top_bar.append(top_bar_links[i].text)
    assert name in top_bar
    for i in range(len(top_bar_links)):
        action = ActionChains(driver)
        action.context_click(top_bar_links[i]).perform()
        driver.switch_to.window(driver.window_handles[1])
        assert 'ozon' in page.get_url()
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
