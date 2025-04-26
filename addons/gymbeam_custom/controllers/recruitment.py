from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.form import WebsiteForm

class CustomWebsiteForm(WebsiteForm):
    @http.route('/website/form/', type='http', auth="public", website=True, methods=['POST'])
    def website_form(self, model, **kwargs):
        # Получаем данные формы
        post = kwargs.copy()
        error = {}
        has_errors = False

        # Проверяем обязательные поля
        if not post.get('partner_name'):
            error['partner_name'] = 'This is a required field'
            has_errors = True
        if not post.get('email_from'):
            error['email_from'] = 'This is a required field'
            has_errors = True
        if not post.get('partner_mobile'):
            error['phone'] = 'This is a required field'
            has_errors = True
        if not post.get('Resume'):
            error['attachment'] = 'This is a required field'
            has_errors = True

        # Если есть ошибки, возвращаем форму с ошибками
        if has_errors:
            job_id = post.get('job_id')
            job = request.env['hr.job'].sudo().browse(int(job_id)) if job_id else None
            if not job:
                return request.render('website.404')

            return request.render('website_hr_recruitment.apply', {
                'job': job,
                'error': error,
                'has_errors': has_errors,
                'post': post,
                'action': f'/website/form/{model}',  # Обновляем action
            })

        # Если ошибок нет, продолжаем стандартную обработку
        return super(CustomWebsiteForm, self).website_form(model, **kwargs)

    @http.route('/jobs/apply/<string:job_slug>', type='http', auth="public", website=True, methods=['GET'])
    def apply_job(self, job_slug, **post):
        job = request.env['hr.job'].sudo().search([('website_url', '=', job_slug)], limit=1)

        if not job and job_slug.isdigit():
            job = request.env['hr.job'].sudo().browse(int(job_slug))

        if not job:
            return request.render('website.404')

        return request.render('website_hr_recruitment.apply', {
            'job': job,
            'error': {},
            'has_errors': False,
            'post': post if post else {},
            'action': '/website/form/hr_applicant',  # Указываем правильный action
        })