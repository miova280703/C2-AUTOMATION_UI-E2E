from screenpy_playwright import Target

class LoginForm:
    TXT_USERNAME = Target.the("campo de usuario").located_by("[data-test='username']")
    TXT_PASSWORD = Target.the("campo de contraseña").located_by("[data-test='password']")
    BTN_LOGIN = Target.the("botón de inicio de sesión").located_by("[data-test='login-button']")