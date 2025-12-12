# -*- coding: utf-8 -*-

{
    'name': 'POS - Deshabilitar Descarga Factura',
    'category': 'Point of Sale',
    'summary': """Este módulo permite habilitar o deshabilitar la funcionalidad de descarga de la factura de la
    orden como un PDF en el sistema Odoo POS. Proporciona flexibilidad para las empresas que no requieren facturas PDF
    para cada venta, mejorando la eficiencia y simplificando el proceso POS.
    keywords: 'Deshabilitar Descarga Factura | POS factura descarga | Odoo POS factura | PDF factura POS | Descargar factura',""",
    'description': """Este módulo permite habilitar o deshabilitar la funcionalidad de descarga de la factura de la
    orden como un PDF en el sistema Odoo POS. Proporciona flexibilidad para las empresas que no requieren facturas PDF
    para cada venta, mejorando la eficiencia y simplificando el proceso POS.
    """,
    'author': 'z99sys',
    'version': '1.0',
    'depends': ['point_of_sale', 'account'],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_deshabilitar_factura_descarga/static/src/**/*'
        ],
    },
    'data':  ['views/pos.xml'],
    'installable': True,
    'auto_install': False,
    "license": "LGPL-3",
    "images":["static/description/banner.png"],
}
