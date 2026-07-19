# language: es
Característica: Ordenamiento de los productos

  Antecedentes:
    Dado que el usuario se encuentra en la página de inicio de sesión de saucedemo
    Y realiza la autenticación con las credenciales "standard_user" y "secret_sauce"

  @ordenamiento
  Escenario: Aplicar los filtros para ordenar los productos
    Cuando el usuario selecciona un filtro para ordenar los productos
    Entonces los productos se ordenan y se muestran de esa manera