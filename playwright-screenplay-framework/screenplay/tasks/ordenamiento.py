from screenpy import Actor
from screenpy_playwright.actions import Select
from screenpy_playwright.actions import Click, Enter
from screenplay.user_interfaces.home_privado import homePrivado as InventoryUI

class Ordenamiento:
    @staticmethod
    def por_criterio(criterio: str):
        return Ordenamiento(criterio)

    def __init__(self, criterio: str):
        self.criterio = criterio

    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            Select.the_option(self.criterio).from_(InventoryUI.DRP_SORT)
        )