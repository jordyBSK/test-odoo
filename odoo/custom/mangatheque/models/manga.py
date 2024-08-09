from odoo import fields, models


class Manga(models.Model):
    _name = "manga"
    _description = "Manga"

    name = fields.Char("Titre", required=True)
    annee_parution = fields.Integer("Année de parution")
    auteur = fields.Many2one("res.partner", string="Auteur")
    image_couverture = fields.Binary("Couverture")

    etat = fields.Char("Etat",default="Disponible")
