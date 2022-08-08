from odoo import http
from odoo.http import request


class WebsiteForm(http.Controller):
    @http.route(['/appointment'], type='http', auth="public", website=True)
    def appointment(self):
        patient = request.env['res.partner'].sudo().search([])
        values = {}
        values.update({
            'patients': patient
        })
        return request.render("website_hospital_appointment.online_appointment_form",values)


class WebsiteAccount(http.Controller):

    @http.route(['/my_new_controller'], type='http', auth='public',
                website=True)
    def my_controller_method(self, redirect=None, **post):
# Put your backend operations here, e.g.
        appointment = request.env['hospital.appointment']
        appointment.appointment_confirm_btn({...})

# After you're done, use either request.render() or request.redirect() to show
# a different page to the user. You can check out the website_portal module for examples.
