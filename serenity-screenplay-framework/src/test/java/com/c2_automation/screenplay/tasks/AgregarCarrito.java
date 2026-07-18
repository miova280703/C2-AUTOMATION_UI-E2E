package com.c2_automation.screenplay.tasks;

import net.serenitybdd.annotations.Step;
import net.serenitybdd.screenplay.Actor;
import net.serenitybdd.screenplay.Task;
import net.serenitybdd.screenplay.Tasks;
import net.serenitybdd.screenplay.actions.Click;
import com.c2_automation.screenplay.ui.homePrivado;
import java.util.List;

public class AgregarCarrito implements Task {
    private final List<String> productos;

    public AgregarCarrito(List productos){
        this.productos = productos;
    }

    public static AgregarCarrito losProductos(List productos){
        return Tasks.instrumented(AgregarCarrito.class, productos);
    }

    @Override
    @Step("{0} agrega productos al carrito de compras")
    public <T extends Actor> void performAs(T actor){
        for (String producto : this.productos){
            actor.attemptsTo(Click.on(homePrivado.btnAgregarProducto.of(producto)));
        }
        actor.attemptsTo(Click.on(homePrivado.btnCarritoCompras));
    }
}
