package com.c2_automation.screenplay.tasks;

import net.serenitybdd.annotations.Step;
import net.serenitybdd.screenplay.Actor;
import net.serenitybdd.screenplay.Task;
import net.serenitybdd.screenplay.Tasks;
import net.serenitybdd.screenplay.actions.Click;
import com.c2_automation.screenplay.ui.homePrivado;
import net.serenitybdd.screenplay.actions.Enter;

public class DestruirCompra implements Task {
    public static DestruirCompra destruccion(){
        return Tasks.instrumented(DestruirCompra.class);
    }

    @Override
    @Step("{0} destruir compra")
    public <T extends Actor> void performAs(T actor){
        actor.attemptsTo(
                Click.on(homePrivado.btnMenuHamburguesa),
                Click.on(homePrivado.optionRestablecer)
        );
    }
}
