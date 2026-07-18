package com.c2_automation.screenplay.questions;

import net.serenitybdd.screenplay.Actor;
import net.serenitybdd.screenplay.Question;
import net.serenitybdd.screenplay.questions.Text;
import com.c2_automation.screenplay.ui.loginForm;

public class loginQuestion implements Question<String>{
    public static loginQuestion es() {
        return new loginQuestion();
    }

    @Override
    public String answeredBy(Actor actor){
        return Text.of(loginForm.PRODUCTS_TITLE).answeredBy(actor);
    }
}
