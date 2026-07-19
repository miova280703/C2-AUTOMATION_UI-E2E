import random
from screenpy import Actor
from screenpy_playwright.abilities.browse_the_web_synchronously import BrowseTheWebSynchronously

class SeleccionarProductosAleatorios:
    def __init__(self, quantity: int):
        self.quantity = quantity

    @staticmethod
    def cantidad_de(quantity: int):
        return SeleccionarProductosAleatorios(quantity)

    def perform_as(self, the_actor: Actor) -> None:
        page = the_actor.ability_to(BrowseTheWebSynchronously).pages[0]
        
        all_items = page.locator(".inventory_item").all()
        selected_items = random.sample(all_items, self.quantity)
        
        precios = []
        for item in selected_items:
            price_text = item.locator(".inventory_item_price").text_content()
            price_value = float(price_text.replace("$", "").strip())
            precios.append(price_value)
            
            item.locator("button[id^='add-to-cart']").click()
            
        the_actor.precios_guardados = precios