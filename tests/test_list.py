from pages.list_page import ListPage

BASE_URL = "https://cerulean-praline-8e5aa6.netlify.app/list"


def test_min_price_filter(page):
    page_obj = ListPage(page)
    page_obj.open(BASE_URL)

    page_obj.set_min_price("100")
    prices = page_obj.get_prices()

    assert len(prices) > 0, "Нет объявлений"
    assert all(p >= 100 for p in prices)


def test_max_price_filter(page):
    page_obj = ListPage(page)
    page_obj.open(BASE_URL)

    page_obj.set_max_price("500")
    prices = page_obj.get_prices()

    assert len(prices) > 0
    assert all(p <= 500 for p in prices)


def test_sort_price(page):
    page_obj = ListPage(page)
    page_obj.open(BASE_URL)

    page.select_option("select", "asc")
    page.wait_for_timeout(800)

    prices = page_obj.get_prices()

    assert prices == sorted(prices)


def test_urgent_filter(page):
    page_obj = ListPage(page)
    page_obj.open(BASE_URL)

    page_obj.toggle_urgent()

    assert page_obj.get_items().count() > 0
    assert page_obj.has_urgent_only(), "Есть не срочные объявления"
