# -*- coding: utf-8 -*-
{
    'name': "{{ name|snake }}",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "Vauxoo",
    'website': "http://www.vauxoo.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    #Change the version every release for apps.
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': [
        'base'
    ],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # only loaded in test
    'test': [
    ],
}
