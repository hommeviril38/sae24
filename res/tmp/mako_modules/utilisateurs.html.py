# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1685551786.9825497
_enable_loop = True
_template_filename = 'c:/Users/louis/Desktop/Alexandre_Louis_SAE23_liv1/res/templates/utilisateurs.html'
_template_uri = 'utilisateurs.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        utilisateurs = context.get('utilisateurs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html lang="fr">\r\n<head>\r\n  <meta charset="UTF-8">\r\n  <title>SUPERMOTARD</title>\r\n  <link rel="stylesheet" href="/css/style.css">\r\n</head>\r\n<body>\r\n\r\n<header>\r\n    <nav>\r\n        <ul>\r\n            <li><a href="index">Accueil</a></li>\r\n            <li class="dropdown">\r\n                <a href="motos">Motos</a>\r\n                <div class="dropdown-content">\r\n                    <a href="motos">Visualiser toutes les motos</a>\r\n                    <a href="motos_KTM">Visualiser les motos de la marque KTM</a>\r\n                    <a href="motos_recentes">Visualiser les motos récentes</a>\r\n                    <a href="motos_pas_chere">Visualiser les motos pas chères</a>\r\n                </div>\r\n            </li>\r\n            <li class="dropdown">\r\n            <a href="pilotes">Pilotes</a>\r\n            <div class="dropdown-content">\r\n                <a href="pilotes">Visualiser les pilotes existants</a>\r\n                <a href="ajouter_pilotes">Ajouter des pilotes</a>\r\n                <a href="modifier_pilotes">Modifier des pilotes</a>\r\n                <a href="supprimer_pilotes">Supprimer des pilotes</a>\r\n            </div>\r\n            </li>\r\n            <li class="dropdown">\r\n            <a href="vente">Vente</a>\r\n            <div class="dropdown-content">\r\n                <a href="utilisateurs">Ajouter un nouvel utilisateur</a>\r\n                <a href="vente">Vente aux enchères</a>\r\n            </div>\r\n            </li>\r\n        </ul>\r\n    </nav>\r\n</header>\r\n\r\n<h1>Inscrivez vous afin de pouvoir participer à la vente aux enchères :</h1>\r\n<form method="POST" action="/utilisateurs">\r\n    <label for="nom">Nom d\'utilisateur :</label>\r\n    <input type="text" id="nom" name="nom" required><br>\r\n    <label for="id">Numéro d\'utilisateur (Vérifiez qu\'il n\'existe pas déjà) :</label>\r\n    <input type="text" id="id" name="id" required><br>\r\n    <button type="submit">Ajouter</button>\r\n</form>\r\n\r\n<h1>Utilisateurs existants :</h1>\r\n<div class="tableau-centré">\r\n<table>\r\n  <thead>\r\n    <tr>\r\n      <th>Numéro d\'utilisateur</th>\r\n      <th>Nom Utilisateur</th>\r\n    </tr>\r\n  </thead>\r\n  <tbody>\r\n')
        for utilisateur in utilisateurs:
            __M_writer('    <tr>\r\n      <td>')
            __M_writer(str(utilisateur[0]))
            __M_writer('</div></td>\r\n      <td>')
            __M_writer(str(utilisateur[1]))
            __M_writer('</div></td>\r\n    </tr>\r\n')
        __M_writer('  </tbody>\r\n</table>\r\n<div class="tableau-centré"></div>\r\n\r\n</body>\r\n</html>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "c:/Users/louis/Desktop/Alexandre_Louis_SAE23_liv1/res/templates/utilisateurs.html", "uri": "utilisateurs.html", "source_encoding": "utf-8", "line_map": {"16": 0, "22": 1, "23": 62, "24": 63, "25": 64, "26": 64, "27": 65, "28": 65, "29": 68, "35": 29}}
__M_END_METADATA
"""
