package com.c2_automation.screenplay.ui;

import net.serenitybdd.screenplay.targets.Target;
import org.openqa.selenium.By;

public class finalizarCompra {
    public static final Target h2Mensaje =
            Target.the("h2_mensaje").located(By.xpath("//h2[@class='complete-header' and text()='Thank you for your order!']"));

    public static final Target btnBackHome =
            Target.the("btn_back home").located(By.id("back-to-products"));
}
