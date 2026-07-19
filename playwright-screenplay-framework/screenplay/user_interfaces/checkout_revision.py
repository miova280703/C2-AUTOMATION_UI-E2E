from screenpy_playwright import Target

class checkoutRevision:
    SUBTOTAL_LABEL = Target.the("etiqueta de subtotal").located_by(".summary_subtotal_label")
    TAX_LABEL = Target.the("etiqueta de impuestos").located_by(".summary_tax_label")
    TOTAL_LABEL = Target.the("etiqueta de total").located_by(".summary_total_label")
