WARNING : This project is an early development version

The actual frontend is a forked version of Grapheditor, an exemple of the mxGraph library on Apache 2 license, sharing Draw.io codebase.
All files in the grapheditor directory belongs to them, unless excplicitly told otherwise.



Pour lancer le serveur :
Installer Flask :
python -m pip install flask
Lancer le serveur :
./server.py

Puis se connecter sur localhost:5000 depuis un navigateur.

Les programmes python du répertoire ont été écrits par nous-même, les fichiers 
contenus dans le répertoire "grapheditor" font partie de la bibliothèque mxGraph 
dont nous avons modifié l'exemple d'éditeur de graphe comme il est recommandé 
dans la documentation. Certains fichiers comme /grapheditor/www/js/LayerMain.js 
ont été eux créés par nous-même. Les modifications sont précédées d'un commentaire 
commencant par :CHANGED: et les ajouts d'un commentaire commencant par :ADDED:. 

Le bouton "Save" du menu "File" de la barre du haut permet de générer un fichier XML.
Le bouton "Generate Python" permet générer un code python correspondant au graphe créé
 dans l'interface graphique.

