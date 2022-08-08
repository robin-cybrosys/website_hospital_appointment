from odoo import http
from odoo.http import request


class WebsiteForm(http.Controller):
    @http.route(['/appointment'], type='http', auth="public", website=True)
    def appointment(self):
        partners = request.env['res.partner'].sudo().search([])
        values = {}
        values.update({
            'partners': partners
        })
        return request.render("website_hospital_appointment.online_appointment_form", values)
