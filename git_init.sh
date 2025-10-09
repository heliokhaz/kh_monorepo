#!/usr/bin/env zsh

# git_init.sh
#
# Git initialization
#

git init
echo "__pycache__/" >> .gitignore
echo ".pytest_cache/" >> .gitignore
echo "*.pyc" >> .gitignore
