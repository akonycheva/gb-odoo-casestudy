rom
odoo
import api, SUPERUSER_ID

def update_api_id(cr, registry):

    env = api.Environment(cr, SUPERUSER_ID, {})


    jobs = env['hr.job'].search([('api_id', '=', False)])


    for job in jobs:

        if job.name == 'Python Developer':
            job.api_id = '4249974'
        else:

            job.api_id = f'JOB_{job.id}'
