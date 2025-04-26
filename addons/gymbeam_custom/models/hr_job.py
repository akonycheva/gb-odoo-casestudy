from odoo import fields, models

class HrJob(models.Model):
    _inherit = 'hr.job'

    api_id = fields.Char(string="API ID", required=True)
