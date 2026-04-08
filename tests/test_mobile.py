def test_theme_switch(page):
    page.set_viewport_size({"width": 375, "height": 812})
    page.goto("https://cerulean-praline-8e5aa6.netlify.app")

    body_before = page.locator("body").get_attribute("class")

    page.click("button")

    page.wait_for_timeout(500)

    body_after = page.locator("body").get_attribute("class")

    assert body_before != body_after, "Тема не переключилась"
