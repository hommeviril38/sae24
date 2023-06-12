# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1685380202.0644956
_enable_loop = True
_template_filename = 'c:/Users/louis/Desktop/Alexandre_Louis_SAE23_liv1/res/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html lang="fr">\r\n<head>\r\n  <meta charset="UTF-8">\r\n  <title>SUPERMOTARD</title>\r\n  <link rel="stylesheet" href="/css/accueil.css">\r\n</head>\r\n<body>\r\n\r\n<header>\r\n    <nav>\r\n        <ul>\r\n            <li><a href="index">Accueil</a></li>\r\n            <li class="dropdown">\r\n                <a href="motos">Motos</a>\r\n                <div class="dropdown-content">\r\n                    <a href="motos">Visualiser toutes les motos</a>\r\n                    <a href="motos_KTM">Visualiser les motos de la marque KTM</a>\r\n                    <a href="motos_recentes">Visualiser les motos récentes</a>\r\n                    <a href="motos_pas_chere">Visualiser les motos pas chères</a>\r\n                </div>\r\n            </li>\r\n            <li class="dropdown">\r\n            <a href="pilotes">Pilotes</a>\r\n            <div class="dropdown-content">\r\n                <a href="pilotes">Visualiser les pilotes existants</a>\r\n                <a href="ajouter_pilotes">Ajouter des pilotes</a>\r\n                <a href="modifier_pilotes">Modifier des pilotes</a>\r\n                <a href="supprimer_pilotes">Supprimer des pilotes</a>\r\n            </div>\r\n            </li>\r\n            <li class="dropdown">\r\n            <a href="vente">Vente</a>\r\n            <div class="dropdown-content">\r\n                <a href="utilisateurs">Ajouter un nouvel utilisateur</a>\r\n                <a href="vente">Vente aux enchères</a>\r\n            </div>\r\n            </li>\r\n        </ul>\r\n    </nav>\r\n</header>\r\n\r\n  <main>\r\n    <h1>Supermotard</h1>\r\n    <a href="motos" class="button">Découvrez la fusion entre la route et la piste : explorez notre séléction de présigieux supermotard.</a>\r\n  </main>\r\n\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "c:/Users/louis/Desktop/Alexandre_Louis_SAE23_liv1/res/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 1, "27": 21}}
__M_END_METADATA
"""
