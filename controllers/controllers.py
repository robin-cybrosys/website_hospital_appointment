from odoo import http
from odoo.http import request


class WebsiteForm(http.Controller):
    @http.route(['/appointment'], type='http', auth="public", website=True)
    def appointment(self):
        patient_card = request.env['hospital.management'].sudo().search([])
        doctor_id = request.env['hr.employee'].sudo().search(
            [('job_id', '=', 'Doctor')])
        values = {}
        values.update({
            'patients': patient_card,
            'doctors': doctor_id
        })
        return request.render(
            "website_hospital_appointment.online_appointment_form", values)

    # class WebsiteAccount(http.Controller):
    @http.route(['/appointment/submit'], type='http', auth='public',
                website=True)
    def appointment_submit(self, **post):
        patient = int(post['patient_id'])
        doctor = int(post['doctor_id'])
        date = post.get('appointment_date')
        print(patient, doctor, date)
        appointments = request.env['hospital.appointment'].sudo().search([])
        appointments.create({
            'patient_card_id': patient,
            'date': date,
            'doctor_id': doctor,
        })
        vals = {
            'appointments': appointments,
        }
        return request.render(
            "website_hospital_appointment.appointment_creation_success", vals)

        # create patient card if it's not existing

    @http.route(['/appointment/card/create'], type='http', auth='public',
                website=True)
    def create_card(self):
        patient = request.env['res.partner'].sudo().search([])
        # dob = patient.dob
        # print(dob)
        # patient_phone
        # gender
        # blood_group
        # age

        # doctor_id = request.env['hr.employee'].sudo().search(
        #     [('job_id', '=', 'Doctor')])
        values = {}
        values.update({
            'patients': patient
            # 'doctors': doctor_id
        })
        return request.render(
            "website_hospital_appointment.card_creation_form", values)

    # card submit button
    @http.route(['/appointment/card/submit'], type='http', auth='public',
                website=True)
    def appointment_card_submit(self, **post):
        patient_card = int(post['partner_id'])
        # print(patient, post)
        card = request.env['hospital.management'].sudo().search([])
        card.create({
            # 'patient_id': patient,
            'patient_id': patient_card,

        })
        vals = {
            'card': card,
        }
        return request.render(
            "website_hospital_appointment.card_creation_success",
            vals)

        # # patient = int(post['patient_id'])
        # # print(patient, post)
        # patient_card = request.env['res.partner'].sudo().create({
        #     'patient_card_id': patient,
        #     'name': post.get('name'),
        #     'email': post.get('email'),
        #     'phone': post.get('phone')
        # })
        # vals = {
        #     'patient_cards': patient_card,
        # }
        # return request.render(
        #     "website_hospital_appointment.customer_creation_success",
        #     vals)

        # print(each,"laalalalaalaa")

        #     each.qty_sold = 0
        #     each.views = 0
        #     each.top_selling = False
        #
        #     date = fields.Datetime.now()
        #     date_before = date - datetime.timedelta(days=7)
        #
        # orders = request.env['sale.order'].sudo().search(
        #     [('date_order', '<=', date),
        #      ('date_order', '>=', date_before), ('website_id', '!=', False),
        #      ('state', 'in', ('sale', 'done'))])
        # for order in orders:
        #     order_line = order.order_line
        # for product in order_line:
        #     print(product.product_id.qty_sold)
        #     product.product_id.qty_sold = product.product_id.qty_sold + 1
        #     products = request.env['website.track'].sudo().search(
        #         [('visit_datetime', '<=', date),
        #          ('visit_datetime', '>=', date_before),
        #          ('product_id', '!=', False)])
        # for pro in products:
        #     pro.product_id.views = pro.product_id.views + 1
        # super(WebsiteSort, self).index()
        # website_product_ids = request.env['product.template'].sudo().search(
        #     [('is_published', '=', True),
        #      ('qty_sold', '!=', 0)],
        #     order='qty_sold desc', limit=4)
        # website_product_ids.top_selling = True
        # return request.render('website.homepage',
        #                       {'website_product_ids': website_product_ids})

    # demo
    # products = request.env['product.template'].sudo().search([])
    # for each in products:
    #     each.qty_sold = 0
    #     each.views = 0
    #     each.top_selling = False
    #
    # date = fields.Datetime.now()
    # date_before = date - datetime.timedelta(days=7)
    #
    # orders = request.env['sale.order'].sudo().search(
    #     [('date_order', '<=', date),
    #      ('date_order', '>=', date_before), ('website_id', '!=', False),
    #      ('state', 'in', ('sale', 'done'))])
    # for order in orders:
    #     order_line = order.order_line
    # for product in order_line:
    #     print(product.product_id.qty_sold)
    #     product.product_id.qty_sold = product.product_id.qty_sold + 1
    #     products = request.env['website.track'].sudo().search(
    #         [('visit_datetime', '<=', date),
    #          ('visit_datetime', '>=', date_before),
    #          ('product_id', '!=', False)])
    # for pro in products:
    #     pro.product_id.views = pro.product_id.views + 1
    # super(WebsiteSort, self).index()
    # website_product_ids = request.env['product.template'].sudo().search(
    #     [('is_published', '=', True),
    #      ('qty_sold', '!=', 0)],
    #     order='qty_sold desc', limit=4)
    # website_product_ids.top_selling = True
    # return request.render('website.homepage',
    #                       {'website_product_ids': website_product_ids})
