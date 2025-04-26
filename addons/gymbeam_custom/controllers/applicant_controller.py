from odoo import http
from odoo.http import request

class ApplicantController(http.Controller):

    @http.route('/case_study/applicant/get', type='json', auth='public', methods=['POST'], csrf=False)
    def create_applicant(self):
        data = request.jsonrequest
        candidates = data.get('candidates', [])
        for candidate in candidates:
            firstname = candidate.get('firstname')
            surname = candidate.get('surname')
            phone = candidate.get('phone')
            email = candidate.get('email')
            gender = candidate.get('gender')
            job_api_id = candidate.get('job', {}).get('id')

            if not all([firstname, surname, phone, email, gender, job_api_id]):
                return {'status': 'error', 'message': 'Missing required fields'}

            job = request.env['hr.job'].sudo().search([('api_id', '=', str(job_api_id))], limit=1)
            if not job:
                return {'status': 'error', 'message': f'Job with api_id {job_api_id} not found'}

            applicant = request.env['hr.applicant'].sudo().create({
                'name': f"{firstname} {surname}",
                'partner_phone': phone,
                'email_from': email,
                'gender': gender,
                'job_id': job.id,
            })

        return {'status': 'success', 'message': 'Applicants created successfully'}