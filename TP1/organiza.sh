#!/bin/bash

# Função para verificar se a pasta existe e criar se necessário
verificar_pasta() {
  local caminho=$1
  local function=$2
  
  if [ ! -d "$caminho" ]; then
    if [ "$function" == "n" ]; then
      echo "A pasta '$caminho' não existe."
      exit 1
    elif [ "$function" == "y" ]; then
      echo "A pasta '$caminho' não existe. Criando..."
      mkdir -p "$caminho" || { echo "Falha ao criar a pasta '$caminho'."; exit 1; }
    fi
  fi
}

# Função para mover arquivos conforme a extensão
mover_arquivos() {
  local origem=$1
  local destino=$2

  # Encontrar todos os arquivos e mover para pastas conforme a extensão
  for arquivo in "$origem"/*.*; do
    # Verificar se é um arquivo (evitar tentar mover diretórios)
    if [ ! -f "$arquivo" ]; then
      continue
    fi

    # Obter a extensão do arquivo
    extensao="${arquivo##*.}"

    # Ignorar arquivos sem extensão (sem ponto)
    if [ "$extensao" == "$arquivo" ]; then
      continue
    fi

    # Criar a pasta com o nome da extensão dentro da pasta destino, se não existir
    pasta_destino="$destino/$extensao"
    [ ! -d "$pasta_destino" ] && mkdir -p "$pasta_destino"

    # Mover o arquivo para a pasta correspondente na pasta destino
    mv -- "$arquivo" "$pasta_destino/" || { echo "Falha ao mover '$arquivo'."; exit 1; }
  done
}

# Função principal
organizar_arquivos() {
  # Verificar se os parâmetros foram passados
  if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Uso: $0 <pasta-origem> <pasta-destino>"
    exit 1
  fi

  # Caminhos das pastas
  pasta="$1"
  destino="$2"

  # Verificar se as pastas existem
  verificar_pasta "$pasta" "n"  # Não cria a pasta origem
  verificar_pasta "$destino" "y"  # Cria a pasta destino caso não exista

  # Mover os arquivos
  mover_arquivos "$pasta" "$destino"

  echo "Arquivos organizados com sucesso!"
}

# Chama a função principal passando os argumentos
organizar_arquivos "$1" "$2"

