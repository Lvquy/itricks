# -*- coding: utf-8 -*-
{
    'name': 'iTricks.me',
    'version': '1',
    'category': 'Tricks & Tips',
    'live_test_url': '#',
    'summary': '#',
    'author': 'Lv Quy',
    'company': '#',
    'website': 'https://itricks.me',
    'depends': ['base_setup','website'],
    'data': [
        #data

        # security
        'security/groups.xml',
        'security/ir.model.access.csv',
        # report
        # views
        'views/custom_footer.xml',
        'views/header.xml',
        'views/custom_style_heading.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'itricks_me/static/src/css/style.css'
        ],
        'web._assets_primary_variables': [
        ],
    },

    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
}
