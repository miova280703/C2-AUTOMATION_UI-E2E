from screenpy_playwright import Target

class homePrivado:
    
    DRP_SORT = Target.the("selector de ordenamiento de productos").located_by('[data-test="product-sort-container"]')
    
    LST_PRODUCT_NAMES = Target.the("lista de nombres de productos").located_by('[data-test="inventory-item-name"]')
    
    LST_PRODUCT_PRICES = Target.the("lista de precios de productos").located_by('[data-test="inventory-item-price"]')
    
    CART_ICON = Target.the("icono del carrito de compras").located_by(".shopping_cart_link")
    
    