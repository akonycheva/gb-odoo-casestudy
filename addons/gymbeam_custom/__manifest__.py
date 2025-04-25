{
    'name': 'GymBeam Custom Module',
    'version': '1.0',
    'depends': ['hr', 'hr_recruitment'],
    'data': [
        'security/ir.model.access.csv',
        'wizards/send_emails_wizard_views.xml',
        'views/hr_employee_views.xml',
        'views/hr_applicant_views.xml',
    ],
    'installable': True,
    'application': False,
}