from odoo import fields, models

class Manga(models.Model):
    _name="mangatheque.manga"
    _description = "manga"

    name = fields.Char("Titre",required=True)
    anne_parution = fields.Integer('Année de parution')
    auteur = fields.Many2one('res.partner', string="auteur")
    image_couverture = fields.Binary('Couverture')