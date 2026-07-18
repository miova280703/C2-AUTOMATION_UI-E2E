package com.c2_automation.screenplay.tasks;

import net.serenitybdd.annotations.Step;
import net.serenitybdd.screenplay.Actor;
import net.serenitybdd.screenplay.Task;
import net.serenitybdd.screenplay.Tasks;
import net.serenitybdd.screenplay.actions.Click;
import com.c2_automation.screenplay.ui.registrarCompra;
import net.serenitybdd.screenplay.actions.Enter;

public class Checkout implements Task {
    private final String firstName;
    private final String lastName;
    private final String zipCode;

    public Checkout(String firstName, String lastName, String zipCode){
        this.firstName = firstName;
        this.lastName = lastName;
        this.zipCode = zipCode;
    }

    public static Checkout check(String firstName, String lastName, String zipCode){
        return Tasks.instrumented(Checkout.class, firstName, lastName, zipCode);
    }

    @Override
    @Step("{0} completar formulario checkout")
    public <T extends Actor> void performAs(T actor){
        actor.attemptsTo(
                Click.on(registrarCompra.btnCheckout),
                Enter.theValue(firstName).into(registrarCompra.inputFirstName),
                Enter.theValue(lastName).into(registrarCompra.inputLastName),
                Enter.theValue(zipCode).into(registrarCompra.inputPostalCode),
                Click.on(registrarCompra.btnContinue),
                Click.on(registrarCompra.btnFinish)
        );
    }
}
