# C2-AUTOMATION_UI-E2E

Este repositorio unifica las suites de pruebas automatizadas para la validación de la interfaz gráfica y los flujos críticos de la aplicación Saucedemo. El objetivo de este proyecto es demostrar la coexistencia de múltiples stacks tecnológicos bajo el patrón de diseño **Screenplay**, garantizando pruebas altamente legibles, escalables y fáciles de mantener.

## 📂 Estructura del Proyecto

```text
C2-AUTOMATION_UI-E2E/
│
├── Jenkinsfile # Pipeline de CI/CD como Código
│
├── playwright-screenplay-framework/ # Ecosistema Python + Playwright
│   ├── conftest.py # Configuración global y habilidades 
│   ├── reporte.html # Reporte local autogenerado
│   ├── requirements.txt # Dependencias del entorno virtual
│   └── screenplay/
│       └── step_definitions/ # Definición de pasos Pytest-BDD
│           ├── test_ordenamiento.py
│           └── test_precios.py
│
└── serenity-screenplay-framework/ # Ecosistema Java + Serenity BDD
    ├── pom.xml
    └── src/
        └── test/
            ├── java/
            │   └── com/
            │       └── c2_automation/
            │           ├── CucumberTestSuite.java
            │           └── step_definitions/ # Definición de pasos Cucumber
            │               ├── comprar.java
            │               ├── destruir.java
            │               └── loginStepDefinitions.java
            └── resources/
                └── features/ # Archivos de especificación Gherkin
                    ├── comprar.feature
                    ├── destruccion.feature
                    └── login.feature
```

## 🛠️ Tecnologías Utilizadas

### Core de Pruebas
*   **Java Suite**: Java, Maven, Serenity BDD, Cucumber, Selenium WebDriver.
*   **Python Suite**: Python 3.12, Pytest, Pytest-BDD, Playwright, Screenpy-Playwright, Pytest-HTML.

### Orquestación e Infraestructura
*   **CI/CD**: Jenkins Pipelines (Declarative Pipeline).
*   **Navegadores**: Google Chrome / Chromium (Ejecución en modo Headless).

---

## 🏗️ Estructura del Monorepo

El proyecto está dividido en dos grandes componentes independientes:

### 1. Serenity Screenplay Framework (Java)
Ubicado en la carpeta `/serenity-screenplay-framework`. Gestiona flujos mediante especificaciones Cucumber tradicionales.
*   **Casos Automatizados**:
    *   `login.feature`: Verificación de acceso con usuarios del sistema.
    *   `comprar.feature`: Flujo completo de compra agregando múltiples productos al carrito y validando el checkout.
    *   `destruccion.feature`: Limpieza y restablecimiento del estado de la aplicación desde el menú lateral (`Reset App State`).

### 2. Playwright Screenplay Framework (Python)
Ubicado en la carpeta `/playwright-screenplay-framework`. Emplea `pytest-bdd` junto con las habilidades y actores provistos por `screenpy-playwright`.
*   **Casos Automatizados**:
    *   `test_ordenamiento.py`: Validación de filtros de ordenamiento de productos (alfabético, precios).
    *   `test_precios.py`: Verificación de consistencia en el catálogo de precios expuesto al usuario.

---

## 🚀 Ejecución Local

### Prerrequisitos
*   Java JDK 11 o superior instalado.
*   Apache Maven configurado en las variables de entorno.
*   Python 3.12+ instalado localmente.

### Ejecutar Suite de Java (Serenity)
1. Desplázate a la carpeta del framework:
   ```bash
   cd serenity-screenplay-framework
1. Ejecuta el comando de compilación y pruebas de Maven:
    ```bash
    mvn clean verify -U
1. El reporte detallado se generará en: `target/site/serenity/index.html.`

### Ejecutar Suite de Python (Playwright)
1. Desplázate a la carpeta del framework:
   ```bash
   cd playwright-screenplay-framework
1. Crea y activa un entorno virtual de Python:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
1. Instala las dependencias y los binarios de los navegadores:
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    python -m playwright install chromium
1. Ejecuta las pruebas generando el reporte autocontenido:
    ```bash
    pytest --html=report.html --self-contained-html

## 🤖 Integración Continua (Jenkins)
El ciclo de vida de este proyecto está automatizado mediante el archivo `Jenkinsfile`. El pipeline realiza las siguientes acciones de forma no interactiva:
1. Clona el repositorio desde la rama principal (main).
1. Entra a la subcarpeta de Java, ejecuta el siguiente comando que archiva de inmediato los reportes HTML nartivos de Serenity
    ```bash 
    mvn clean verify 
1. Crea un entorno virtual aislado `(venv_jenkins)`, instala de forma segura los binarios de chromium sin requerir elevación de privilegios `(sudo)`, ejecuta las pruebas con pytest y genera el reporte HTML.
1. Publica ambos reportes en la sección de artefactos del build y limpia el espacio de trabajo de Jenkins (cleanWs).

---

## 2. Detalles Técnicos de la Automatización y CI/CD

A efectos de mantenimiento para ingeniería, se deben tener en cuenta las siguientes consideraciones clave sobre el diseño del pipeline y las correcciones de dependencias aplicadas:

### Tabla de Equivalencias del Patrón Screenplay

| Concepto Screenplay | Implementación en Java (Serenity) | Implementación en Python (Screenpy) |
| :--- | :--- | :--- |
| **Actor** | `Actor actor = Actor.named("Diana");` | `actor = Actor.named("Diana")` |
| **Habilidad** | `BrowseTheWeb.with(hisBrowser)` | `BrowseTheWebSynchronously.using(browser)` |
| **Tareas / Acciones** | `Click.on(BUTTON)`, `Enter.theValue()` | `Click.on_the(BUTTON)`, `Enter.the_text()` |
| **Preguntas / Aseguramientos** | `seeThat(WebElementQuestion.the(TITLE), matches..)` | `actor.should( See.the(Text.of_the(TITLE), ReadsTheSameAs(...)) )` |

### Notas de Configuración Críticas para el Servidor Jenkins

*   **Instalación de Navegadores**: Durante el aprovisionamiento de la etapa de Python, el comando utilizado omitió intencionalmente el flag `--with-deps` (`python -m playwright install chromium`). Dado que el agente de Jenkins ya cuenta con las dependencias compartidas a nivel de sistema operativo debido a la ejecución previa de las pruebas de Chrome controladas por Selenium/WebDriver en la etapa de Serenity, la instalación se realiza de forma limpia en el espacio de usuario, evitando solicitudes interactivas de contraseñas de administración (`sudo`).
*   **Reportes Autocontenidos**: El uso de `--self-contained-html` en la ejecución de `pytest` garantiza que todos los recursos gráficos (CSS, JS embebidos) se unifiquen en el archivo `report.html`. Esto evita pérdidas de estilos cuando Jenkins sirve el artefacto guardado desde su interfaz web.