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
{
    'name': 'Birtum | Update edi payment time',
    'author': 'Wedoo ©',
    'category': 'Accounting',
    'sequence': 50,
    'summary': "Update edi payment time",
    'website': 'http://www.birtum.com',
    'version': '14.0.1.0',
    'license': 'LGPL-3',
    'description': """
        """,
    'depends': [
        'base',
        'account',
        'l10n_mx_edi',
    ],
    'data': [
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
}
