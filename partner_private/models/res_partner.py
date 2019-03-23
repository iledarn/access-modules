# -*- coding: utf-8 -*-
from openerp import models, fields


class Partner(models.Model):
    _inherit = "res.partner"

    type = fields.Selection(selection_add=[("private", "Private Address")])
