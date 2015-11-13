# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
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

from openerp import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    main_project_id = fields.Many2one('project.project', string="Main Project")

    @api.one
    @api.onchange('main_project_id')
    def onchange_project_id(self):
        for line in self.order_line:
            line.account_analytic_id = self.main_project_id.analytic_account_id
