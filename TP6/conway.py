import sys
import random
import time
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGraphicsScene, QGraphicsView, QGraphicsRectItem

class ConwayGameOfLife(QWidget):
    def __init__(self, grid_size=50, cell_size=10):
        super().__init__()
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.setWindowTitle("Jogo da Vida de Conway")

        # Layout
        layout = QVBoxLayout()
        
        # Botões de controle
        self.start_button = QPushButton("Iniciar")
        self.start_button.clicked.connect(self.toggle_game)
        layout.addWidget(self.start_button)
        
        self.reset_button = QPushButton("Resetar")
        self.reset_button.clicked.connect(self.reset_grid)
        layout.addWidget(self.reset_button)

        # Preparar a cena gráfica
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        layout.addWidget(self.view)
        
        # Inicializar a grid do jogo
        self.grid = [[random.choice([0, 1]) for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.cells = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        
        # Adicionar os itens gráficos (células) à cena
        self.init_grid()
        
        # Timer para a execução do jogo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_grid)
        
        self.setLayout(layout)
        self.show()

    def init_grid(self):
        """Adiciona as células à cena gráfica."""
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                rect = QGraphicsRectItem(j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size)
                rect.setBrush(Qt.black if self.grid[i][j] == 1 else Qt.white)
                rect.setPen(Qt.NoPen)
                self.scene.addItem(rect)
                self.cells[i][j] = rect

    def toggle_game(self):
        """Alterna entre iniciar e pausar o jogo."""
        if self.timer.isActive():
            self.timer.stop()
            self.start_button.setText("Iniciar")
        else:
            self.timer.start(200)  # Atualiza a cada 200 ms
            self.start_button.setText("Pausar")

    def reset_grid(self):
        """Reseta o estado do tabuleiro para uma configuração aleatória."""
        self.grid = [[random.choice([0, 1]) for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.update_graphic()

    def update_grid(self):
        """Atualiza o estado do tabuleiro de acordo com as regras do jogo."""
        new_grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                # Contar vizinhos vivos
                live_neighbors = self.count_live_neighbors(i, j)

                if self.grid[i][j] == 1:  # Célula viva
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[i][j] = 0  # Morre por subpopulação ou superpopulação
                    else:
                        new_grid[i][j] = 1  # Sobrevive
                elif self.grid[i][j] == 0 and live_neighbors == 3:
                    new_grid[i][j] = 1  # Revive por reprodução

        self.grid = new_grid
        self.update_graphic()

    def count_live_neighbors(self, i, j):
        """Conta o número de vizinhos vivos de uma célula."""
        live_neighbors = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                ni, nj = i + x, j + y
                if 0 <= ni < self.grid_size and 0 <= nj < self.grid_size:
                    live_neighbors += self.grid[ni][nj]
        return live_neighbors

    def update_graphic(self):
        """Atualiza a representação gráfica das células."""
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.cells[i][j].setBrush(Qt.black if self.grid[i][j] == 1 else Qt.white)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConwayGameOfLife()
    sys.exit(app.exec())
