from pages.list_page import ListPage

BASE_URL = "https://cerulean-praline-8e5aa6.netlify.app"


def test_min_price_filter(page):
    page_obj = ListPage(page)
    page_obj.open(BASE_URL)
    page_obj.set_min_price("1000")
    prices = page_obj.get_prices()

    assert len(prices) > 0, "Нет объявлений"
    assert all(p >= 1000 for p in prices)


def test_max_price_filter(page):
    page_obj = ListPage(page)
    page_obj.open(BASE_URL)

    page_obj.set_max_price("10000")
    prices = page_obj.get_prices()

    assert len(prices) > 0
    assert all(p <= 10000 for p in prices)


def test_sort_price(page):
    page_obj = ListPage(page)
    page_obj.open(BASE_URL)

    page.locator("select").nth(0).select_option(label="Цене")
    page.locator("select").nth(1).select_option(label="По возрастанию")
    page.keyboard.press("Enter")
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(500)

    page_obj.wait_for_update()

    prices = page_obj.get_prices()

    assert len(prices) > 0, "Список пуст, проверьте локаторы в list_page.py"
    assert prices == sorted(prices), f"Сортировка не сработала. Получено: {prices}"


def test_urgent_filter(page):
    page_obj = ListPage(page)
    page_obj.open(BASE_URL)

    page_obj.toggle_urgent()

    assert page_obj.get_items().count() > 0
    assert page_obj.has_urgent_only(), "Есть не срочные объявления"
