from odoo import models, fields

class DonnerNote(models.TransientModel):
    _name = "donner.note"
    _description = "Pour donner une Note"

    note = fields.Integer('donner.note')

    def donner_note(self):
        Manga = self.env['manga']
        manga_id = Manga.browse(self.env.context.get('active_id'))
        manga_id.note = self.note