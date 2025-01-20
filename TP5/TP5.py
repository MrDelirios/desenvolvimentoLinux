import threading
import random
import time
from collections import deque

class Estoque:
    def __init__(self, capacidade=10):
        self.capacidade = capacidade
        self.fila = deque()
        self.lock = threading.Lock()
    
    def armazenar(self, produtor_id, item_id):
        with self.lock:
            if len(self.fila) < self.capacidade:
                self.fila.append((produtor_id, item_id))
                print(f"Produtor {produtor_id} armazena item {item_id}.")
            else:
                print(f"Estoque cheio, aguardando espaço...")
    
    def consumir(self, consumidor_id):
        with self.lock:
            if self.fila:
                item = self.fila.popleft()
                print(f"Consumidor {consumidor_id} recebe item {item[1]}.")
                return item
            else:
                print(f"Estoque vazio, aguardando item...")
                return None

class Produtor(threading.Thread):
    def __init__(self, id_produtor, estoque):
        super().__init__()
        self.id_produtor = id_produtor
        self.estoque = estoque
        self.item_id = 1
    
    def run(self):
        while True:
            time.sleep(random.randint(1, 5))  # Atraso aleatório entre 1 e 5 segundos
            self.estoque.armazenar(self.id_produtor, self.item_id)
            self.item_id += 1

class Consumidor(threading.Thread):
    def __init__(self, id_consumidor, estoque):
        super().__init__()
        self.id_consumidor = id_consumidor
        self.estoque = estoque
    
    def run(self):
        while True:
            time.sleep(random.randint(1, 3))  # Atraso aleatório entre 1 e 3 segundos
            item = None
            while item is None:  # Repetir até conseguir consumir um item
                item = self.estoque.consumir(self.id_consumidor)
                if item is None:
                    time.sleep(1)  # Espera antes de tentar novamente

def main():
    estoque = Estoque()
    
    produtores = [Produtor(i, estoque) for i in range(1, 4)]
    consumidores = [Consumidor(i, estoque) for i in range(1, 4)]
    
    for p in produtores:
        p.start()
    
    for c in consumidores:
        c.start()

if __name__ == "__main__":
    main()
