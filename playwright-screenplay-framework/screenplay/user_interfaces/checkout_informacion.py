from screenpy_playwright import Target

class checkoutInformacion:
    FIRST_NAME = Target.the("campo nombre").located_by("id=first-name")
    LAST_NAME = Target.the("campo apellido").located_by("id=last-name")
    POSTAL_CODE = Target.the("campo código postal").located_by("id=postal-code")
    CONTINUE_BUTTON = Target.the("botón continuar").located_by("id=continue")