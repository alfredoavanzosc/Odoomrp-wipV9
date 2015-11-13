
# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "Product Purchase Warrant",
    "version": "9.0.1.0.0",
    "license": 'AGPL-3',
    "author": 'Odoo Community Association (OCA),'
              'OdooMRP team,'
              'AvanzOSC,'
              'Serv. Tecnol. Avanzados - Pedro M. Baeza',
    "depends": ["base", "stock", "product"],
    "contributors": ["Mikel Arregi <mikelarregi@avanzosc.es>"],
    "category": "Product",
    "description": """
    Sets a purchase warranty term on product supplier info,
    and apply it on incoming lots for this product and supplier
    """,
    'data': ["views/stock_view.xml", "views/product_view.xml",
             "wizard/stock_transfer_details_view.xml"
             ],
    "installable": True,
    "auto_install": False,
}
