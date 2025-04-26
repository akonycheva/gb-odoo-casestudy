from odoo import api, SUPERUSER_ID


def update_api_id(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})

    jobs = env['hr.job'].search([])

    if not jobs:
        print("No jobs found in the database.")
        return

    print(f"Found {len(jobs)} jobs to process.")

    for job in jobs:
        try:
            if not hasattr(job, 'api_id'):
                print(f"Field 'api_id' does not exist on hr.job. Ensure the module defining 'api_id' is installed.")
                return

            if job.name == 'Python Developer':
                job.api_id = '4249974'
                print(f"Set api_id to '4249974' for job '{job.name}' (ID: {job.id})")
            else:
                job.api_id = '4249974'
                print(f"Set api_id to 'JOB_{job.id}' for job '{job.name}' (ID: {job.id})")

        except Exception as e:
            print(f"Error processing job '{job.name}' (ID: {job.id}): {str(e)}")

    env.cr.commit()
    print("API IDs updated successfully.")