package com.c2_automation.stepdefinitions;

import io.cucumber.java.es.Cuando;
import io.cucumber.java.es.Entonces;
import net.serenitybdd.screenplay.ensure.Ensure;
import com.c2_automation.screenplay.ui.homePrivado;
import com.c2_automation.screenplay.tasks.AgregarCarrito;
import net.serenitybdd.screenplay.actors.OnStage;
import com.c2_automation.screenplay.tasks.DestruirCompra;
import com.c2_automation.screenplay.questions.compraConfirmacion;

public class destruir {
    @Cuando("hace clic en el menú lateral seleccionando la opción {string}")
    public void haceClicEnElMenuLateralSeleccionadoLaOpcion(String opcion){
        OnStage.theActorInTheSpotlight().attemptsTo(
                DestruirCompra.destruccion()
        );
    }

    @Entonces("el contador del carrito debe volver a estar vacío")
    public void elContadorDelCarritoDebeVolverAEstarVacio(){
        OnStage.theActorInTheSpotlight().attemptsTo(
                Ensure.that(homePrivado.contador).isNotDisplayed()
        );
    }
}
