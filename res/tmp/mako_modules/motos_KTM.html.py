# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1685389816.003312
_enable_loop = True
_template_filename = 'c:/Users/louis/Desktop/Alexandre_Louis_SAE23_liv1/res/templates/motos_KTM.html'
_template_uri = 'motos_KTM.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        motos = context.get('motos', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n<head>\r\n    <meta charset="UTF-8">\r\n    <title>SUPERMOTARD</title>\r\n    <link rel="stylesheet" href="/css/style.css">\r\n</head>\r\n\r\n<header>\r\n    <nav>\r\n        <ul>\r\n            <li><a href="index">Accueil</a></li>\r\n            <li class="dropdown">\r\n                <a href="motos">Motos</a>\r\n                <div class="dropdown-content">\r\n                    <a href="motos">Visualiser toutes les motos</a>\r\n                    <a href="motos_KTM">Visualiser les motos de la marque KTM</a>\r\n                    <a href="motos_recentes">Visualiser les motos récentes</a>\r\n                    <a href="motos_pas_chere">Visualiser les motos pas chères</a>\r\n                </div>\r\n            </li>\r\n            <li class="dropdown">\r\n            <a href="pilotes">Pilotes</a>\r\n            <div class="dropdown-content">\r\n                <a href="pilotes">Visualiser les pilotes existants</a>\r\n                <a href="ajouter_pilotes">Ajouter des pilotes</a>\r\n                <a href="modifier_pilotes">Modifier des pilotes</a>\r\n                <a href="supprimer_pilotes">Supprimer des pilotes</a>\r\n            </div>\r\n            </li>\r\n            <li class="dropdown">\r\n            <a href="vente">Vente</a>\r\n            <div class="dropdown-content">\r\n                <a href="utilisateurs">Ajouter un nouvel utilisateur</a>\r\n                <a href="vente">Vente aux enchères</a>\r\n            </div>\r\n            </li>\r\n        </ul>\r\n    </nav>\r\n</header>\r\n\r\n<body>\r\n    <h1>Liste des motos de la marque KTM</h1>\r\n    <table>\r\n        <tr>\r\n            <th>ID Moto</th>\r\n            <th>Marque</th>\r\n            <th>Modèle</th>\r\n            <th>Année</th>\r\n            <th>Cylindrée</th>\r\n            <th>Prix</th>\r\n            <th>ID Pilote</th>\r\n        </tr>\r\n')
        for moto in motos:
            __M_writer('      <tr>\r\n')
            for element in moto:
                __M_writer('          <td>')
                __M_writer(str(element))
                __M_writer('</td>\r\n')
            __M_writer('      </tr>\r\n')
        __M_writer("    </table>\r\n</body>\r\n\r\n<footer>\r\n    <p>C'est pas de la moto, c'est du SUPERMOT !</p>\r\n</footer>\r\n\r\n</html>\r\n\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "c:/Users/louis/Desktop/Alexandre_Louis_SAE23_liv1/res/templates/motos_KTM.html", "uri": "motos_KTM.html", "source_encoding": "utf-8", "line_map": {"16": 0, "22": 1, "23": 54, "24": 55, "25": 56, "26": 57, "27": 57, "28": 57, "29": 59, "30": 61, "36": 30}}
__M_END_METADATA
"""
