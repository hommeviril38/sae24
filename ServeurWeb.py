import os
import cherrypy
from cherrypy import HTTPRedirect
from mako.lookup import TemplateLookup
from mako.exceptions import TemplateLookupException
from CLI import connexion_mysql,visualiser_motos, visualiser_motos_KTM, visualiser_motos_recente, visualiser_motos_pas_chere, visualiser_pilotes, ajouter_pilote, supprimer_pilote, modifier_pilote, ajouter_enchere, ajouter_utilisateur, visualiser_utilisateurs, obtenir_montant_enchere
from urllib.parse import quote

chemin = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'res', 'templates')
chemin_images = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'res', 'images')
chemin_css = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'res', 'css')
mylookup = TemplateLookup(directories=[chemin], input_encoding='utf-8', module_directory='res/tmp/mako_modules')
conn = connexion_mysql()


class InterfaceWebsae23(object):     
    ###### Page d'accueil #############
    @cherrypy.expose
    def index(self):
        mytemplate = mylookup.get_template("index.html")
        return mytemplate.render()
    
    ###### Pages d'affichages ###########
    @cherrypy.expose
    def motos(self):
        motos = visualiser_motos(conn)
        mytemplate = mylookup.get_template("motos.html")
        html = mytemplate.render(motos=motos)
        return html

    @cherrypy.expose
    def motos_KTM(self):
        motos = visualiser_motos_KTM(conn)
        mytemplate = mylookup.get_template("motos_KTM.html")
        html = mytemplate.render(motos=motos)
        return html

    @cherrypy.expose
    def motos_recentes(self):
        motos = visualiser_motos_recente(conn)
        mytemplate = mylookup.get_template("motos_recentes.html")
        html = mytemplate.render(motos=motos)
        return html
    
    @cherrypy.expose
    def motos_pas_chere(self):
        motos = visualiser_motos_pas_chere(conn)
        mytemplate = mylookup.get_template("motos_pas_chere.html")
        html = mytemplate.render(motos=motos)
        return html
    
    @cherrypy.expose
    def pilotes(self):
        pilotes = visualiser_pilotes(conn)
        mytemplate = mylookup.get_template("pilotes.html")
        html = mytemplate.render(pilotes=pilotes)
        return html
    
    ###### Pages d'insertion ###########

    @cherrypy.expose
    def ajouter_pilotes(self, id_pilote=None, nom=None, statut=None, instagram=None, abonnes=None, erreur=None):
        if cherrypy.request.method == 'POST':
            if pilote_existe(conn, id_pilote):
                erreur = "L'ID du pilote existe déjà."
            else:
                ajouter_pilote(conn, id_pilote, nom, statut, instagram, abonnes)
                raise cherrypy.HTTPRedirect("/pilotes")
        try:
            mytemplate = mylookup.get_template("ajouter_pilotes.html")
            return mytemplate.render(erreur=erreur)
        except TemplateLookupException:
            return "Template 'ajouter_pilotes.html' introuvable."
        
    @cherrypy.expose
    def utilisateurs(self, nom=None, id=None, erreur=None):
        if cherrypy.request.method == 'POST':
            if nom and id:
                if utilisateur_existe(conn, id):
                    erreur = "L'utilisateur existe déjà."
                else:
                    ajouter_utilisateur(conn, id, nom)
            
        utilisateurs = visualiser_utilisateurs(conn)
        mytemplate = mylookup.get_template("utilisateurs.html")
        html = mytemplate.render(utilisateurs=utilisateurs, erreur=erreur)  
        return html

    ###### Page de suppression ###########

    @cherrypy.expose
    def supprimer_pilotes(self, id_pilote=None, erreur=None):
        if cherrypy.request.method == 'POST':
            if pilote_existe(conn, id_pilote):
                supprimer_pilote(conn, id_pilote)
                raise cherrypy.HTTPRedirect("/pilotes")
            else:
                erreur = "L'ID du pilote n'existe pas."
        try:
            mytemplate = mylookup.get_template("supprimer_pilotes.html")
            return mytemplate.render(erreur=erreur)
        except TemplateLookupException:
            return "Template 'supprimer_pilotes.html' introuvable."
        
    ###### Page de modification ###########

    @cherrypy.expose
    def modifier_pilotes(self, id_pilote=None, nom=None, statut=None, instagram=None, abonnes=None, erreur=None):
        if cherrypy.request.method == 'POST':
            if pilote_existe(conn, id_pilote):
                modifier_pilote(conn, id_pilote, nom, statut, instagram, abonnes)
                raise cherrypy.HTTPRedirect("/pilotes")
            else:
                erreur = "L'ID du pilote n'existe pas."
        try:
            mytemplate = mylookup.get_template("modifier_pilotes.html")
            return mytemplate.render(erreur=erreur)
        except TemplateLookupException:
            return "Template 'modifier_pilotes.html' introuvable."

    ###### Vente aux enchères ###########

    @cherrypy.expose
    @cherrypy.tools.expires(secs=-1, force=True)
    def vente(self, **kwargs):
        id_encheres = [1, 2, 3, 4]
        montants_enchere_max = []
        
        for id_enchere in id_encheres:
            montant_enchere_max = obtenir_montant_enchere(conn, id_enchere)
            montants_enchere_max.append((id_enchere, montant_enchere_max))
        
        message = kwargs.get('message', None)
        mytemplate = mylookup.get_template("vente.html")
        return mytemplate.render(message=message, montants_enchere_max=montants_enchere_max)

    @cherrypy.expose
    def encherir(self, id_enchere, id_utilisateur=None, montant_enchere=None, date_enchere=None):

        if not enchere_existe(conn, id_enchere):
            message = f"L'enchère numéro {id_enchere} n'existe pas, veuillez participer à une enchère existante."
            raise HTTPRedirect("/vente?message=" + quote(message))

        if not utilisateur_existe(conn, id_utilisateur):
            message = f"L'utilisateur {id_utilisateur} n'existe pas, veuillez vous enregistrer sur la page dédié."
            raise HTTPRedirect("/vente?message=" + quote(message))

        ajouter_enchere(conn, id_enchere, id_utilisateur, montant_enchere, date_enchere)

        message = f"L'utilisateur {id_utilisateur} a placé une enchère à {montant_enchere}€ sur l'enchère numéro {id_enchere}"
        raise HTTPRedirect("/vente?message=" + quote(message))        


    ###### Fonctions nécessaires à la gestions des erreurs ###########

def pilote_existe(conn, id_pilote):
    requete = "SELECT COUNT(*) FROM pilotes WHERE id_pilote = %s"
    donnees = (id_pilote,)
    cursor = conn.cursor()
    cursor.execute(requete, donnees)
    count = cursor.fetchone()[0]
    cursor.close()
    return count > 0

def utilisateur_existe(conn, id_utilisateur):
    requete = "SELECT COUNT(*) FROM utilisateurs WHERE id_utilisateur = %s"
    donnees = (id_utilisateur,)
    cursor = conn.cursor()
    cursor.execute(requete, donnees)
    count = cursor.fetchone()[0]
    cursor.close()
    return count > 0

def enchere_existe(conn, id_enchere):
    requete = "SELECT COUNT(*) FROM encheres WHERE id_enchere = %s"
    donnees = (id_enchere,)
    cursor = conn.cursor()
    cursor.execute(requete, donnees)
    count = cursor.fetchone()[0]
    cursor.close()
    return count > 0


    ###### Démarrage du Serveur #############

if __name__ == '__main__':
    cherrypy.tree.mount(InterfaceWebsae23(), '/', {
        '/image': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(chemin_images)
        },
        '/css': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(chemin_css)
        }
    })
    cherrypy.engine.start()
    cherrypy.engine.block()