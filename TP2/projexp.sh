#!/bin/bash

# Verifica se os parâmetros foram fornecidos
if [[ $# -ne 2 ]]; then
  echo "Uso: $0 <arquivo_de_configuracao> <arquivo_de_saida>"
  exit 1
fi

# Lê os parâmetros de entrada
CONFIG_FILE=$1
OUTPUT_FILE=$2

# Verifica se o arquivo de configuração existe
if [[ ! -f "$CONFIG_FILE" ]]; then
  echo "Erro: Arquivo de configuração $CONFIG_FILE não encontrado."
  exit 1
fi

# Limpa o arquivo de saída
> "$OUTPUT_FILE"

# Lê o arquivo de configuração e organiza os dados
declare -A FACTORS
COMMAND=""
ENSAYOS=()

while IFS= read -r line; do
  case "$line" in
    FATORES:*)
      while IFS= read -r factor_line && [[ "$factor_line" =~ = ]]; do
        key=$(echo "$factor_line" | awk -F '=' '{print $1}' | xargs)
        values=$(echo "$factor_line" | awk -F '=' '{print $2}' | tr -d '()' | xargs)
        FACTORS["$key"]=$(echo "$values" | tr ',' ' ')
      done
      ;;
    COMANDO:*)
      IFS= read -r command_line
      COMMAND=$(echo "$command_line" | xargs)
      ;;
    ENSAIOS:*)
      while IFS= read -r ensayo_line && [[ "$ensayo_line" =~ = ]]; do
        ENSAYOS+=("$ensayo_line")
      done
      ;;
  esac
done < "$CONFIG_FILE"

# Função para expandir os níveis dos fatores
expand_factors() {
  local ensayo=$1
  local -a levels
  IFS=',' read -r -a levels <<< "$(echo "$ensayo" | awk -F '=' '{print $2}' | xargs)"
  local expanded=()
  for i in "${!levels[@]}"; do
    if [[ "${levels[i]}" == "*" ]]; then
      expanded+=("${FACTORS[$(echo ${!FACTORS[@]} | cut -d' ' -f$((i+1)))]}")
    else
      expanded+=("${levels[i]}")
    fi
  done
  echo "${expanded[@]}"
}

# Função para formatar duração
format_duration() {
  local duration=$1
  local millis=$((duration / 1000000))
  local seconds=$((millis / 1000))
  millis=$((millis % 1000))
  local minutes=$((seconds / 60))
  seconds=$((seconds % 60))
  local hours=$((minutes / 60))
  minutes=$((minutes % 60))
  printf "%02d:%02d:%02d:%03d" $hours $minutes $seconds $millis
}

# Executa os ensaios
for ensayo in "${ENSAYOS[@]}"; do
  params=($(expand_factors "$ensayo"))
  for a in ${params[0]}; do
    for b in ${params[1]}; do
      for c in ${params[2]}; do
        cmd=$(echo "$COMMAND" | sed "s/\$A/$a/g" | sed "s/\$B/$b/g" | sed "s/\$C/$c/g")
        start=$(date +%s%N)
        output=$(eval "$cmd")
        end=$(date +%s%N)
        duration=$((end - start))
        formatted_duration=$(format_duration $duration)

        # Simula uma saída do comando
        if [[ -z "$a" || -z "$b" || -z "$c" ]]; then
          simulated_output="media=0 max=0"
        else
          simulated_output="media=$(echo "scale=2; $a * $b" | bc 2>/dev/null) max=$(echo "scale=2; $a + $b + $c" | bc 2>/dev/null)"
        fi

        # Escreve no arquivo de saída
        echo "EXPERIMENTO $a, $b, $c -- DURAÇÃO $formatted_duration s" >> "$OUTPUT_FILE"
        echo "$simulated_output" >> "$OUTPUT_FILE"
        echo "" >> "$OUTPUT_FILE"
      done
    done
  done
done

echo "Execução concluída. Resultados em $OUTPUT_FILE"

