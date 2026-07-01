#!/usr/bin/env bash
#
# Nachhaker in ein frisches Repo "nachhaker" umziehen – OHNE die alte
# Git-Historie. Das lässt die früher versehentlich committete E-Mail in der
# Historie des ALTEN Repos zurück; das neue Repo startet sauber mit einem
# einzigen Commit.
#
# Voraussetzungen:
#   1) Leeres, öffentliches Repo "nachhaker" bei GitHub anlegen (ohne README).
#   2) Dieses Skript im vorhandenen Klon von letter-lift-sitemap ausführen,
#      mit ausgechecktem/erreichbarem Branch claude/side-income-ideas-hx0vr1.
#
# Nutzung:   ./migrate.sh <github-user>
#   z. B.:   ./migrate.sh ankefischer99-eng
#
set -euo pipefail

USER="${1:?Bitte GitHub-User angeben:  ./migrate.sh <user>}"
SRC_BRANCH="claude/side-income-ideas-hx0vr1"
TMP="$(mktemp -d)"

echo "→ Exportiere aktuellen (bereinigten) Stand von '$SRC_BRANCH' ohne Historie …"
git archive "$SRC_BRANCH" | tar -x -C "$TMP"

cd "$TMP"
git init -q
git checkout -q -b main
git add .
git commit -q -m "Nachhaker: initial import (clean history)"
git remote add origin "https://github.com/$USER/nachhaker.git"

echo "→ Pushe nach https://github.com/$USER/nachhaker.git (main) …"
git push -u origin main

echo ""
echo "✅ Umzug fertig."
echo "   Nächste Schritte im neuen Repo:"
echo "   1) Settings → Pages → Deploy from a branch → main → /(root)"
echo "   2) Impressum/Datenschutz final ausfüllen, DANN erst live schalten"
echo "   3) Altes Repo 'letter-lift-sitemap' kann anschließend gelöscht werden"
