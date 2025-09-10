from odoo import models, fields, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)


class CrmLead(models.Model):
    _inherit = "crm.lead"

    crm_order_line_ids = fields.One2many(
        "crm.order.line", "lead_id", string="Order Lines"
    )
    company_currency = fields.Many2one(
        "res.currency",
        related="company_id.currency_id",
        string="Company Currency",
        readonly=True
    )
    sale_order_id = fields.Many2one("sale.order", string="Quotation", readonly=True)

    def action_new_quotation(self):
        self.ensure_one()

        # Prepare context as in original method
        context = self._prepare_opportunity_quotation_context()
        context['search_default_opportunity_id'] = self.id

        # Create quotation manually, using prepared context values
        sale_order = self.env['sale.order'].with_context(context).create({
            'partner_id': self.partner_id.id,
            'opportunity_id': self.id,
            'company_id': self.company_id.id,
            'team_id': self.team_id.id if self.team_id else False,
            'user_id': self.user_id.id if self.user_id else False,
        })

        # Copy CRM lines
        if self.crm_order_line_ids:
            sale_order.write({
                'order_line': [(0, 0, {
                    'product_id': l.product_id.id,
                    'product_uom_qty': l.product_uom_qty,
                    'product_uom': l.product_uom.id,
                    'price_unit': l.price_unit,
                    'name': l.product_id.display_name,
                }) for l in self.crm_order_line_ids]
            })

        self.sale_order_id = sale_order.id

        # Open form for the created quotation
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'res_id': sale_order.id,
            'view_mode': 'form',
            'views': [(self.env.ref('sale.view_order_form').id, 'form')],
            'target': 'current',
        }
