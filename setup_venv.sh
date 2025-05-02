#!/bin/bash

echo "🔧 Skapar virtuell miljö i .venv ..."
python3.13 -m venv .venv

echo "✅ .venv skapad."

echo "📦 Installerar pip i .venv ..."
source .venv/bin/activate
python -m ensurepip --upgrade --default-pip

echo "📦 Installerar ipykernel ..."
pip install ipykernel

echo "🧠 Registrerar kernel för VS Code ..."
python -m ipykernel install --user --name=exercises --display-name "Python (.venv)"

echo "✅ Klar! Välj 'Python (.venv)' som kernel i VS Code."



## kör detta i terminalen:

##  chmod +x setup_venv.sh
##  ./setup_venv.sh