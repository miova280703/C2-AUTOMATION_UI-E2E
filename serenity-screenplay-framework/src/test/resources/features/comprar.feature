# language: es
Característica: Comprar un producto

  Antecedentes:
    Dado el usuario se encuentra en la página de inicio de sesión de saucedemo
    Y realiza la autenticación con las credenciales usuario "standard_user" y contraseña "secret_sauce"

  @comprar
  Escenario: Compra exitosa con múltiples productos
    Cuando el usuario agrega los productos "Sauce Labs Backpack" y "Test.allTheThings() T-Shirt (Red)" al carrito
    Y completa el checkout con los datos "Diana", "Flores" y "01007"
    Entonces debería de ver el mensaje de confirmación "Thank you for your order!"
