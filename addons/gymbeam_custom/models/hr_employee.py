from odoo import fields, models, api
from odoo.exceptions import ValidationError

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    i_love_gb = fields.Boolean(string='I Love GymBeam', default=True)

    salary = fields.Integer(string='Salary')
    tax = fields.Integer(string='Tax')
    total_salary = fields.Integer(string='Total Salary', compute='_compute_total_salary',store=False)

    special_phone = fields.Char(string='Special Phone')

    employee_contacts = fields.Binary(string='Employee Contacts')

    employee_number = fields.Char(string='Employee Number', required=True, tracking=True)

    @api.depends('salary', 'tax')
    def _compute_total_salary(self):
         self.total_salary = self.salary + self.tax

    def write(self, vals):
        if 'special_phone' in vals and not vals['special_phone']:
            vals['special_phone'] = '0901123456'
        return super(HrEmployee, self).write(vals)

    @api.constrains('employee_number')
    def _check_unique_employee_number(self):
        for record in self:
            domain_employee = [('employee_number', '=', record.employee_number), ('id', '!=', record.id)]
            if self.env['hr.employee'].search(domain_employee):
                raise ValidationError("Employee Number must be unique across Employees!")

            domain_applicant = [('employee_number', '=', record.employee_number)]
            if self.env['hr.applicant'].search(domain_applicant):
                raise ValidationError("Employee Number must be unique across Applicants!")