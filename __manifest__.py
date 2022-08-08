# -*- coding: utf-8 -*-
{
    'name': "website_hospital_appointment",
    'application': "True",
    'summary': """
        Hospital Website
        """,
    'author': "My Company",
    'website': "http://www.cybrosys.com",
    'sequence': "4",
    'licence': "LGPL-3",
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/appointments_page.xml',
        'views/appointments_webpage_template.xml',
    ],

    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
