# -*- coding: utf-8 -*-
{
    'name': 'Palette Tracking',
    'summary': """Palette tracking for Company partners""",
    'version': '13.0.1.2.1',
    'category': 'Other',
    "author": "Mostafa Mohamed",
    "license": 'Other OSI approved licence',
    'depends': ['base', 'sale', 'sale_management', 'stock', 'sale_stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/palette_tracking_view.xml',
        'views/res_partner_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
