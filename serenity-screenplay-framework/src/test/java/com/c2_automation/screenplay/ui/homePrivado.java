package com.c2_automation.screenplay.ui;
import net.serenitybdd.screenplay.targets.Target;
import org.openqa.selenium.By;


public class homePrivado {
    public static final Target btnAgregarProducto =
            Target.the("btn_agregar_producto").
                    locatedBy("//div[text()='{0}']/ancestor::div[@class='inventory_item']//button");

    public static final Target btnCarritoCompras =
            Target.the("btn_carrito compras").located(By.className("shopping_cart_link"));

    public static final Target btnMenuHamburguesa =
            Target.the("btn_menu_hamburguesa").located(By.id("react-burger-menu-btn"));

    public static final Target optionRestablecer =
            Target.the("option_reset").located(By.id("reset_sidebar_link"));

    public static final Target contador =
            Target.the("contador_carrito").locatedBy(".shopping_cart_badge");
}

