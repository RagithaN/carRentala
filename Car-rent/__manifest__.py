# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Car_Rent_application ',
    'version': '1.0',
    'category': 'Tools',
     'summary': 'cars and Customers Management',
    'depends': ['web', 'mail', 'sms', 'rating', 'utm', 'website', 'portal'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/carRent_views.xml',
         'views/carrent_cars_view.xml',
         
           'views/carrent_customers_view.xml',
          
        
    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
