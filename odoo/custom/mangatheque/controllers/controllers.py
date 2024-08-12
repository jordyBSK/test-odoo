# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Mangatheque(http.Controller):

    @http.route('/mangatheque', type='http', auth='public', website=True)
    def index(self):
        Manga = request.env['manga']
        # Chercher tous les enregistrements de manga
        mangas = Manga.search([])

        # Si mangas est None, le transformer en liste vide pour éviter les erreurs dans le template
        if mangas is None:
            mangas = []

        # Rendre le template avec les données de mangas
        return request.render('mangatheque.mangatheque_controller', {
            'manga': mangas
        })

