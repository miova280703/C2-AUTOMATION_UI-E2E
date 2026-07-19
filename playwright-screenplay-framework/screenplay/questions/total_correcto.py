import re
from screenpy import Actor
from screenpy_playwright.questions import Text
from screenplay.user_interfaces.checkout_revision import checkoutRevision as CheckoutStep2UI

class SubtotalEnPantalla:
    @staticmethod
    def valor():
        return SubtotalEnPantalla()

    def answered_by(self, the_actor: Actor) -> float:
        texto_subtotal = Text.of_the(CheckoutStep2UI.SUBTOTAL_LABEL).answered_by(the_actor)
        
        match = re.search(r"\$(\d+\.\d+)", texto_subtotal)
        if match:
            return float(match.group(1))
        return 0.0