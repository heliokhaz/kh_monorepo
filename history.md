# `monorepo` history

## `monorepo` - creating locally

1. mdc /home/khaz/softdev/python/dev/softdev/github/monorepo

2. subfolders, files:

2.1 m_utils/src/m_utils/
2.2 m_utils/tests/
2.3 m_softdev/src/m_softdev/
2.4 m_softdev/tests/
2.5 touch m_utils/src/m_utils/__init__.py
2.6 touch m_softdev/src/m_softdev/__init__.py

3. script file with folders/files creation:

touch …/monorepo/init.sh

```shell title=init.sh
mkdir -p m_utils/src/m_utils m_utils/tests m_softdev m_softdev/src m_softdev/tests
mkdir -p m_softdev/src/m_softdev m_softdev/tests
touch m_utils/src/m_utils/__init__.py
touch m_softdev/src/m_softdev/__init__.py
```

### git initialization

```shell title=git_init.sh
git init
echo "__pycache__/" >> .gitignore
echo ".pytest_cache/" >> .gitignore
echo "*.pyc" >> .gitignore
```
```shell
./git_init.sh 
Zainicjowano puste repozytorium Gita w /home/khaz/softdev/python/dev/softdev/github/monorepo/.git/
```

#### first git commit

git add .
git commit -m "Initial monorepo structure with m_utils and m_softdev"

### KROK 4 – Stworzenie repo na GitHubie

Masz dwie opcje:

####🅰️ Z GUI (prościej)

Wejdź na https://github.com/new

Nazwij repozytorium: monorepolib

Nie zaznaczaj „Initialize with README” (bo już masz lokalne)

Kliknij „Create repository”

Skopiuj adres (np. https://github.com/pykhaz/monorepolib.git)
https://github.com/heliokhaz/kh_monorepo
https://github.com/heliokhaz/kh_monorepo.git
git@github.com:heliokhaz/kh_monorepo.git

####🔗 KROK 5 – Połączenie zdalnego repo z lokalnym

W terminalu:

git remote add origin https://github.com/pykhaz/monorepolib.git
git branch -M main
git push -u origin main


Gotowe — Twoje lokalne repo jest teraz zsynchronizowane z GitHubem.
Z każdą zmianą:

git add .
git commit -m "opis zmian"
git push

###🧰 KROK 6 – (Opcjonalnie) Dodanie Hatch i Pytest

W katalogu głównym:

hatch new m_utils
hatch new m_softdev


...ale to by nadpisało struktury, więc raczej lepiej:

stwórz plik pyproject.toml taki jak wcześniej Ci przygotowałem,

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "monorepolib"
version = "0.1.0"
description = "Monorepo containing m_utils and m_softdev packages"
authors = [{ name = "pykhaz" }]
readme = "README.md"
requires-python = ">=3.8"

[tool.hatch.build.targets.wheel]
packages = [
  "m_utils/src/m_utils",
  "m_softdev/src/m_softdev"
]

[tool.hatch.metadata]
allow-direct-references = true

[tool.hatch.envs.default]
dependencies = [
  "pytest",
]

[tool.pytest.ini_options]
testpaths = [
  "m_utils/tests",
  "m_softdev/tests"
]
pythonpath = [
  "m_utils/src",
  "m_softdev/src"
]
```

a potem uruchom:

hatch run pytest

🚀 Alternatywnie — zacznij od GitHub (i potem klonuj lokalnie)

Jeśli wolisz „z drugiej strony”:

Utwórz puste repo monorepolib na GitHubie

Następnie:

cd ~/Projects
git clone https://github.com/pykhaz/monorepolib.git
cd monorepolib
mkdir -p m_utils/src/m_utils ...


Dalej robisz to samo, tylko od kroku 2.

Chcesz, żebym przygotował gotowy zestaw komend Bash (do wklejenia w terminal, który utworzy cały szkielet monorepo i wrzuci pierwszy commit na GitHub)?
Jeśli tak, napisz tylko:
✅ „tak, zrób wersję bash z moim nickiem GitHub (pykhaz)”
