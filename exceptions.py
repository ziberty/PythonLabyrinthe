"""
Ce fichier contient les définitions des exceptions définies pour ce projet.
Pour créer un nouveau type d'exception, il suffit d'hériter de la classe Exception, et de laisser le corps vide.
Ainsi la nouvelle exception récupère automatiquement les constructeur de la classe mère Exception
"""

class AbstractMethodCallException(Exception):
    """ Cette exception est levée lorsqu'on appelle une méthode abstraite.
    On ne doit normalement jamais les appeler puisqu'elles sont par définition redéfinies dans les classes filles
    des classes abstraites ou interfaces.
    """
    pass