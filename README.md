# Git - Guide Complet des Commandes Essentielles

> Ce guide regroupe les principales commandes Git avec leur rôle, leur syntaxe et des exemples concrets.

---

# Sommaire

1. Initialiser ou récupérer un projet
2. Travailler sur les fichiers
3. Enregistrer les modifications
4. Consulter l'historique
5. Travailler avec les branches
6. Annuler des modifications
7. Les tags
8. Travailler avec GitHub (Remote)
9. Commandes avancées
10. Workflow recommandé
11. Les commandes à connaître

---

# 1. Initialiser ou récupérer un projet

## git init

Initialise un dépôt Git dans le dossier courant.

```bash
git init
```

Exemple :

```bash
mkdir monprojet
cd monprojet
git init
```

Git crée alors :

```
.git/
```

À faire une seule fois lors de la création du projet.

---

## git clone

Télécharge un dépôt Git existant.

```bash
git clone https://github.com/salmaizou/testVenvPython.git
```

Git crée automatiquement le dossier du projet avec tout son historique.

### Différence

```text
git init
↓
Créer un dépôt local

git clone
↓
Récupérer un dépôt existant
```

---

# 2. Travailler sur les fichiers

## git status

Affiche l'état du projet.

```bash
git status
```

Exemple :

```yaml
modified: appTest.py
```

Commande à utiliser très fréquemment.

---

## git add

Ajoute les modifications dans le **Staging Area**.

Ajouter un fichier :

```bash
git add appTest.py
```

Ajouter tous les fichiers :

```bash
git add .
```

Schéma :

```text
Modification
      ↓
   git add
      ↓
 Staging Area
      ↓
 git commit
```

---

## git restore

Annule les modifications non sauvegardées.

```bash
git restore appTest.py
```

Si le fichier est déjà dans le staging :

```bash
git restore --staged appTest.py
git restore appTest.py
```

---

## git rm

Supprime un fichier du projet et de Git.

```bash
git rm ancien.py
```

Puis :

```bash
git commit -m "Suppression de ancien.py"
```

---

## git mv

Renomme ou déplace un fichier.

```bash
git mv appTest.py app.py
```

---

# 3. Enregistrer les modifications

## git commit

Crée un nouveau commit.

```bash
git commit -m "Ajout page accueil"
```

Workflow :

```bash
git add .
git commit -m "Ajout page accueil"
```

Historique :

```text
A → B → C
        ↑
     Nouveau commit
```

---

# 4. Consulter l'historique

## git log

Historique détaillé.

```bash
git log
```

---

## git log --oneline

Historique condensé.

```bash
git log --oneline
```

Exemple :

```text
fd6d50b Setup du projet
9697037 Initial commit
```

---

## git show

Affiche le contenu d'un commit.

Dernier commit :

```bash
git show
```

Commit spécifique :

```bash
git show fd6d50b
```

---

## git diff

Montre les modifications non ajoutées au staging.

```bash
git diff
```

Exemple :

```diff
- return "Bonjour"
+ return "Bonjour Flask"
```

---

## git diff --staged

Affiche les modifications déjà dans le staging.

```bash
git diff --staged
```

Résumé :

```text
git diff
↓
Non staged

git diff --staged
↓
Staged
```

---

## git grep

Recherche un texte dans les fichiers suivis.

```bash
git grep "Flask"
```

---

# 5. Les branches

## git branch

Liste les branches.

```bash
git branch
```

Exemple :

```text
* main
  develop
```

---

## Créer une branche

```bash
git branch develop
```

---

## git switch

Changer de branche.

```bash
git switch develop
```

Créer et changer immédiatement :

```bash
git switch -c develop
```

---

## git merge

Fusionner une branche.

```bash
git switch main
git merge develop
```

Schéma :

```text
develop
    │
    ▼
main
```

---

## git rebase

Réapplique les commits au-dessus d'une nouvelle base.

```bash
git pull --rebase origin main
```

Avant :

```text
A---B---C
     \
      D---E
```

Après :

```text
A---B---C---D'---E'
```

---

# 6. Annuler des modifications

## git reset

### --soft

Annule le commit mais conserve le staging.

```bash
git reset --soft HEAD~1
```

---

### --mixed

Annule le commit et vide le staging.

```bash
git reset --mixed HEAD~1
```

---

### --hard

Annule le commit et supprime toutes les modifications.

```bash
git reset --hard HEAD~1
```

⚠️ Très dangereux.

---

# 7. Les tags

## git tag

Créer un tag.

```bash
git tag v1.0
```

Lister les tags.

```bash
git tag
```

Exemple :

```text
v1.0
v1.1
v2.0
```

---

# 8. Travailler avec GitHub (Remote)

## git remote

Afficher les dépôts distants.

```bash
git remote -v
```

Exemple :

```text
origin https://github.com/... (fetch)
origin https://github.com/... (push)
```

---

## git fetch

Télécharge les informations du serveur sans modifier la branche locale.

```bash
git fetch origin
```

---

## git pull

Télécharge puis fusionne.

```bash
git pull origin main
```

Schéma :

```text
GitHub
   ↓
 fetch
   ↓
 merge
   ↓
Local
```

---

## git pull --rebase

Télécharge puis réapplique les commits locaux.

```bash
git pull --rebase origin main
```

---

## git push

Envoie les commits.

```bash
git push
```

ou

```bash
git push origin main
```

Schéma :

```text
Ordinateur
      │
      ▼
 git push
      │
      ▼
 GitHub
```

---

# 9. Commandes avancées

## git bisect

Trouve automatiquement le commit ayant introduit un bug.

```bash
git bisect start
git bisect bad
git bisect good abc1234
```

Git effectue une recherche binaire.

---

## git help

Documentation Git.

```bash
git help commit
```

ou

```bash
git commit --help
```

Toutes les commandes :

```bash
git help -a
```

---

# 10. Workflow recommandé

## Développer

```text
Modifier le code
        │
        ▼
 git status
        │
        ▼
  git diff
        │
        ▼
 git add .
        │
        ▼
git diff --staged
        │
        ▼
git commit -m "..."
        │
        ▼
  git push
        │
        ▼
   GitHub
```

---

## Récupérer le travail des autres

```text
git pull --rebase
        │
        ▼
Modifier
        │
        ▼
 git add .
        │
        ▼
 git commit
        │
        ▼
 git push
```

---

# 11. Les commandes à connaître

## Niveau débutant

```bash
git init
git clone
git status
git add
git restore
git commit
git log
git log --oneline
git show
git diff
git branch
git switch
git merge
git pull
git push
```

---

## Niveau intermédiaire

```bash
git fetch
git rebase
git reset
git stash
git cherry-pick
git tag
git bisect
```

---

# Résumé

Pour la majorité des projets (Flask, Python, Docker, DevOps, Data Engineering), les commandes essentielles à maîtriser sont :

```text
git status
      ↓
git diff
      ↓
git add .
      ↓
git commit -m "..."
      ↓
git pull --rebase
      ↓
git push
```

Puis apprendre progressivement :

- Branches (`branch`, `switch`, `merge`)
- Rebase
- Reset
- Stash
- Tags

Une bonne maîtrise de ce workflow couvre la très grande majorité des situations rencontrées dans un projet Git professionnel.
