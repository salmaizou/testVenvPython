# Créer une CI avec GitHub Actions

## 1. Qu'est-ce que la CI ?

**CI** signifie **Continuous Integration** (Intégration Continue).

L'objectif est de vérifier automatiquement que le projet fonctionne correctement lorsqu'on modifie le code.

Par exemple :

```text
Développeur
    │
    │ git push
    ▼
GitHub
    │
    ▼
GitHub Actions
    │
    ▼
Machine Ubuntu temporaire
    │
    ├── Récupérer le code
    ├── Installer Python
    ├── Installer les dépendances
    └── Lancer les tests
            │
            ▼
       Tests réussis ✅
       ou
       Tests échoués ❌
```

Cela permet de détecter rapidement les problèmes avant de fusionner du code dans `main`.

---

# 2. Créer le dossier GitHub Actions

À la racine du projet, créer le dossier :

```text
.github/
└── workflows/
```

La commande peut être :

```bash
mkdir -p .github/workflows
```

---

# 3. Créer le fichier `CI.yml`

Dans le dossier `workflows`, créer :

```text
.github/
└── workflows/
    └── CI.yml
```

On peut utiliser :

```bash
touch .github/workflows/CI.yml
```

> L'extension `.yml` signifie que le fichier utilise le format **YAML**, un format utilisé pour écrire la configuration du workflow.

---

# 4. Donner un nom au workflow

Dans `CI.yml` :

```yaml
name: CI
```

`name` permet de donner un nom au workflow.

Dans GitHub Actions, le workflow apparaîtra donc sous le nom :

```text
CI
```

---

# 5. Définir quand la CI doit se lancer

On utilise `on:` :

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
```

## `push`

```yaml
push:
  branches: [main]
```

Cela signifie :

> Lancer la CI lorsqu'un `push` est effectué sur la branche `main`.

Par exemple :

```bash
git add .
git commit -m "ajout fonctionnalité"
git push origin main
```

---

## `pull_request`

```yaml
pull_request:
  branches: [main]
```

Cela signifie :

> Lancer la CI lorsqu'une Pull Request est créée ou modifiée pour être fusionnée vers `main`.

Par exemple :

```text
develop
   │
   │ Pull Request
   ▼
 main
```

GitHub peut alors vérifier le code avant la fusion.

---

# 6. Créer un job

On utilise :

```yaml
jobs:
  test:
```

`jobs` contient les différents travaux que GitHub doit effectuer.

Ici, on crée un job appelé :

```text
test
```

Le nom `test` est libre. On pourrait également utiliser :

```yaml
jobs:
  verification:
```

---

# 7. Choisir la machine

On ajoute :

```yaml
runs-on: ubuntu-latest
```

Cela signifie que GitHub va créer une **machine virtuelle Ubuntu temporaire** pour exécuter le job.

```text
GitHub
   │
   ▼
Machine Ubuntu temporaire
   │
   └── exécution de la CI
```

Cette machine est indépendante de notre ordinateur personnel.

---

# 8. Récupérer le code du projet

On ajoute :

```yaml
steps:
  - name: Récupérer le code
    uses: actions/checkout@v4
```

## Que signifie `actions/checkout@v4` ?

Cette instruction utilise une action GitHub appelée `checkout`.

```text
actions / checkout @ v4
   │          │       │
   │          │       └── version 4
   │          └────────── action checkout
   └───────────────────── organisation GitHub
```

Son rôle est de **récupérer le contenu du dépôt GitHub sur la machine Ubuntu**.

Sans cette étape, la machine créée par GitHub ne disposerait pas automatiquement des fichiers de notre projet.

---

# 9. Installer Python

On ajoute :

```yaml
- name: Installer Python
  uses: actions/setup-python@v5
  with:
    python-version: "3.12"
```

`actions/setup-python@v5` est une action permettant de configurer Python.

```yaml
with:
  python-version: "3.12"
```

indique que nous voulons utiliser **Python 3.12**.

---

# 10. Installer les dépendances

Si le projet possède un fichier :

```text
requirements.txt
```

on peut installer les dépendances avec :

```yaml
- name: Installer les dépendances
  run: |
    pip install -r requirements.txt
```

### `run`

`run` signifie :

> Exécuter une commande dans le terminal de la machine Ubuntu.

La commande :

```bash
pip install -r requirements.txt
```

demande à `pip` de lire `requirements.txt` et d'installer toutes les bibliothèques indiquées.

Par exemple, si `requirements.txt` contient :

```text
Flask==3.1.3
gunicorn==26.2.0
pytest
```

alors ces bibliothèques seront installées dans la machine utilisée par la CI.

---

# 11. Lancer les tests

Pour utiliser `pytest`, on peut ajouter :

```yaml
- name: Lancer les tests
  run: |
    pytest
```

La CI exécutera alors les tests automatiquement.

---

# 12. Fichier `CI.yml` complet

Voici le workflow complet :

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Récupérer le code
        uses: actions/checkout@v4

      - name: Installer Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Installer les dépendances
        run: |
          pip install -r requirements.txt

      - name: Lancer les tests
        run: |
          pytest
```

---

# 13. Comprendre le workflow étape par étape

Lorsqu'on fait :

```bash
git push origin main
```

GitHub déclenche le workflow.

### Étape 1

```yaml
runs-on: ubuntu-latest
```

GitHub crée une machine Ubuntu temporaire.

### Étape 2

```yaml
uses: actions/checkout@v4
```

Le code du dépôt est récupéré sur cette machine.

### Étape 3

```yaml
uses: actions/setup-python@v5
```

Python 3.12 est configuré.

### Étape 4

```yaml
pip install -r requirements.txt
```

Les dépendances du projet sont installées.

### Étape 5

```yaml
pytest
```

Les tests sont exécutés.

---

# 14. Ajouter le fichier à Git

Après avoir créé `CI.yml` :

```bash
git status
```

On devrait voir :

```text
.github/workflows/CI.yml
```

Puis :

```bash
git add .github/workflows/CI.yml
```

Créer le commit :

```bash
git commit -m "ajout de la CI GitHub Actions"
```

Puis envoyer vers GitHub :

```bash
git push origin main
```

---

# 15. Vérifier la CI sur GitHub

Sur GitHub :

```text
Repository
   │
   └── Actions
          │
          └── CI
```

Dans l'onglet **Actions**, on peut voir l'exécution du workflow.

Une exécution réussie apparaît avec :

```text
✓ CI
```

Une exécution échouée apparaît avec :

```text
✗ CI
```

On peut cliquer sur l'exécution pour voir chaque étape et les éventuelles erreurs.

---

# 16. Résumé

Le fichier :

```text
.github/workflows/CI.yml
```

décrit automatiquement ce que GitHub doit faire.

```text
CI.yml
│
├── name
│     └── nom du workflow
│
├── on
│     ├── push
│     └── pull_request
│
└── jobs
      │
      └── test
            │
            ├── ubuntu-latest
            │
            ├── checkout
            │
            ├── Python 3.12
            │
            ├── dépendances
            │
            └── pytest
```

L'idée principale à retenir est :

> **La CI permet de vérifier automatiquement le projet à chaque modification importante du code.**

---

# 17. Les trois notions importantes

### `uses`

```yaml
uses: actions/checkout@v4
```

Utilise une **action existante**.

### `run`

```yaml
run: pytest
```

Exécute une **commande dans le terminal**.

### `runs-on`

```yaml
runs-on: ubuntu-latest
```

Définit **la machine sur laquelle le job sera exécuté**.

---

# 18. CI dans un projet réel

Une CI peut ensuite devenir plus complète :

```text
             Git push / Pull Request
                       │
                       ▼
              GitHub Actions
                       │
                       ▼
                Ubuntu
                       │
              ┌────────┴────────┐
              ▼                 ▼
        Installer Python    Installer dépendances
              │                 │
              └────────┬────────┘
                       ▼
                     pytest
                       │
                 ┌─────┴─────┐
                 ▼           ▼
              SUCCESS       FAIL
                 │           │
                 ▼           ▼
            Code validé   Correction
```

Une fois cette partie maîtrisée, on peut ajouter progressivement **linting, couverture de tests, Docker et CD (Continuous Deployment)**.
