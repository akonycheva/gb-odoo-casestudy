from odoo import fields, models

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    i_love_gb = fields.Boolean(string='I Love GymBeam', default=True)
