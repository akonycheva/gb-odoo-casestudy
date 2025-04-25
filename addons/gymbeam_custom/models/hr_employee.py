from odoo import fields, models, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    i_love_gb = fields.Boolean(string='I Love GymBeam', default=True)

    salary = fields.Integer(string='Salary')
    tax = fields.Integer(string='Tax')
    total_salary = fields.Integer(string='Total Salary', compute='_compute_total_salary',store=False)

    special_phone = fields.Char(string='Special Phone')

    employee_contacts = fields.Binary(string='Employee Contacts')

    @api.depends('salary', 'tax')
    def _compute_total_salary(self):
         self.total_salary = self.salary + self.tax

    def write(self, vals):
        if 'special_phone' in vals and not vals['special_phone']:
            vals['special_phone'] = '0901123456'
        return super(HrEmployee, self).write(vals)
