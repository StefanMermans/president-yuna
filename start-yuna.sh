#!/usr/bin/env bash

projectDir=$(dirname "$0")

cd "$projectDir" && venv/bin/python3 src/main.py --type "$1"
