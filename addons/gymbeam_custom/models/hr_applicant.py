from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HrApplicant(models.Model):
    _inherit = 'hr.applicant'
    employee_number = fields.Char(string='Employee Number', required=True, tracking=True)

    @api.constrains('employee_number')
    def _check_unique_employee_number(self):
        for record in self:
            # Проверяем, есть ли такой номер в hr.applicant (кроме текущей записи)
            domain_applicant = [('employee_number', '=', record.employee_number), ('id', '!=', record.id)]
            if self.env['hr.applicant'].search(domain_applicant):
                raise ValidationError("Employee Number must be unique across Applicants!")

            # Проверяем, есть ли такой номер в hr.employee
            domain_employee = [('employee_number', '=', record.employee_number)]
            if self.env['hr.employee'].search(domain_employee):
                raise ValidationError("Employee Number must be unique across Employees!")

    gender = fields.Char(string="Gender")

