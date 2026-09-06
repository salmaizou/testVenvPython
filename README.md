# testVenvPython
# 🐍 Python Application avec Venv, Git et GitHub

Ce projet montre comment créer une application Python avec un environnement virtuel (`venv`), installer les dépendances, exécuter l'application, utiliser Git pour gérer les versions et publier le projet sur GitHub.

---

## 📋 Prérequis

Vérifier que Python et Git sont installés :

```bash
python3 --version
git --version
```

Si Python est installé, une version s'affiche par exemple :

```text
Python 3.12.3
```

---

# 1. 📁 Créer le projet

Créer un dossier pour le projet :

```bash
mkdir testVenvPython
```

Entrer dans le dossier :

```bash
cd testVenvPython
```

Vérifier le contenu :

```bash
ls
```

---

# 2. 🐍 Créer l'environnement virtuel

Créer un environnement virtuel appelé `salmaenv` :

```bash
python3 -m venv salmaenv
```

Cela crée un dossier :

```text
testVenvPython/
└── salmaenv/
```

L'environnement virtuel permet d'installer les bibliothèques Python du projet indépendamment du système.

---

# 3. ▶️ Activer l'environnement virtuel

Sur Linux / Ubuntu :

```bash
source salmaenv/bin/activate
```

Après activation, le terminal affiche généralement :

```text
(salmaenv)
```

Par exemple :

```text
(salmaenv) user@computer:~/Documents/testVenvPython$
```

---

# 4. 🔎 Vérifier Python

Une fois l'environnement activé :

```bash
python --version
```

Vérifier également quel Python est utilisé :

```bash
which python
```

Le chemin doit pointer vers l'environnement virtuel :

```text
.../testVenvPython/salmaenv/bin/python
```

---

# 5. 📝 Créer l'application Python

Créer un fichier Python :

```bash
nano appTest.py
```

Exemple de code :

```python
print("Bonjour depuis mon application Python !")
```

Sauvegarder avec :

```text
CTRL + O
ENTER
CTRL + X
```

---

# 6. ▶️ Exécuter l'application

Avec l'environnement virtuel activé :

```bash
python appTest.py
```

Résultat :

```text
Bonjour depuis mon application Python !
```

---

# 7. 📦 Installer des bibliothèques Python

Mettre à jour `pip` :

```bash
python -m pip install --upgrade pip
```

Installer une bibliothèque, par exemple Flask :

```bash
pip install flask
```

Vérifier les bibliothèques installées :

```bash
pip list
```

---

# 8. 📄 Créer le fichier requirements.txt

Pour enregistrer les dépendances du projet :

```bash
pip freeze > requirements.txt
```

Vérifier le fichier :

```bash
cat requirements.txt
```

Il contiendra les bibliothèques nécessaires au projet.

> Remarque : le nom recommandé est `requirements.txt` avec un **s** à `requirements`.

---

# 9. 🔄 Réinstaller les dépendances

Sur une nouvelle machine, après avoir activé le venv :

```bash
pip install -r requirements.txt
```

Cela installe toutes les dépendances nécessaires au projet.

---

# 10. 🚫 Créer le fichier .gitignore

Créer le fichier :

```bash
nano .gitignore
```

Ajouter :

```text
salmaenv/
__pycache__/
*.pyc
.env
```

Explications :

```text
salmaenv/
```

➡️ empêche Git de suivre l'environnement virtuel.

```text
__pycache__/
*.pyc
```

➡️ empêche Git de suivre les fichiers Python temporaires.

```text
.env
```

➡️ empêche Git de publier les variables d'environnement et informations sensibles.

---

# 11. 🔧 Initialiser Git

Dans le dossier du projet :

```bash
git init
```

Vérifier l'état du dépôt :

```bash
git status
```

---

# 12. ➕ Ajouter les fichiers au staging

Ajouter tous les fichiers autorisés par `.gitignore` :

```bash
git add .
```

Vérifier :

```bash
git status
```

Les fichiers devraient apparaître dans :

```text
Changes to be committed:
```

L'environnement `salmaenv/` ne doit pas apparaître.

---

# 13. 💾 Créer le premier commit

Créer le premier commit :

```bash
git commit -m "Premier commit"
```

Vérifier :

```bash
git status
```

Si tout est correctement enregistré :

```text
nothing to commit, working tree clean
```

---

# 14. 🌿 Vérifier la branche

Afficher la branche actuelle :

```bash
git branch
```

Si nécessaire, utiliser `main` :

```bash
git branch -M main
```

---

# 15. ☁️ Créer le repository GitHub

Se connecter à GitHub et créer un nouveau repository.

Nom du repository :

```text
testVenvPython
```

Pour un projet déjà existant localement :

* README → ne pas ajouter
* `.gitignore` → ne pas ajouter
* License → facultatif

Le `.gitignore` existe déjà localement.

Choisir :

```text
Public
```

si le projet doit être visible publiquement.

---

# 16. 🔗 Connecter le projet local à GitHub

Après avoir créé le repository GitHub, copier son URL.

Ajouter le repository distant :

```bash
git remote add origin https://github.com/USERNAME/testVenvPython.git
```

Remplacer `USERNAME` par son nom d'utilisateur GitHub.

Vérifier :

```bash
git remote -v
```

---

# 17. 🚀 Envoyer le projet sur GitHub

Envoyer la branche `main` :

```bash
git push -u origin main
```

Lors du premier `push`, GitHub peut demander une authentification.

---

# 18. 🌍 Vérifier que le projet est public

Ouvrir le repository GitHub.

Si le repository est configuré en `Public`, les autres personnes peuvent voir :

```text
appTest.py
requirements.txt
.gitignore
README.md
```

Mais elles ne doivent pas voir :

```text
salmaenv/
.env
__pycache__/
```

---

# 19. 🔄 Modifier l'application

Après avoir modifié `appTest.py` :

```bash
python appTest.py
```

Tester l'application.

Puis vérifier les changements :

```bash
git status
```

---

# 20. 📤 Publier les modifications

Ajouter les modifications :

```bash
git add .
```

Créer un commit :

```bash
git commit -m "Modification de l'application"
```

Envoyer sur GitHub :

```bash
git push
```

---

# 21. 📥 Récupérer un projet depuis GitHub

Sur une autre machine :

```bash
git clone https://github.com/USERNAME/testVenvPython.git
```

Entrer dans le projet :

```bash
cd testVenvPython
```

Créer un nouvel environnement virtuel :

```bash
python3 -m venv salmaenv
```

Activer l'environnement :

```bash
source salmaenv/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Exécuter l'application :

```bash
python appTest.py
```

---

# 22. 🔐 Variables d'environnement

Pour les informations sensibles, utiliser un fichier `.env`.

Créer :

```bash
nano .env
```

Exemple :

```text
API_KEY=ma_cle_secrete
DATABASE_PASSWORD=mon_mot_de_passe
```

Le fichier `.env` doit être présent dans `.gitignore` :

```text
.env
```

Ainsi, Git ne le publiera pas sur GitHub.

⚠️ Ne jamais mettre directement une clé API, un mot de passe ou un token dans le code avant de publier un repository public.

---

# 23. 🧹 Commandes Git importantes

Voir l'état du projet :

```bash
git status
```

Voir l'historique :

```bash
git log
```

Voir les fichiers suivis :

```bash
git ls-files
```

Ajouter un fichier :

```bash
git add fichier.py
```

Ajouter tous les fichiers :

```bash
git add .
```

Créer un commit :

```bash
git commit -m "Message du commit"
```

Envoyer sur GitHub :

```bash
git push
```

Récupérer les modifications :

```bash
git pull
```

Voir le repository distant :

```bash
git remote -v
```

---

# 24. 🛑 Désactiver le venv

Lorsque le travail est terminé :

```bash
deactivate
```

Le `(salmaenv)` disparaît du terminal.

Pour le réactiver :

```bash
source salmaenv/bin/activate
```

---

# 25. 📁 Structure finale du projet

Le projet peut avoir cette structure :

```text
testVenvPython/
│
├── salmaenv/          # Environnement virtuel - ignoré par Git
│
├── appTest.py         # Application Python
│
├── requirements.txt   # Dépendances Python
│
├── .gitignore         # Fichiers ignorés par Git
│
└── README.md          # Documentation du projet
```

Sur GitHub, `salmaenv/` ne sera pas présent.

---

# 🚀 Résumé : de zéro à GitHub

Voici la version rapide de toutes les commandes :

```bash
# Créer le projet
mkdir testVenvPython
cd testVenvPython

# Créer le venv
python3 -m venv salmaenv

# Activer le venv
source salmaenv/bin/activate

# Créer l'application
nano appTest.py

# Installer les dépendances
python -m pip install --upgrade pip
pip install flask

# Enregistrer les dépendances
pip freeze > requirements.txt

# Créer .gitignore
nano .gitignore

# Initialiser Git
git init

# Ajouter les fichiers
git add .

# Vérifier
git status

# Premier commit
git commit -m "Premier commit"

# Utiliser main
git branch -M main

# Connecter Git à GitHub
git remote add origin https://github.com/USERNAME/testVenvPython.git

# Publier
git push -u origin main
```

---

# 🔁 Pour les prochaines modifications

À chaque modification :

```bash
git status
git add .
git commit -m "Description de la modification"
git push
```

---

# 🎯 Workflow complet

```text
Créer le projet
      ↓
Créer le venv
      ↓
Activer le venv
      ↓
Développer l'application
      ↓
Installer les dépendances
      ↓
requirements.txt
      ↓
.gitignore
      ↓
git init
      ↓
git add .
      ↓
git commit
      ↓
Créer le repository GitHub
      ↓
git remote add origin
      ↓
git push
      ↓
Repository GitHub public
```

## 📝 Technologies utilisées

* Python
* Python `venv`
* pip
* Git
* GitHub
* Flask (exemple de dépendance)
