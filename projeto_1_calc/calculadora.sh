#!/bin/bash

echo "Script automático para execução da Calculadora"

# Script no caminho /home/danilocda/ebac/analise_dados/modulo1/python

echo "Entrando no caminho onde está o script"

cd /home/danilocda/ebac/analise_dados/modulo1/python/

echo "Atualizando python"

sudo apt update
sudo apt install python3

echo "Executando script calculadora.py"

python3 calculadora.py
