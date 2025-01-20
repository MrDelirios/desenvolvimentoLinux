#!/bin/bash

# Inicialização do ncurses
initialize_ncurses() {
  tput civis          # Oculta o cursor
  stty -echo          # Desativa a exibição das teclas pressionadas
  clear               # Limpa a tela
  tput smcup          # Salva o estado do terminal
}

# Finaliza o ncurses e restaura o terminal
finalize_ncurses() {
  tput rmcup          # Restaura o estado do terminal
  stty echo           # Restaura a exibição das teclas
  tput cnorm          # Mostra o cursor
  clear               # Limpa a tela
}

# Função para desenhar bordas
draw_border() {
  tput setaf 7
  for ((i = 0; i <= 20; i++)); do
    tput cup $i 0
    echo "║"
    tput cup $i 40
    echo "║"
  done
  tput cup 0 0
  echo "╔═══════════════════════════════════════╗"
  tput cup 20 0
  echo "╚═══════════════════════════════════════╝"
}

# Função para desenhar HUD
draw_hud() {
  tput setaf 3
  tput cup 0 42
  echo "Score: $score_left - $score_right"
  tput sgr0
}

# Função para desenhar a raquete
draw_paddle() {
  local y=$1 x=$2
  tput setaf 2
  for ((i = 0; i < 3; i++)); do
    tput cup $((y + i)) $x
    echo "|"
  done
  tput sgr0
}

# Função para desenhar a bola
draw_ball() {
  tput setaf 7
  tput cup $ball_y $ball_x
  echo "o"
  tput sgr0
}

# Função para limpar uma posição da tela
clear_position() {
  local y=$1 x=$2
  tput cup $y $x
  echo " "
}

# Variáveis do jogo
top_paddle_y=8
bottom_paddle_y=8
ball_x=20
ball_y=10
ball_dx=1
ball_dy=1
score_left=0
score_right=0
sleep_time=0.05

# Função para movimentar a máquina
move_machine() {
  if ((ball_y > bottom_paddle_y + 2)); then
    bottom_paddle_y=$((bottom_paddle_y + 1))
  elif ((ball_y < bottom_paddle_y + 2)); then
    bottom_paddle_y=$((bottom_paddle_y - 1))
  fi

  # Limita a movimentação dentro do campo
  if ((bottom_paddle_y < 1)); then
    bottom_paddle_y=1
  elif ((bottom_paddle_y > 15)); then
    bottom_paddle_y=15
  fi
}

# Função para verificar colisões
check_collision() {
  # Colisão com bordas horizontais
  if ((ball_y == 1 || ball_y == 19)); then
    ball_dy=$((ball_dy * -1))
  fi

  # Colisão com a raquete esquerda
  if ((ball_x == 2 && ball_y >= top_paddle_y && ball_y < top_paddle_y + 3)); then
    ball_dx=$((ball_dx * -1))
  fi

  # Colisão com a raquete direita
  if ((ball_x == 38 && ball_y >= bottom_paddle_y && ball_y < bottom_paddle_y + 3)); then
    ball_dx=$((ball_dx * -1))
  fi

  # Pontuação
  if ((ball_x <= 1)); then
    score_right=$((score_right + 1))
    reset_ball
  elif ((ball_x >= 39)); then
    score_left=$((score_left + 1))
    reset_ball
  fi
}

# Função para resetar a posição da bola
reset_ball() {
  ball_x=20
  ball_y=10
  ball_dx=$((RANDOM % 2 == 0 ? 1 : -1))
  ball_dy=$((RANDOM % 2 == 0 ? 1 : -1))
}

# Loop principal do jogo
game_loop() {
  while true; do
    # Limpar a tela para evitar sobreposição
    clear

    # Desenhar o campo
    draw_border
    draw_hud
    draw_paddle $top_paddle_y 1
    draw_paddle $bottom_paddle_y 39
    draw_ball

    # Captura de teclas para movimentar o jogador
    read -t $sleep_time -n 1 key
    case $key in
      w|W) # Movimentar para cima
        if ((top_paddle_y > 1)); then
          clear_position $((top_paddle_y + 4)) 1
          top_paddle_y=$((top_paddle_y - 1))
        fi
        ;;
      s|S) # Movimentar para baixo
        if ((top_paddle_y < 15)); then
          clear_position $top_paddle_y 1
          top_paddle_y=$((top_paddle_y + 1))
        fi
        ;;
      q|Q) # Sair do jogo
        break
        ;;
    esac

    # Atualizar a posição da bola
    clear_position $ball_y $ball_x
    ball_x=$((ball_x + ball_dx))
    ball_y=$((ball_y + ball_dy))

    # Verificar colisões
    check_collision

    # Movimentar a máquina
    move_machine
  done
}

# Inicializar e rodar o jogo
initialize_ncurses
trap finalize_ncurses EXIT
game_loop
