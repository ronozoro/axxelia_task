# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AxxPaletteTracking(models.Model):
    _name = 'axx.palette.tracking'
    _rec_name = 'axx_picking_id'

    @api.depends('axx_palette_count_plus', 'axx_palette_count_minus')
    def _compute_palette_balance(self):
        for palette in self:
            palette.axx_balance = palette.axx_palette_count_plus - palette.axx_palette_count_minus

    axx_picking_id = fields.Many2one(comodel_name='stock.picking', string='Picking', required=True)
    axx_partner_id = fields.Many2one(comodel_name='res.partner', string='Partner', required=True)
    axx_license_plate = fields.Char(string='Licence Plate')
    axx_picking_partner_id = fields.Many2one(comodel_name='res.partner', string='Picking Partner')
    axx_picking_date_done = fields.Datetime(string='Date of Transfer')
    axx_palette_count_plus = fields.Integer(string='Palette +', default=0)
    axx_palette_count_minus = fields.Integer(string='Palette -', default=0)
    axx_balance = fields.Integer(string='Balance', compute='_compute_palette_balance')

    @api.onchange('axx_picking_id')
    def onchange_picking_id(self):
        for rec in self:
            if rec.axx_picking_id:
                rec.axx_picking_partner_id = rec.axx_picking_id.partner_id.id
                rec.axx_picking_date_done = rec.axx_picking_id.date_done


AxxPaletteTracking()
