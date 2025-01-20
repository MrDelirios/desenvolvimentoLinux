import random

class SerVivo:
    def __init__(self, nome, idade_maxima, energia_maxima):
        self.nome = nome
        self.idade = 0
        self.energia = energia_maxima
        self.idade_maxima = idade_maxima
        self.energia_maxima = energia_maxima

    def nascer(self):
        self.idade = 0
        self.energia = self.energia_maxima
        print(f"{self.nome} nasceu!")

    def morrer(self):
        print(f"{self.nome} morreu!")
        
    def envelhecer(self):
        self.idade += 1
        if self.idade >= self.idade_maxima:
            self.morrer()
    
    def alimentar(self, energia):
        self.energia += energia
        if self.energia > self.energia_maxima:
            self.energia = self.energia_maxima
    
    def gastar_energia(self, energia):
        self.energia -= energia
        if self.energia <= 0:
            self.morrer()

    def status(self):
        return f"{self.nome} | Idade: {self.idade}, Energia: {self.energia}"

class Animal(SerVivo):
    def __init__(self, nome, idade_maxima, energia_maxima):
        super().__init__(nome, idade_maxima, energia_maxima)
    
    def movimentar(self):
        # Vamos apenas reduzir energia para o movimento
        energia_gasta = random.randint(1, 3)
        self.gastar_energia(energia_gasta)
        print(f"{self.nome} se moveu e gastou {energia_gasta} de energia.")

class Vegetal(SerVivo):
    def __init__(self, nome, idade_maxima, energia_maxima):
        super().__init__(nome, idade_maxima, energia_maxima)

    def crescer(self):
        # Vegetais não gastam energia com movimento, mas podem crescer
        print(f"{self.nome} cresceu.")

class Carnivoro(Animal):
    def __init__(self, nome, idade_maxima, energia_maxima):
        super().__init__(nome, idade_maxima, energia_maxima)
    
    def alimentar(self, presas):
        if presas:
            presa = random.choice(presas)
            energia_ganha = min(presa.energia, 10)  # Ganha até 10 de energia
            self.alimentar(energia_ganha)
            print(f"{self.nome} comeu {presa.nome} e ganhou {energia_ganha} de energia.")
        else:
            print(f"{self.nome} não encontrou presas.")

class Herbivoro(Animal):
    def __init__(self, nome, idade_maxima, energia_maxima):
        super().__init__(nome, idade_maxima, energia_maxima)

    def alimentar(self, vegetais):
        if vegetais:
            vegetal = random.choice(vegetais)
            energia_ganha = min(vegetal.energia, 5)  # Ganha até 5 de energia
            self.alimentar(energia_ganha)
            print(f"{self.nome} comeu {vegetal.nome} e ganhou {energia_ganha} de energia.")
        else:
            print(f"{self.nome} não encontrou vegetais.")

class Ecossistema:
    def __init__(self):
        self.seres_vivos = []
        self.turno = 0

    def adicionar_ser_vivo(self, ser_vivo):
        self.seres_vivos.append(ser_vivo)

    def simular_turno(self):
        # A cada turno, o tempo avança e todos os seres vivos envelhecem ou realizam ações
        self.turno += 1
        print(f"\n--- Turno {self.turno} ---")
        
        for ser in self.seres_vivos:
            ser.envelhecer()  # Envelhece cada ser vivo
            
            # Ações específicas por turno (exemplo simplificado)
            if isinstance(ser, Animal):
                ser.movimentar()
            if isinstance(ser, Vegetal):
                ser.crescer()

        print(f"Fim do turno {self.turno}")

# Criando seres vivos
leo = Carnivoro("Leão", idade_maxima=10, energia_maxima=50)
zebra = Herbivoro("Zebra", idade_maxima=8, energia_maxima=40)
grama = Vegetal("Grama", idade_maxima=5, energia_maxima=30)

# Criando o ecossistema e adicionando seres vivos
ecossistema = Ecossistema()
ecossistema.adicionar_ser_vivo(leo)
ecossistema.adicionar_ser_vivo(zebra)
ecossistema.adicionar_ser_vivo(grama)

# Simulando alguns turnos
for _ in range(5):
    ecossistema.simular_turno()
