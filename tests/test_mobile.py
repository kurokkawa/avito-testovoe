def test_theme_switch(page):
    page.set_viewport_size({"width": 375, "height": 812})
    page.goto("https://cerulean-praline-8e5aa6.netlify.app")

    theme_before = page.locator("html").get_attribute("data-theme")

    page.click("._themeToggle_127us_1")

    page.wait_for_timeout(500)

    theme_after = page.locator("html").get_attribute("data-theme")

    assert theme_before != theme_after, (
        f"Тема не переключилась в атрибуте data-theme. "
        f"Было: '{theme_before}', стало: '{theme_after}'"
    )
