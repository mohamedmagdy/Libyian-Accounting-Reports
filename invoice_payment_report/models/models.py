# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.ehcs_qr_code_base.models.qr_code_base import generate_qr_code


class AccountMove(models.Model):
    # _name = 'account.move'
    _inherit = 'account.move'

    qr_code = fields.Binary(string='QR Code', compute='_compute_qr_code')

    def _compute_qr_code(self):
        for rec in self:
            if rec.id:
                url = rec.env['ir.config_parameter'].sudo().get_param('web.base.url') + '/my/invoices/' + str(rec.id)
                qr_code = generate_qr_code(url)
                rec.qr_code = qr_code
