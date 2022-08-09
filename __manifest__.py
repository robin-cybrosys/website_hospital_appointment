# -*- coding: utf-8 -*-
{
    'name': "website_hospital_appointment",
    # 'application': "True",
    'summary': """
        Hospital Website
        """,
    'author': "The R",
    'website': "http://www.cybrosys.com",
    'sequence': "4",
    'licence': "LGPL-3",
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'hospital_management'],

    # always loaded
    'data': [
        'views/appointments_page.xml',
        'views/appointments_webpage_template.xml',
    ],
}
