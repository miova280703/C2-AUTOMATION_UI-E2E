from screenpy import Actor
from screenpy_playwright.actions import Click, Enter
from screenplay.user_interfaces.home_privado import homePrivado as InventoryUI
from screenplay.user_interfaces.cart import cart as CartUI
from screenplay.user_interfaces.checkout_informacion import checkoutInformacion as CheckoutStep1UI

class Checkout:
    @staticmethod
    def ahora():
        return Checkout()

    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            Click.on(InventoryUI.CART_ICON),
            Click.on(CartUI.CHECKOUT_BUTTON),
            Enter.the_text("Diana").into(CheckoutStep1UI.FIRST_NAME),
            Enter.the_text("Flores").into(CheckoutStep1UI.LAST_NAME),
            Enter.the_text("01007").into(CheckoutStep1UI.POSTAL_CODE),
            Click.on(CheckoutStep1UI.CONTINUE_BUTTON),
        )