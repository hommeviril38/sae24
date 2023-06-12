# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1685380206.8619702
_enable_loop = True
_template_filename = 'c:/Users/louis/Desktop/Alexandre_Louis_SAE23_liv1/res/templates/motos.html'
_template_uri = 'motos.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        motos = context.get('motos', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html lang="fr">\r\n<head>\r\n  <meta charset="UTF-8">\r\n  <title>SUPERMOTARD</title>\r\n  <link rel="stylesheet" href="/css/style.css">\r\n</head>\r\n<body>\r\n\r\n  <header>\r\n    <nav>\r\n        <ul>\r\n            <li><a href="index">Accueil</a></li>\r\n            <li class="dropdown">\r\n                <a href="motos">Motos</a>\r\n                <div class="dropdown-content">\r\n                    <a href="motos">Visualiser toutes les motos</a>\r\n                    <a href="motos_KTM">Visualiser les motos de la marque KTM</a>\r\n                    <a href="motos_recentes">Visualiser les motos récentes</a>\r\n                    <a href="motos_pas_chere">Visualiser les motos pas chères</a>\r\n                </div>\r\n            </li>\r\n            <li class="dropdown">\r\n            <a href="pilotes">Pilotes</a>\r\n            <div class="dropdown-content">\r\n                <a href="pilotes">Visualiser les pilotes existants</a>\r\n                <a href="ajouter_pilotes">Ajouter des pilotes</a>\r\n                <a href="modifier_pilotes">Modifier des pilotes</a>\r\n                <a href="supprimer_pilotes">Supprimer des pilotes</a>\r\n            </div>\r\n            </li>\r\n            <li class="dropdown">\r\n            <a href="vente">Vente</a>\r\n            <div class="dropdown-content">\r\n                <a href="utilisateurs">Ajouter un nouvel utilisateur</a>\r\n                <a href="vente">Vente aux enchères</a>\r\n            </div>\r\n            </li>\r\n        </ul>\r\n    </nav>\r\n</header>\r\n\r\n<main>\r\n  <h1>Les Motos</h1>\r\n  <div class="fiches">\r\n    <table>\r\n      <tr>\r\n        <th>ID Moto</th>\r\n        <th>Marque</th>\r\n        <th>Modèle</th>\r\n        <th>Année</th>\r\n        <th>Cylindrée</th>\r\n        <th>Prix</th>\r\n        <th>ID Pilote</th>\r\n      </tr>\r\n')
        for moto in motos:
            __M_writer('      <tr>\r\n')
            for element in moto:
                __M_writer('          <td>')
                __M_writer(str(element))
                __M_writer('</td>\r\n')
            __M_writer('      </tr>\r\n')
        __M_writer('    </table>\r\n    \r\n    <h3>Fiches descriptives pour quelques motos de la base de donnée :</h3>\r\n    \r\n    <div class="fiche" id="ktm450">\r\n      <img src="/image/moto_thomas_corsi.png" alt="KTM 450 EXC-F">\r\n      <h2>KTM 450 EXC-F</h2>\r\n      <p>Marque : KTM <br><br>\r\n        Modèle : EXC-F <br><br>\r\n        Année de fabrication : 2022<br><br>\r\n        Cylindrée : 450 cm2<br><br>\r\n        Prix neuf : 11 149 €<br><br>\r\n        Propriétaire :\r\n        <a href="pilotes#thomas" style="text-decoration: none;"> Thomas corsi</a></p>\r\n    </div>\r\n    <div class="fiche" id="sherco">\r\n      <img src="/image/moto_sherco.png" alt="SHERCO 450 SEF-R">\r\n      <h2>SHERCO 450 SEF-R</h2>\r\n      <p>Marque : SHERCO <br><br>\r\n        Modèle : SEF-R <br><br>\r\n        Année de fabrication : 2016<br><br>\r\n        Cylindrée : 450 cm2<br><br>\r\n        Prix neuf : 10 385 €<br><br>\r\n        Propriétaire :\r\n        <a href="pilotes#sherco" style="text-decoration: none;"> Shercobike</a></p>\r\n    </div>\r\n    <div class="fiche" id="kawa">\r\n      <img src="/image/moto_tekstunt.jpeg" alt="KAWASAKI 450 KX">\r\n      <h2>KAWASAKI 450 KX</h2>\r\n      <p>Marque : KAWASAKI <br><br>\r\n        Modèle : KX <br><br>\r\n        Année de fabrication : 2022<br><br>\r\n        Cylindrée : 450 cm2<br><br>\r\n        Prix neuf : 9 099 €<br><br>\r\n        Propriétaire :\r\n        <a href="pilotes#tekstunt" style="text-decoration: none;"> Tekstunt</a></p>\r\n    </div>\r\n    <div class="fiche" id="TM">\r\n      <img src="/image/moto_thomas_chareyre.png" alt="TM SMK 450 ES FI">\r\n      <h2>TM SMK 450 ES FI</h2>\r\n      <p>Marque : TM Racing<br><br>\r\n        Modèle : SMK ES FI<br><br>\r\n        Année de fabrication : 2023<br><br>\r\n        Cylindrée : 450 cm2<br><br>\r\n        Prix neuf : 14 599 €<br><br>\r\n        Propriétaire :\r\n        <a href="pilotes#thomas_chareyre" style="text-decoration: none;"> Thomas Chareyre</a></p>\r\n    </div>\r\n    <div class="fiche" id="honda">\r\n      <img src="/image/moto_laurent.png" alt="HONDA CRF 450 R">\r\n      <h2>HONDA CRF 450 R</h2>\r\n      <p>Marque : HONDA <br><br>\r\n        Modèle : CRF-R <br><br>\r\n        Année de fabrication : 2023<br><br>\r\n        Cylindrée : 450 cm2<br><br>\r\n        Prix neuf : 10 149 €<br><br>\r\n        Propriétaire :\r\n        <a href="pilotes#laurent" style="text-decoration: none;"> Laurent Fath</a></p>\r\n    </div>\r\n    <div class="fiche" id="ktm500">\r\n      <img src="/image/500 2T.JPG" alt="KTM 250 EXC (500 BRC)">\r\n      <h2>KTM 250 EXC (500 BRC)</h2>\r\n      <p>Marque : KTM (moteur BRC)<br><br>\r\n        Modèle : EXC<br><br>\r\n        Année de fabrication : 2016<br><br>\r\n        Cylindrée : 500 cm2<br><br>\r\n        Prix neuf : 8 355 €<br><br>\r\n        Propriétaire :\r\n        <a href="pilotes#kika" style="text-decoration: none;"> Kikaninac</a></p>\r\n    </div>\r\n  </div>\r\n\r\n</main>\r\n\r\n<footer>\r\n  <p>C\'est pas de la moto, c\'est du SUPERMOT !</p>\r\n</footer>\r\n\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "c:/Users/louis/Desktop/Alexandre_Louis_SAE23_liv1/res/templates/motos.html", "uri": "motos.html", "source_encoding": "utf-8", "line_map": {"16": 0, "22": 1, "23": 56, "24": 57, "25": 58, "26": 59, "27": 59, "28": 59, "29": 61, "30": 63, "36": 30}}
__M_END_METADATA
"""
