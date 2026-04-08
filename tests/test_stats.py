import re
from playwright.sync_api import expect


BASE_URL = "https://cerulean-praline-8e5aa6.netlify.app"


def test_refresh_button(page):
    page.goto(BASE_URL)
    page.click('a[href="/stats"]')
    page.wait_for_load_state("networkidle")

    value_loc = page.locator('[class*="_value_"]').first
    value_loc.wait_for()
    old_val = value_loc.text_content()

    # Кликаем "Обновить"
    page.get_by_role("button", name="Обновить").click()

    # Даем сайту время (некоторые сервера обновляют статистику не мгновенно)
    page.wait_for_timeout(2000)

    # Проверяем, что текст СТАЛ другим (не "не должен быть старым", а именно изменился)
    new_val = value_loc.text_content()
    assert old_val != new_val, f"Значение не обновилось, осталось {old_val}"


def test_stop_timer(page):
    page.goto(BASE_URL)
    page.click('text=Статистика')
    page.wait_for_load_state("networkidle")

    # Вместо текста с эмодзи используем класс кнопки
    # Находим кнопку по классу и нажимаем на неё
    toggle_btn = page.locator('[class*="_toggleButton_"]')

    # Кликаем для остановки (если таймер шел)
    toggle_btn.click()

    # Проверяем, что кнопка перешла в состояние готовности к старту
    # (Обычно меняется aria-label или title)
    expect(toggle_btn).to_have_attribute("title", re.compile("Включить", re.IGNORECASE))

def test_start_timer(page):
    page.goto(BASE_URL)
    page.click('text=Статистика')
    page.wait_for_load_state("networkidle")

    toggle_btn = page.locator('[class*="_toggleButton_"]')

    # Сначала гарантируем, что таймер СТОИТ (title должен быть "Включить...")
    if "Отключить" in (toggle_btn.get_attribute("title") or ""):
        toggle_btn.click()

    # Теперь нажимаем "Старт"
    toggle_btn.click()

    # Проверяем, что теперь кнопка предлагает "Отключить" (значит таймер запущен)
    expect(toggle_btn).to_have_attribute("title", re.compile("Отключить", re.IGNORECASE))
