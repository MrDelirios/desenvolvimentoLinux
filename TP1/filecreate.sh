#!/bin/bash

cd "$1"

Ext=("png" "mp4" "mpv" "txt" "jpg" "pdf" "exe")
i=1
while [[ $i -lt $2 ]]; do
    rand=$((RANDOM % ${#Ext[@]}))  # Corrigindo o acesso ao índice aleatório
    touch "$i.${Ext[rand]}"  # Usando o nome correto do array
    ((i++))
done

