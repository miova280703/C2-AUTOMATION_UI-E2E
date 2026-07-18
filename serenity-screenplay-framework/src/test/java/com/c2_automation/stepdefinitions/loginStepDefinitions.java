package com.c2_automation.stepdefinitions;

import io.cucumber.java.Before;
import io.cucumber.java.es.Dado;
import io.cucumber.java.es.Y;
import net.serenitybdd.screenplay.actions.Open;
import net.serenitybdd.screenplay.actors.OnStage;
import net.serenitybdd.screenplay.actors.OnlineCast;
import com.c2_automation.screenplay.tasks.Login;

import static net.serenitybdd.screenplay.actors.OnStage.theActorCalled;
import static net.serenitybdd.screenplay.actors.OnStage.theActorInTheSpotlight;

public class loginStepDefinitions {

    @Before
    public void preparEscenario(){
        OnStage.setTheStage(new OnlineCast());
    }

    @Dado("el usuario se encuentra en la página de inicio de sesión de saucedemo")
    public void elUsuarioSeEncuentraEnLaPaginaDeInicioDeSesionDeSaucedemo() {
        theActorCalled("Diana").wasAbleTo(Open.url("https://www.saucedemo.com/"));
    }

    @Y("realiza la autenticación con las credenciales usuario {string} y contraseña {string}")
    public void realizaLaAutenticacionConLasCredencialesUsuarioYContraseña(String usr, String pwd){
        theActorInTheSpotlight().attemptsTo(Login.conCredenciales(usr, pwd));
    }
}
