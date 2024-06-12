# -*- coding: utf-8 -*-
{
    'name': 'Stock Distributors',
    'version': '16.0.1.0.0',
    'summary': """ Muestra storck actual a distribuidores""",
    'author': '',
    'website': '',
    'category': '',
    'depends': ['base', 'web', 'stock', 'website'],
    "data": [
        "views/stock_products_views.xml",
        "views/menu_items.xml",
    ],'assets': {
            'web.assets_backend': [
                'tagre_stock_distributors/static/src/**/*'
            ],
        },
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
