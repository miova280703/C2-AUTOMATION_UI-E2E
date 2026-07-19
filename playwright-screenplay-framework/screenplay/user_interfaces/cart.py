from screenpy_playwright import Target

class cart:
    CHECKOUT_BUTTON = Target.the("botón de checkout").located_by("id=checkout")