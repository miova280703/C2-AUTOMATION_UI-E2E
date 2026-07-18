package com.c2_automation.screenplay.ui;
import net.serenitybdd.screenplay.targets.Target;
import org.openqa.selenium.By;

public class loginForm {
    public static final Target USERNAME_FIELD =
            Target.the("campo username").located(By.id("user-name"));

    public static final Target PASSWORD_FIELD =
            Target.the("campo password").located(By.id("password"));

    public static final Target LOGIN_BUTTON =
            Target.the("boton iniciar sesion").located(By.id("login-button"));

    public static final Target PRODUCTS_TITLE =
            Target.the("titulo productos").located(By.xpath("//span[contains(@class,'title') and text()='roducts']"));
}
