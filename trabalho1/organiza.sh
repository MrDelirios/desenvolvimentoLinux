#!/bin/bash

# SCRIPT CRIADO POR GUSTAVO TEIXEIRA MAGALHÃES
# MATRÍCULA: 0056150
# TRABALHO 1 DE DESENVOLVIMENTO LINUX

set -o errexit

find_and_move(){
	declare -A pastas_criadas
	# PERCORRE OS ARQUIVOS DA PASTA ORIGEM, IGNORANDO SUBPASTAS 
	for i in "$1"/*; do
		if [[ "$i" != "$1" && ! -d "$i" ]]; then 			# VERIFICA SE i NÃO É A PASTA RAIZ OU i NÃO É DIRETÓRIO 
			if [[ "$i" != *.* ]]; then 				# SE O ARQUIVO NÃO TEM EXTENSÃO 
				extension="vazio"
			else
				extension=$(echo "$i" | sed -E "s/.*\.//")		# PEGA A EXTENSÃO DO ARQUIVO
			fi

			if [[ -z "${pastas_criadas[$extension]}" ]]; then			# SE NÃO EXISTE UM DIRETÓRIO PRA EXTENSÃO, ELE É CRIADO 
				mkdir -p "$2"/"$extension"
				pastas_criadas["$extension"]=1 #Marca a pasta como já criada
			fi
			cp "$i" "$2"/"$extension"			# MOVE O ARQUIVO DA EXTENSÃO PRA PASTA DESTINO/EXTENSÃO
		fi
	done
}


# SE A PASTA ORIGEM NÃO EXISTE, TERMINA O PROGRAMA
if [[ ! -d "$1" ]]; then
	echo "ERRO: PASTA ORIGEM INEXISTENTE"
	exit 1
else
	# SE A PASTA ORIGEM ESTIVER VAZIA 
	if [[ -d "$1" && -z "$(ls -A "$1")" ]]; then 
		echo "ERRO: PASTA ORIGEM VAZIA"
		exit 1
	else
		# SE A PASTA DESTINO NÃO EXISTE, CRIA ELA
		if [[ ! -d "$2" ]]; then
			mkdir "$2"
		fi
		find_and_move "$1" "$2"
	fi
fi


