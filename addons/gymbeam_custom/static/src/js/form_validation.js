odoo.define('gymbeam_custom_module.form_validation', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');

    publicWidget.registry.JobApplicationFormValidation = publicWidget.Widget.extend({
        selector: '#job_application_form',
        events: {
            'submit': '_onSubmitForm',
        },

        _onSubmitForm: function (ev) {
            ev.preventDefault(); // Предотвращаем отправку формы

            var $form = $(this.selector);
            var hasErrors = false;

            // Очищаем старые ошибки
            $form.find('.error:not(.general-error)').remove();
            $form.find('.s_website_form_input').removeClass('is-invalid');
            $form.find('.general-error').hide();

            // Проверяем обязательные поля
            $form.find('input[required], input[type="file"][required]').each(function () {
                var $input = $(this);
                var value = $input.val();
                var isFileInput = $input.attr('type') === 'file';

                // Проверяем, заполнено ли поле
                if (isFileInput && (!value || $input[0].files.length === 0)) {
                    $input.addClass('is-invalid');
                    $input.parent().after('<span class="error">This is a required field</span>');
                    hasErrors = true;
                } else if (!isFileInput && !value.trim()) {
                    $input.addClass('is-invalid');
                    $input.after('<span class="error">This is a required field</span>');
                    hasErrors = true;
                }
            });

            // Показываем общее сообщение об ошибке, если есть ошибки
            if (hasErrors) {
                $form.find('.general-error').show();
            } else {
                // Если ошибок нет, отправляем форму
                $form.off('submit').submit();
            }
        },
    });

    return publicWidget.registry.JobApplicationFormValidation;
});