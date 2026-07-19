import base64
import pytest
from screenpy_playwright.abilities import BrowseTheWebSynchronously
from pytest_html import extras

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook de pytest optimizado para extraer fixtures en entornos pytest-bdd
    e inyectar capturas base64 compatibles con pytest-html 4.x.
    """
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call":
        actor = None
        
        # SOLUCIÓN 1: Ir al contexto interno de la solicitud (_request) 
        # para extraer el fixture del actor usado en los steps de BDD.
        if hasattr(item, "_request"):
            try:
                actor = item._request.getfixturevalue("actor")
            except Exception:
                pass
        
        # Respaldo en caso de que esté declarado de forma clásica
        if not actor:
            actor = item.funcargs.get("actor")
            
        if actor:
            try:
                # Extraemos la página activa de la habilidad del actor
                page = actor.ability_to(BrowseTheWebSynchronously).pages[0]
                
                # Tomamos la captura en memoria y la codificamos
                screenshot_bytes = page.screenshot()
                screenshot_base64 = base64.b64encode(screenshot_bytes).decode("utf-8")
                
                pytest_html = item.config.pluginmanager.getplugin("html")
                if pytest_html:
                    if not hasattr(report, "extras"):
                        report.extras = []
                    
                    # SOLUCIÓN 2: En lugar de usar .image(), insertamos un tag <img> 
                    # puro vía .html() para garantizar que renderice directo en las filas del reporte.
                    html_img = (
                        f'<div style="margin-top: 10px;">'
                        f'<p style="margin:0 0 5px 0; font-weight:bold; color:#4caf50;">Evidencia Visual:</p>'
                        f'<img src="data:image/png;base64,{screenshot_base64}" '
                        f'style="width:600px; max-width:100%; height:auto; border:1px solid #e6e6e6; border-radius:4px;"/>'
                        f'</div>'
                    )
                    report.extras.append(pytest_html.extras.html(html_img))
                    
            except Exception as e:
                print(f"\n[⚠️ Alerta Conftest] No se pudo capturar la pantalla: {e}")