package com.c2_automation.screenplay.ui;
import net.serenitybdd.screenplay.targets.Target;
import org.openqa.selenium.By;

public class registrarCompra {
    public static final Target btnCheckout =
            Target.the("btn_checkout").located(By.id("checkout"));

    public static final Target inputFirstName =
            Target.the("input_First name").located(By.id("first-name"));

    public static final Target inputLastName =
            Target.the("input_Last name").located(By.id("last-name"));

    public static final Target inputPostalCode =
            Target.the("input_Postal code").located(By.id("postal-code"));

    public static final Target btnContinue =
            Target.the("btn_continue").located(By.id("continue"));

    public static final Target btnFinish =
            Target.the("btn_finish").located(By.id("finish"));
}
