{
    'name': 'GymBeam Custom Module',
    'version': '1.0',
    'depends': ['hr', 'hr_recruitment', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'wizards/send_emails_wizard_views.xml',
        'views/hr_employee_views.xml',
        'views/hr_applicant_views.xml',
        'views/recruitment_form.xml',

    ],
    'assets': {
        'web.assets_frontend': [
            'gymbeam_custom/static/src/css/application_form.css',

        ],
    },
    'installable': True,
    'application': False,
    'post_init_hook': 'update_api_id',
}