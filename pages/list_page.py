import re
from .base_page import BasePage


class ListPage(BasePage):

    MIN_PRICE = 'input[placeholder*="От"]'
    MAX_PRICE = 'input[placeholder*="До"]'
    PRICE_ITEMS = '[data-testid="price"]'
    ITEM_CARDS = '[data-testid="item"]'
    URGENT_BADGE = 'text=Срочно'

    def set_min_price(self, value):
        self.fill(self.MIN_PRICE, value)
        self.wait_for_update()

    def set_max_price(self, value):
        self.fill(self.MAX_PRICE, value)
        self.wait_for_update()

    def wait_for_update(self):
        # базовое ожидание (можно заменить на loader/network)
        self.page.wait_for_timeout(800)

    def get_prices(self):
        texts = self.page.locator(self.PRICE_ITEMS).all_text_contents()
        prices = []

        for text in texts:
            clean = re.sub(r"[^\d]", "", text)
            if clean:
                prices.append(int(clean))

        return prices

    def toggle_urgent(self):
        self.page.locator('label:has-text("🔥 Только срочные")').click()
        self.wait_for_update()

    def get_items(self):
        return self.page.locator(self.ITEM_CARDS)

    def has_urgent_only(self):
        items = self.get_items()
        for i in range(items.count()):
            if not items.nth(i).locator(self.URGENT_BADGE).is_visible():
                return False
        return True
