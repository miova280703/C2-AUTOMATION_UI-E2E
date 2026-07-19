import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page

# Clases Core de ScreenPy y resoluciones de aserción
from screenpy import Actor, See
from screenpy.resolutions import IsEqualTo
from screenpy_playwright.abilities.browse_the_web_synchronously import BrowseTheWebSynchronously

# Componentes de nuestro modelo Screenplay
from screenplay.tasks.login import Login
from screenplay.tasks.seleccionar_productos_aleatorios import SeleccionarProductosAleatorios
from screenplay.tasks.checkout import Checkout
from screenplay.questions.total_correcto import SubtotalEnPantalla

# Carga el archivo de características correspondiente
scenarios('../../features/precios.feature')

@pytest.fixture
def actor(browser): # <-- Cambiamos 'page' por 'browser'
    # Instanciamos la habilidad directamente pasándole el navegador completo
    tester = Actor.named("Diana").who_can(BrowseTheWebSynchronously(browser))
    return tester

@given('que el usuario se encuentra en la página de inicio de sesión de saucedemo')
def step_open_saucedemo(actor):
    # La navegación inicial ocurre directamente al ejecutar la tarea de Login
    pass

@given(parsers.parse('realiza la autenticación con las credenciales "{username}" y "{password}"'))
def step_login(actor, username, password):
    actor.attempts_to(Login.con_credenciales(username, password))

@when(parsers.parse('el usuario agrega "{quantity}" productos aleatorios al carrito guardando sus precios'))
def step_add_random_products(actor, quantity):
    actor.attempts_to(SeleccionarProductosAleatorios.cantidad_de(int(quantity)))

@when('completa el checkout con los datos correctos')
def step_go_to_step_2(actor):
    actor.attempts_to(Checkout.ahora())

@then('el subtotal del pedido debería coincidir con la suma de los precios guardados en memoria')
def step_verify_subtotal(actor):
    # Recuperamos los datos de la memoria integrada del actor
    precios_originales = actor.precios_guardados
    suma_esperada = sum(precios_originales)
    
    # Ejecutamos la aserción fluida de ScreenPy
    actor.should(
        See.the(SubtotalEnPantalla.valor(), IsEqualTo(suma_esperada))
    )