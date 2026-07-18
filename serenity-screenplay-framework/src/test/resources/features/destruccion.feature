# language: es
Característica: Destrucción de productos en el carrito

  Antecedentes:
    Dado el usuario se encuentra en la página de inicio de sesión de saucedemo
    Y realiza la autenticación con las credenciales usuario "standard_user" y contraseña "secret_sauce"
    Y el usuario agrega los productos "Sauce Labs Backpack" y "Test.allTheThings() T-Shirt (Red)" al carrito

  @destruccion
  Escenario: destrucción exitosa de los productos en el carrito
    Cuando hace clic en el menú lateral seleccionando la opción "Rest App State"
    Entonces el contador del carrito debe volver a estar vacío
