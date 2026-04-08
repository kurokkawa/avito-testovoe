BASE_URL = "https://cerulean-praline-8e5aa6.netlify.app/stats"


def test_refresh_button(page):
    page.goto(BASE_URL)

    old_content = page.locator("._value_s99h9_85").first.text_content()

    page.click("text=Обновить")
    page.wait_for_timeout(1000)

    new_content = page.locator("._value_s99h9_85").first.text_content()

    assert old_content != new_content, "Страница не обновилась"


def test_stop_timer(page):
    page.goto(BASE_URL)

    page.click("text=Стоп")

    disabled = page.locator("text=Старт").is_enabled()

    assert disabled, "Кнопка старт должна быть доступна после стопа"


def test_start_timer(page):
    page.goto(BASE_URL)

    page.click("text=Старт")

    # Проверяем, что кнопка реально нажалась (например стала disabled)
    is_disabled = not page.locator("text=Старт").is_enabled()

    assert is_disabled, "Кнопка старт не изменила состояние"
