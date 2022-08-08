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
        return request.render(
            "website_hospital_appointment.online_appointment_form", values)


class WebsiteAccount(http.Controller):
    @http.route(['/appointment_submit'], type='http', auth='public',
                website=True)
    def my_controller_method(self, redirect=None, **post):
        print("laalalalaalaa")
        # Put your backend operations here, e.g.
        appointments = request.env['hospital.appointment'].sudo().search([])



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
