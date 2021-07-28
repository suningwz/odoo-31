# -*- encoding: utf-8 -*-
###############################################################################
#
#    Module Writen to Odoo14, Open Source Management Solution
#
############################################################################
{
    'name': 'Unoobi | Custom cfdi',

    'summary': """Custom cfdi""",

    'description': """
        Custom cfdi
    """,

    'author': 'UNOOBI ©',

    "website": "https://www.unoobi.com/",

    'category': 'Extra tool',

    'version': '1.0',

    'depends': ['base', 'l10n_mx_edi'],

    'data': [
        'data/3.3/inherit_cfdi.xml',
    ],

    # 'qweb': [
    #         'static/src/xml/*.xml'
    #     ],

    'installable': True,

    'active': False,

    'certificate': '',

    'application':False,
}
