package com.c2_automation;
import io.cucumber.junit.CucumberOptions;
import net.serenitybdd.cucumber.CucumberWithSerenity;
import org.junit.runner.RunWith;

@RunWith(CucumberWithSerenity.class)
@CucumberOptions(
        plugin = {"pretty"},
        features = "src/test/resources/features",
        glue = "com.c2_automation.stepdefinitions",
        snippets = CucumberOptions.SnippetType.CAMELCASE
)
public class CucumberTestSuite {
}
