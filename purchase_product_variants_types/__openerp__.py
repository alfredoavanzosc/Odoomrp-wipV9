# -*- coding: utf-8 -*-
# (c) 2015 Serv. Tecnol. Avanzados - Pedro M. Baeza
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Purchase - Product variants types",
    "version": "9.0.1.0.0",
    "license": 'AGPL-3',
    "author": 'Odoo Community Association (OCA),'
              'OdooMRP team,'
              'AvanzOSC,'
              'Serv. Tecnol. Avanzados - Pedro M. Baeza',
    "depends": [
        "purchase_product_variants",
        "product_attribute_types",
    ],
    "contributors": [
        "Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>",
    ],
    "category": "Hidden/Dependency",
    "website": "http://www.odoomrp.com",
    "data": [
        "views/purchase_order_view.xml",
    ],
    "installable": True,
    "auto_install": True,
}
