package com.c2_automation.screenplay.questions;

import net.serenitybdd.screenplay.Actor;
import net.serenitybdd.screenplay.Question;
import net.serenitybdd.screenplay.questions.Text;
import com.c2_automation.screenplay.ui.finalizarCompra;

public class compraConfirmacion implements Question {
    public static compraConfirmacion es(){
        return new compraConfirmacion();
    }

    @Override
    public String answeredBy(Actor actor){
        return Text.of(finalizarCompra.h2Mensaje).answeredBy(actor).trim();
    }
}
