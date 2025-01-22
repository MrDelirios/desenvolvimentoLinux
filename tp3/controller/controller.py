from controller import Gtk
from views import MainView
from model import Model
import sqlite3

class Controller:
    def __init__(self):
        self.view = MainView(self)
        self.view.show_all()
        self.model = Model()

    def navigate(self, page_name):
        self.view.switch_page(page_name)

    def run(self):
        Gtk.main()

    def quit_app(self):
        Gtk.main_quit()

    def create_cliente(self, nome, cpf, endereco):
        try:
            self.model.create_cliente((nome, cpf, endereco))
            return "CLIENTE INSERIDO COM SUCESSO!"
        except sqlite3.Error as e:
            return e
        
    def create_produto(self, nome, valor):
        try:
            self.model.create_produto((nome, float(valor)))
            return "PRODUTO INSERIDO COM SUCESSO!"
        except sqlite3.Error as e:
            return e
        
    def create_venda(self, qtde, valor_total, nome_cliente, nome_produto):
        try:
            try:
                id_cliente = int(self.read_cliente(nome_cliente)[0][0])
                id_produto = int(self.read_produto(nome_produto)[0][0])
            except IndexError as e:
                return "Cliente ou Produto Inexistente"
            self.model.create_venda((qtde, valor_total, id_cliente, id_produto))
            return "VENDA INSERIDA COM SUCESSO!"
        except sqlite3.Error as e:
            return e
    
    def read_cliente(self, nome=None):
        try:
            return self.model.read_cliente(nome)
        except sqlite3.Error as e:
            return e
        
    def read_produto(self, nome=None):
        try:
            return self.model.read_produto(nome)
        except sqlite3.Error as e:
            return e
        
    def read_venda(self, nome_cliente, nome_produto):
        try:
            try:
                id_cliente = int(self.read_cliente(nome_cliente)[0][0])
                id_produto = int(self.read_produto(nome_produto)[0][0])
            except IndexError as e:
                return "Cliente ou Produto Inexistente"
            return self.model.read_venda(id_cliente, id_produto)
        except sqlite3.Error as e:
            return e
        
    def update_cliente(self, nome, cpf, endereco):
        try:
            try:
                id_cliente = int(self.read_cliente(nome)[0][0])
            except IndexError as e:
                return "Cliente Inexistente"
            self.model.update_cliente((nome, cpf, endereco, id_cliente))
            return "Cliente Atualizado com Sucesso"
        except sqlite3.Error as e:
            return e
    
    def update_produto(self, nome, valor):
        try:
            try:
                id_produto = int(self.read_produto(nome)[0][0])
            except IndexError as e:
                return "Produto Inexistente"
            self.model.update_produto((nome, valor, id_produto))
            return "Produto Atualizado com Sucesso"
        except sqlite3.Error as e:
            return e
        
    # def update_venda(self, qtde, valor_total, id_cliente, id_produto, id_venda):
    #     try:
    #         return self.model.update_venda((qtde, valor_total, id_cliente, id_produto, id_venda))
    #     except sqlite3.Error as e:
    #         return e

    def delete_cliente(self, nome):
        try:
            try:
                id_cliente = int(self.read_cliente(nome)[0][0])
            except IndexError as e:
                return "Cliente Inexistente"
            self.model.delete_cliente((id_cliente,))
            return "Registro Apagado com Sucesso"
        except sqlite3.Error as e:
            return e
        
    def delete_produto(self, nome):
        try:
            try:
                id_produto = int(self.read_produto(nome)[0][0])
            except IndexError as e:
                return "Produto Inexistente"
            self.model.delete_produto((id_produto,))
            return "Registro Apagado com Sucesso"
        except sqlite3.Error as e:
            return e
    