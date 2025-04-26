from odoo import models, fields
import base64
import pandas as pd
from io import BytesIO

class SendEmailsWizard(models.TransientModel):
    _name = 'send.emails.wizard'
    _description = 'Send Emails Wizard'

    def send_emails(self):
        employee = self.env['hr.employee'].browse(self._context.get('active_id'))
        if employee.employee_contacts:
            excel_data = base64.b64decode(employee.employee_contacts)
            df = pd.read_excel(BytesIO(excel_data))
            for index, row in df.iterrows():
                email = row[0]
                subject = row[1]
                self.env['mail.mail'].create({
                    'subject': subject,
                    'email_to': email,
                    'body_html': 'Welcome in GymBeam',
                }).send()