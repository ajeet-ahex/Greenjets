from odoo import models, fields ,api

class CrmOrderLine(models.Model):
    _name = "crm.order.line"
    _description = "CRM Order Line"

    lead_id = fields.Many2one("crm.lead", string="Opportunity", ondelete="cascade")
    product_id = fields.Many2one("product.product", string="Product", required=True)
    product_uom_qty = fields.Float(string="Quantity", default=1.0)
    product_uom = fields.Many2one(
        "uom.uom", string="Unit of Measure",
        related="product_id.uom_id", store=True, readonly=True
    )

    price_unit = fields.Float(string="Unit Price")
    price_subtotal = fields.Monetary(
        string="Subtotal",
        compute="_compute_price_subtotal",
        store=True
    )
    currency_id = fields.Many2one(
        "res.currency",
        related="lead_id.company_currency",
        store=True,
        readonly=True
    )

    @api.onchange("product_id", "product_uom_qty", "price_unit")
    def _onchange_product_or_qty(self):
        if self.product_id:
            # Auto-fill from product
            self.product_uom = self.product_id.uom_id
            if not self.price_unit:  # only fill if unit price not set
                self.price_unit = self.product_id.list_price

    @api.depends("product_uom_qty", "price_unit")
    def _compute_price_subtotal(self):
        for line in self:
            line.price_subtotal = line.product_uom_qty * line.price_unit




