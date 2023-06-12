# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1685380205.3136883
_enable_loop = True
_template_filename = 'c:/Users/louis/Desktop/Alexandre_Louis_SAE23_liv1/res/templates/pilotes.html'
_template_uri = 'pilotes.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        pilotes = context.get('pilotes', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html lang="fr">\r\n<head>\r\n  <meta charset="UTF-8">\r\n  <title>SUPERMOTARD</title>\r\n  <link rel="stylesheet" href="/css/style.css">\r\n</head>\r\n<body>\r\n\r\n  <header>\r\n    <nav>\r\n        <ul>\r\n            <li><a href="index">Accueil</a></li>\r\n            <li class="dropdown">\r\n                <a href="motos">Motos</a>\r\n                <div class="dropdown-content">\r\n                    <a href="motos">Visualiser toutes les motos</a>\r\n                    <a href="motos_KTM">Visualiser les motos de la marque KTM</a>\r\n                    <a href="motos_recentes">Visualiser les motos récentes</a>\r\n                    <a href="motos_pas_chere">Visualiser les motos pas chères</a>\r\n                </div>\r\n            </li>\r\n            <li class="dropdown">\r\n            <a href="pilotes">Pilotes</a>\r\n            <div class="dropdown-content">\r\n                <a href="pilotes">Visualiser les pilotes existants</a>\r\n                <a href="ajouter_pilotes">Ajouter des pilotes</a>\r\n                <a href="modifier_pilotes">Modifier des pilotes</a>\r\n                <a href="supprimer_pilotes">Supprimer des pilotes</a>\r\n            </div>\r\n            </li>\r\n            <li class="dropdown">\r\n            <a href="vente">Vente</a>\r\n            <div class="dropdown-content">\r\n                <a href="utilisateurs">Ajouter un nouvel utilisateur</a>\r\n                <a href="vente">Vente aux enchères</a>\r\n            </div>\r\n            </li>\r\n        </ul>\r\n    </nav>\r\n</header>\r\n\r\n  <main>\r\n    <h1>Les Pilotes</h1>\r\n    <div class="fiches">\r\n      <table>\r\n        <tr>\r\n            <th>ID Pilote</th>\r\n            <th>Nom</th>\r\n            <th>Statut</th>\r\n            <th>Instagram</th>\r\n            <th>Abonnées</th>\r\n        </tr>\r\n')
        for pilote in pilotes:
            __M_writer('        <tr>\r\n')
            for element in pilote:
                __M_writer('              <td>')
                __M_writer(str(element))
                __M_writer('</td>\r\n')
            __M_writer('          </tr>\r\n')
        __M_writer('    </table>\r\n\r\n    <h3>Fiches descriptives pour quelques pilotes de la base de donnée :</h3>\r\n\r\n      <div class="fiche" id="thomas">\r\n        <img src="/image/thomas_corsi.png" alt="Thomas Corsi">\r\n        <h2>Thomas Corsi</h2>\r\n        <p>Statut : Pilote Amateur <br><br>\r\n          Instagram : <a href="https://www.instagram.com/thomas_corsi/" target="_blank" rel="noopener noreferrer" style="text-decoration: none;"> @thomas_corsi</a><br><br>\r\n          Nombre d\'abonnées : 89 000<br><br>\r\n          Moto : \r\n          <a href="motos#ktm450" style="text-decoration: none;"> KTM 450 EXC-F</a></p>\r\n      </div>\r\n      <div class="fiche" id ="sherco">\r\n        <img src="/image/sherco.png" alt="Shercobike">\r\n        <h2>Shercobike</h2>\r\n        <p>Statut : Pilote Amateur <br><br>\r\n          Instagram : <a href="https://www.instagram.com/shercobike/" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">@shercobike</a><br><br>\r\n          Nombre d\'abonnées : 1530<br><br>\r\n          Moto : \r\n          <a href="motos#sherco" style="text-decoration: none;"> SHERCO 450 SEF-R</a></p>\r\n      </div>\r\n      <div class="fiche" id="tekstunt">\r\n        <img src="/image/tekstunt.png" alt="Tekstunt">\r\n        <h2>Tekstunt</h2>\r\n        <p>Statut : Pilote officiel pour la marque SUPERMOT <br><br>\r\n          Instagram : <a href="https://www.instagram.com/tekstunt/" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">@tekstunt</a><br><br>\r\n          Nombre d\'abonnées : 50 900<br><br>\r\n          Moto : \r\n          <a href="motos#kawa" style="text-decoration: none;"> KAWASAKI 450 KX</a></p>\r\n      </div>\r\n      <div class="fiche" id="thomas_chareyre">\r\n        <img src="/image/thomas_chareyre.png" alt="Thomas Chareyre">\r\n        <h2>Thomas Chareyre</h2>\r\n        <p>Statut : Pilote professionnel <br><br>\r\n          Instagram : <a href="https://www.instagram.com/tomchareyre4/?hl=fr" target="_blank" rel="noopener noreferrer" style="text-decoration: none;"> @tomchareyre4</a><br><br>\r\n          Nombre d\'abonnées : 38 500<br><br>\r\n          Moto : \r\n          <a href="motos#TM" style="text-decoration: none;"> TM SMK 450 ES FI</a></p>\r\n      </div>\r\n      <div class="fiche" id ="laurent">\r\n        <img src="/image/laurent_fath.png" alt="Laurent Fath">\r\n        <h2>Laurent Fath</h2>\r\n        <p>Statut : Pilote professionnel <br><br>\r\n          Instagram : <a href="https://www.instagram.com/laurentfath/" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">@laurentfath</a><br><br>\r\n          Nombre d\'abonnées : 3 117<br><br>\r\n          Moto : \r\n          <a href="motos#honda" style="text-decoration: none;"> Honda CRF 450 R</a></p>\r\n      </div>\r\n      <div class="fiche" id="kika">\r\n        <img src="/image/kikaninac.png" alt="Pilote 3">\r\n        <h2>Kikaninac</h2>\r\n        <p>Statut : Youtubeur / Créateur de la marque SUPERMOT<br><br>\r\n          Instagram : <a href="https://www.instagram.com/kikaninac/" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">@kikaninac</a><br><br>\r\n          Nombre d\'abonnées : 1 299 000<br><br>\r\n          Moto : \r\n          <a href="motos#ktm500" style="text-decoration: none;"> KTM 250 EXC équipé d\'un kit 500 BRC</a></p>\r\n      </div>\r\n    </div>\r\n  </main>\r\n\r\n  <footer>\r\n    <p>C\'est pas de la moto, c\'est du SUPERMOT !</p>\r\n  </footer>\r\n\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "c:/Users/louis/Desktop/Alexandre_Louis_SAE23_liv1/res/templates/pilotes.html", "uri": "pilotes.html", "source_encoding": "utf-8", "line_map": {"16": 0, "22": 1, "23": 54, "24": 55, "25": 56, "26": 57, "27": 57, "28": 57, "29": 59, "30": 61, "36": 30}}
__M_END_METADATA
"""
