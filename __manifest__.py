# -*- coding: utf-8 -*-
{
    'name': 'Gestion de Ordenadores',
    'version': '1.0',
    'summary': 'Registro de ordenadores, componentes y mantenimiento',
    'author': 'Sonia',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/component_view.xml',
        'views/computer_view.xml',
        'views/menu.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
