# language: es
Característica: Selección aleatoria de productos y validación de checkout

  Antecedentes:
    Dado que el usuario se encuentra en la página de inicio de sesión de saucedemo
    Y realiza la autenticación con las credenciales "standard_user" y "secret_sauce"

  @validacion_precio
  Escenario: Validación exitosa de precios con productos aleatorios
    Cuando el usuario agrega "3" productos aleatorios al carrito guardando sus precios
    Y completa el checkout con los datos correctos
    Entonces el subtotal del pedido debería coincidir con la suma de los precios guardados en memoria