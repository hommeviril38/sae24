# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1685792622.1651962
_enable_loop = True
_template_filename = 'c:/Users/louis/Desktop/Alexandre_Louis_SAE23_liv1/res/templates/vente.html'
_template_uri = 'vente.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        montants_enchere_max = context.get('montants_enchere_max', UNDEFINED)
        message = context.get('message', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html lang="fr">\r\n<head>\r\n  <meta charset="UTF-8">\r\n  <title>SUPERMOTARD</title>\r\n  <link rel="stylesheet" href="/css/style.css">\r\n</head>\r\n<body>\r\n\r\n<header>\r\n    <nav>\r\n        <ul>\r\n            <li><a href="index">Accueil</a></li>\r\n            <li class="dropdown">\r\n                <a href="motos">Motos</a>\r\n                <div class="dropdown-content">\r\n                    <a href="motos">Visualiser toutes les motos</a>\r\n                    <a href="motos_KTM">Visualiser les motos de la marque KTM</a>\r\n                    <a href="motos_recentes">Visualiser les motos récentes</a>\r\n                    <a href="motos_pas_chere">Visualiser les motos pas chères</a>\r\n                </div>\r\n            </li>\r\n            <li class="dropdown">\r\n            <a href="pilotes">Pilotes</a>\r\n            <div class="dropdown-content">\r\n                <a href="pilotes">Visualiser les pilotes existants</a>\r\n                <a href="ajouter_pilotes">Ajouter des pilotes</a>\r\n                <a href="modifier_pilotes">Modifier des pilotes</a>\r\n                <a href="supprimer_pilotes">Supprimer des pilotes</a>\r\n            </div>\r\n            </li>\r\n            <li class="dropdown">\r\n            <a href="vente">Vente</a>\r\n            <div class="dropdown-content">\r\n                <a href="utilisateurs">Ajouter un nouvel utilisateur</a>\r\n                <a href="vente">Vente aux enchères</a>\r\n            </div>\r\n            </li>\r\n        </ul>\r\n    </nav>\r\n</header>\r\n\r\n  <main>\r\n    <h1>Vente aux enchères</h1>\r\n\r\n    <form action="encherir" method="post">\r\n      <label for="id_enchere">Numéro de l\'enchère à laquelle vous voulez participer (1, 2, 3 ou 4) :</label>\r\n      <input type="number" id="id_enchere" name="id_enchere" required>\r\n      <br>\r\n      <label for="id_utilisateur">Identifiant d\'utilisateur (Si vous n\'en possédez pas, enregistrez vous sur la page dédié):</label>\r\n      <input type="text" id="id_utilisateur" name="id_utilisateur" required>\r\n      <br>\r\n      <label for="montant_enchere">Montant auquel vous voulez enchérir :</label>\r\n      <input type="number" id="montant_enchere" name="montant_enchere" required>\r\n      <br>\r\n      <label for="date">Date de l\'enchère :</label>\r\n      <input type="datetime-local" id="date_enchere" name="date_enchere" required>\r\n      <br>\r\n      <input type="submit" value="Enchérir">\r\n    </form>\r\n\r\n')
        if message : 
            __M_writer('    <div class="success-message">\r\n      ')
            __M_writer(str(message))
            __M_writer('\r\n    </div>\r\n')
        __M_writer('\r\n    <div class="enchere-info">\r\n')
        for id_enchere, montant_enchere_max in montants_enchere_max :
            __M_writer("      <p>Montant actuel de l'enchère numéro ")
            __M_writer(str( id_enchere ))
            __M_writer(' : ')
            __M_writer(str( montant_enchere_max ))
            __M_writer('</p>\r\n')
        __M_writer('    </div>    \r\n\r\n    <div class="fiches">\r\n      <div class="fiche" id="ktm450">\r\n        <img src="/image/moto_thomas_corsi.png" alt="KTM 450 EXC-F">\r\n        <h2>Enchère 1</h2>\r\n        <div class="prix-base">\r\n          L\'enchère débute à  1 000 €\r\n        </div>\r\n        <br><br>\r\n        <p>Marque : KTM <br><br>\r\n          Modèle : EXC-F <br><br>\r\n          Année de fabrication : 2022<br><br>\r\n          Cylindrée : 450 cm2<br><br>\r\n          Prix neuf : 11 149 €<br><br>\r\n          Propriétaire :\r\n          <a href="pilotes#thomas" style="text-decoration: none;"> Thomas corsi</a></p>\r\n      </div>\r\n\r\n      <div class="fiche" id="sherco">\r\n        <img src="/image/moto_sherco.png" alt="SHERCO 450 SEF-R">\r\n        <h2>Enchère 2</h2>\r\n        <div class="prix-base">\r\n          L\'enchère débute à  1 000 €\r\n        </div>\r\n        <br><br>\r\n        <p>Marque : SHERCO <br><br>\r\n          Modèle : SEF-R <br><br>\r\n          Année de fabrication : 2016<br><br>\r\n          Cylindrée : 450 cm2<br><br>\r\n          Prix neuf : 10 385 €<br><br>\r\n          Propriétaire :\r\n          <a href="pilotes#sherco" style="text-decoration: none;"> Shercobike</a></p>\r\n      </div>\r\n\r\n      <div class="fiche" id="kawa">\r\n        <img src="/image/moto_tekstunt.jpeg" alt="KAWASAKI 450 KX">\r\n        <h2>Enchère 3</h2>\r\n        <div class="prix-base">\r\n          L\'enchère débute à  1 000 €\r\n        </div>\r\n        <br><br>\r\n        <p>Marque : KAWASAKI <br><br>\r\n          Modèle : KX <br><br>\r\n          Année de fabrication : 2022<br><br>\r\n          Cylindrée : 450 cm2<br><br>\r\n          Prix neuf : 9 099 €<br><br>\r\n          Propriétaire :\r\n          <a href="pilotes#tekstunt" style="text-decoration: none;"> Tekstunt</a></p>\r\n      </div>\r\n\r\n      <div class="fiche" id="TM">\r\n        <img src="/image/moto_thomas_chareyre.png" alt="TM SMK 450 ES FI">\r\n        <h2>Enchère 4</h2>\r\n        <div class="prix-base">\r\n          L\'enchère débute à  1 000 €\r\n        </div>\r\n        <br><br>\r\n        <p>Marque : TM Racing<br><br>\r\n          Modèle : SMK ES FI<br><br>\r\n          Année de fabrication : 2023<br><br>\r\n          Cylindrée : 450 cm2<br><br>\r\n          Prix neuf : 14 599 €<br><br>\r\n          Propriétaire :\r\n          <a href="pilotes#thomas_chareyre" style="text-decoration: none;"> Thomas Chareyre</a></p>\r\n      </div>\r\n    </div>\r\n\r\n  </main>\r\n  \r\n\r\n  <footer>\r\n    <p>C\'est pas de la moto, c\'est du SUPERMOT !</p>\r\n  </footer>\r\n\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "c:/Users/louis/Desktop/Alexandre_Louis_SAE23_liv1/res/templates/vente.html", "uri": "vente.html", "source_encoding": "utf-8", "line_map": {"16": 0, "23": 1, "24": 62, "25": 63, "26": 64, "27": 64, "28": 67, "29": 69, "30": 70, "31": 70, "32": 70, "33": 70, "34": 70, "35": 72, "41": 35}}
__M_END_METADATA
"""
