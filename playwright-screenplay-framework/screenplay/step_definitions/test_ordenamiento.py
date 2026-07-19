import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page

# Clases Core de ScreenPy y resoluciones de aserción
from screenpy import Actor, See
from screenpy.resolutions import IsEqualTo
from screenpy_playwright.abilities.browse_the_web_synchronously import BrowseTheWebSynchronously

# Componentes de nuestro modelo Screenplay
from screenplay.tasks.login import Login
from screenplay.tasks.ordenamiento import Ordenamiento

# Carga el archivo de características correspondiente
scenarios('../../features/ordenamiento.feature')

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

@when("el usuario selecciona un filtro para ordenar los productos")
def selecciona_filtro(actor):
    # Usamos 'lohi' (Price low to high) como el filtro de prueba
    actor.attempts_to(Ordenamiento.por_criterio("lohi"))

@then("los productos se ordenan y se muestran de esa manera")
def verificar_productos_ordenados(actor):
    page = actor.ability_to(BrowseTheWebSynchronously).pages[0]
    precios_texto = page.locator("[data-test='inventory-item-price']").all_text_contents()
    
    # 2. Limpiamos el caracter '$' y los convertimos a flotantes para poder comparar matemáticamente
    precios_obtenidos = [float(p.replace("$", "")) for p in precios_texto]
    
    # 3. Validamos que la lista original sea idéntica a una lista ordenada de menor a mayor
    precios_esperados = sorted(precios_obtenidos)
    assert precios_obtenidos == precios_esperados, f"El orden no es correcto. Esperado: {precios_esperados}, Obtenido: {precios_obtenidos}"
    
