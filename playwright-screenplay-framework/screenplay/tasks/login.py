from screenpy import Actor
from screenpy_playwright.actions import Open, Enter, Click
from screenplay.user_interfaces.login_form import LoginForm as LoginUI

class Login:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        
    @staticmethod
    def con_credenciales(username, password):
        return Login(username, password)

    def perform_as(self, actor: Actor) -> None:
        actor.attempts_to(
            Open("https://www.saucedemo.com/"),
            Enter.the_text(self.username).into(LoginUI.TXT_USERNAME),
            Enter.the_text(self.password).into(LoginUI.TXT_PASSWORD),
            Click.on(LoginUI.BTN_LOGIN),
        )
        if hasattr(actor, "screenshot"):
            actor.screenshot("Paso: Credenciales ingresadas")