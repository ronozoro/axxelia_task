# -*- coding: utf-8 -*-
from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _get_palette_count(self):
        for partner in self:
            partner.palette_count = self.env['axx.palette.tracking'].search_count([('axx_partner_id', '=', partner.id)])

    palette_count = fields.Integer(string='Palette Count', default=0, compute='_get_palette_count')


ResPartner()
