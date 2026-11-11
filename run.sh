#!/bin/bash

# Script para iniciar o servidor do sistema de entrega de provas

echo "Iniciando servidor do sistema de entrega de provas..."

# Ativar ambiente virtual
source venv/bin/activate

# Verificar se o arquivo da prova existe
if [ ! -f "provas/prova.pdf" ]; then
    echo "Atenção: Arquivo de prova não encontrado em provas/prova.pdf"
    echo "Por favor, coloque a prova em PDF na pasta provas/ com o nome prova.pdf"
fi

# Iniciar o servidor Flask
python server.py