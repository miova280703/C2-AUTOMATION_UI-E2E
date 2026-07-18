package com.c2_automation.screenplay.tasks;

import net.serenitybdd.annotations.Step;
import net.serenitybdd.screenplay.Actor;
import net.serenitybdd.screenplay.Task;
import net.serenitybdd.screenplay.Tasks;
import net.serenitybdd.screenplay.actions.Enter;
import net.serenitybdd.screenplay.actions.Click;
import com.c2_automation.screenplay.ui.loginForm;

public class Login implements Task {
    private final String usr;
    private final String pwd;

    public Login(String usr, String pwd){
        this.usr = usr;
        this.pwd = pwd;
    }

    public static Login conCredenciales(String usr, String pwd){
        return Tasks.instrumented(Login.class, usr, pwd);
    }

    @Override
    @Step("{0} inicia sesión con credenciales validas")
    public <T extends Actor> void performAs(T actor){
        actor.attemptsTo(
                Enter.theValue(usr).into(loginForm.USERNAME_FIELD),
                Enter.theValue(pwd).into(loginForm.PASSWORD_FIELD),
                Click.on(loginForm.LOGIN_BUTTON)
        );
    }
}
