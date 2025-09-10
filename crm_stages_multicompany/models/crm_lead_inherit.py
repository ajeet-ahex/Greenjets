from odoo import models, fields, api
from odoo.exceptions import UserError


class CrmStages(models.Model):
    _inherit = 'crm.stage'

    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default = lambda self: self.env.company,
        help='If set, this stage will be available only for the selected company.'
    )



class CrmLead(models.Model):
    _inherit = 'crm.lead'

    stage_id = fields.Many2one(
        'crm.stage', string='Stage',
        group_expand='_group_expand_stage_id'
    )
    @api.model
    def _group_expand_stage_id(self, stages, domain):
        company_id = self.env.company.id
        return self.env['crm.stage'].search([
            ('company_id', 'in', [company_id, False])
        ])