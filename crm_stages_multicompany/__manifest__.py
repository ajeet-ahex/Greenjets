{
    'name': 'Multi-Company-Specific CRM Stages',
    'version': '1.0',
    'summary': 'A CRM enhancement that enables company-specific crm stages ',
    'description': 'This Odoo plugin extends the CRM module by introducing company-specific crm stages. Instead of sharing the same pipeline across all companies in a multi-company environment, each company can now define and manage its own CRM stages. This ensures that workflows are better aligned with each company’s sales process.',
    'category': 'Sales',
    'author': 'Ahex Technologies',
     'website':  'https://ahex.co',
    'live_test_url': 'https://ahex.co/contact/',
    'price' : '14',
    'currency' : 'USD',
    'category': 'Sales',
    'depends': ['base', 'sale', 'web' ,'crm'],
    'license': 'OPL-1',
    'data': [
        'views/crm_view_changes.xml',
    ],

    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
}
