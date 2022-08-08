# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteHospitalAppointment(http.Controller):
#     @http.route('/website_hospital_appointment/website_hospital_appointment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_hospital_appointment/website_hospital_appointment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_hospital_appointment.listing', {
#             'root': '/website_hospital_appointment/website_hospital_appointment',
#             'objects': http.request.env['website_hospital_appointment.website_hospital_appointment'].search([]),
#         })

#     @http.route('/website_hospital_appointment/website_hospital_appointment/objects/<model("website_hospital_appointment.website_hospital_appointment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_hospital_appointment.object', {
#             'object': obj
#         })
