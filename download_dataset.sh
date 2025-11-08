#!/bin/bash

# Script para download do dataset de vibração de rolamentos do Kaggle
# Autor: AC2 - Processamento de Sinais
# Dataset: https://www.kaggle.com/datasets/vinayak123tyagi/bearing-dataset

# Verifica se o diretório Downloads existe
if [ ! -d ~/Downloads ]; then
    mkdir -p ~/Downloads
fi

# Download do dataset
echo "Iniciando download do dataset de rolamentos..."
curl -L -o ~/Downloads/bearing-dataset.zip \
  https://www.kaggle.com/api/v1/datasets/download/vinayak123tyagi/bearing-dataset

# Verifica se o download foi bem-sucedido
if [ $? -eq 0 ]; then
    echo "Download concluído com sucesso!"
    echo "Arquivo salvo em: ~/Downloads/bearing-dataset.zip"
    echo ""
    echo "Para extrair o arquivo, execute:"
    echo "unzip ~/Downloads/bearing-dataset.zip -d data/"
else
    echo "Erro ao fazer download do dataset."
    echo "Certifique-se de ter configurado as credenciais do Kaggle."
    echo "Mais informações: https://www.kaggle.com/docs/api"
    exit 1
fi

