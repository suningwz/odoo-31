# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
#
# Copyright (c) 2022 Birtum - http://www.birtum.com
# All Rights Reserved.
#
# Developer(s): Alan Guzmán
#               (age@wedoo.tech)
########################################################################
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
########################################################################
from odoo import models, fields
from datetime import datetime
from pytz import timezone


class AccountPayment(models.Model):
    _inherit = 'account.payment'


    def update_edi_payment_time(self):
        move = self.move_id
        issued_address = move._get_l10n_mx_edi_issued_address()
        tz = move._l10n_mx_edi_get_cfdi_partner_timezone(issued_address)
        tz_force = self.env['ir.config_parameter'].sudo().get_param('l10n_mx_edi_tz_%s' % move.journal_id.id, default=None)
        if tz_force:
            tz = timezone(tz_force)
        move.l10n_mx_edi_post_time = fields.Datetime.to_string(datetime.now(tz))