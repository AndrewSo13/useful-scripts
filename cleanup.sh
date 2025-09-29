#!/usr/bin/env bash
# Видаляє тимчасові файли у вказаній директорії
set -e
DIR="${1:-.}"
find "$DIR" -type f \( -name "*.tmp" -o -name "*.log" -o -name "*~" \) -print -delete
echo "Готово."
