package com.c2_automation.stepdefinitions;

import io.cucumber.java.es.*;
import net.serenitybdd.screenplay.ensure.Ensure;
import com.c2_automation.screenplay.ui.homePrivado;
import com.c2_automation.screenplay.tasks.AgregarCarrito;
import net.serenitybdd.screenplay.actors.OnStage;
import com.c2_automation.screenplay.tasks.Checkout;
import com.c2_automation.screenplay.questions.compraConfirmacion;

import java.util.Arrays;

import static net.serenitybdd.screenplay.GivenWhenThen.*;
import static org.hamcrest.Matchers.equalTo;

public class comprar {
    @Cuando("el usuario agrega los productos {string} y {string} al carrito")
    public void elUsuarioAgregaLosProductosAlCarrito(String producto1, String producto2){
        OnStage.theActorInTheSpotlight().attemptsTo(
                AgregarCarrito.losProductos(Arrays.asList(producto1,producto2))
        );

        OnStage.theActorInTheSpotlight().attemptsTo(
                Ensure.that(homePrivado.contador).text().isEqualTo("2")
        );
    }

    @Y("completa el checkout con los datos {string}, {string} y {string}")
    public void completaElCheckoutConLosDatos(String firstName, String lastName, String zipcode){
        OnStage.theActorInTheSpotlight().attemptsTo(
                Checkout.check(firstName,lastName,zipcode)
        );
    }

    @Entonces("debería de ver el mensaje de confirmación {string}")
    public void deberiaDeVerElMensajeDeConfirmacion(String mensajeEsperado){
        OnStage.theActorInTheSpotlight().should(
                seeThat(compraConfirmacion.es(), equalTo(mensajeEsperado))
        );
    }
}
