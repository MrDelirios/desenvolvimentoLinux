from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QStandardItem, QStandardItemModel

from crudui import Ui_CRUD
import psycopg2

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CRUD()
        self.ui.setupUi(self)

        # Conectar botões às funções
        self.ui.btnCriar.clicked.connect(self.criar_usuario)
        self.ui.btnListar.clicked.connect(self.listar_usuarios)
        self.ui.btnAtualizar.clicked.connect(self.atualizar_usuario)
        self.ui.btnExcluir.clicked.connect(self.excluir_usuario)
        self.ui.pushButton.clicked.connect(lambda: self.mudar_pagina(0))
        self.ui.pushButton_2.clicked.connect(lambda: self.mudar_pagina(1))

        self.ui.pushButton_4.clicked.connect(lambda: self.mudar_pagina1(0))
        self.ui.pushButton_3.clicked.connect(lambda: self.mudar_pagina1(1))

        # Conectar botões de produto
        self.ui.btnCriarProduto.clicked.connect(self.criar_produto)
        self.ui.btnListarProduto.clicked.connect(self.listar_produtos)
        self.ui.btnAtualizarProduto.clicked.connect(self.atualizar_produto)
        self.ui.btnExcluirProduto.clicked.connect(self.excluir_produto)
    
    def mudar_pagina(self, i):
        self.ui.stackedWidget.setCurrentIndex(i)

    def mudar_pagina1(self, i):
        self.ui.stackedWidget_2.setCurrentIndex(i)

    def conectar(self):
        return psycopg2.connect(
            dbname="meu_crud",
            user="postgres",
            password="75890",
            host="localhost"
        )

    def criar_usuario(self):
        nome = self.ui.inputNome.text()
        email = self.ui.inputEmail.text()
        
        if not nome or not email:
            QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios!")
            return

        try:
            conn = self.conectar()
            cur = conn.cursor()
            cur.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", (nome, email))
            conn.commit()
            QMessageBox.information(self, "Sucesso", "Usuário criado com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao criar usuário: {e}")
        finally:
            cur.close()
            conn.close()

    from PySide6.QtGui import QStandardItem, QStandardItemModel

    def listar_usuarios(self):
        try:
            # Conectar ao banco de dados
            conn = self.conectar()
            cur = conn.cursor()

            # Executar consulta SQL
            cur.execute("SELECT * FROM usuarios")
            usuarios = cur.fetchall()

            # Criar o modelo para o QListView
            model = QStandardItemModel()

            # Adicionar os dados ao modelo (uma linha para cada usuário)
            for u in usuarios:
                item = QStandardItem(f"ID: {u[0]} - Nome: {u[1]} - Email: {u[2]}")
                model.appendRow(item)

            # Configurar o modelo para o QListView
            self.ui.listaC.setModel(model)

            QMessageBox.information(self, "Sucesso", "Usuários listados com sucesso!")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao listar usuários: {e}")
        finally:
            # Fechar cursor e conexão
            cur.close()
            conn.close()


    def atualizar_usuario(self):
        id_usuario = self.ui.inputId.text()
        nome = self.ui.inputNome_2.text()
        email = self.ui.inputEmail_2.text()
        if not id_usuario or not nome or not email:
            QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios!")
            return

        try:
            conn = self.conectar()
            cur = conn.cursor()
            cur.execute(
                "UPDATE usuarios SET nome = %s, email = %s WHERE id = %s",
                (nome, email, int(id_usuario))
            )
            conn.commit()
            QMessageBox.information(self, "Sucesso", "Usuário atualizado com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao atualizar usuário: {e}")
        finally:
            cur.close()
            conn.close()

    def excluir_usuario(self):
        # Obter o índice do item selecionado
        selecionado = self.ui.listaC.selectedIndexes()
        
        # Verificar se algo foi selecionado
        if not selecionado:
            QMessageBox.warning(self, "Erro", "Selecione um usuário para excluir!")
            return

        # Obter o índice da primeira coluna do item selecionado
        indice = selecionado[0]
        
        # Extrair o texto do item selecionado
        item_texto = indice.data()

        # Supondo que o formato seja "ID: {id} - Nome: {nome} - Email: {email}"
        # Vamos extrair o ID a partir do texto
        try:
            id_usuario = int(item_texto.split(" - ")[0].replace("ID: ", ""))
        except ValueError:
            QMessageBox.warning(self, "Erro", "Não foi possível extrair o ID do usuário!")
            return

        if not id_usuario:
            QMessageBox.warning(self, "Erro", "ID do usuário é obrigatório!")
            return

        try:        
            # Conectar ao banco de dados
            conn = self.conectar()
            cur = conn.cursor()

            # Excluir usuário do banco de dados
            cur.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
            conn.commit()

            QMessageBox.information(self, "Sucesso", "Usuário excluído com sucesso!")

            # Atualizar a lista após exclusão
            self.listar_usuarios()  # Pode chamar a função que você já tem para listar novamente

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao excluir usuário: {e}")
        finally:
            cur.close()
            conn.close()
    
        # Funções para produtos (implementadas agora)
    def criar_produto(self):
        descricao = self.ui.inputDescricaoProduto.text()
        preco = self.ui.inputPrecoProduto.text()
        if not descricao or not preco:
            QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios!")
            return
        try:
            conn = self.conectar()
            cur = conn.cursor()
            cur.execute("INSERT INTO produtos (descricao, preco) VALUES (%s, %s)", (descricao, preco))
            conn.commit()
            QMessageBox.information(self, "Sucesso", "Produto criado com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao criar produto: {e}")
        finally:
            cur.close()
            conn.close()

    def listar_produtos(self):
        try:
            conn = self.conectar()
            cur = conn.cursor()
            cur.execute("SELECT * FROM produtos")
            produtos = cur.fetchall()
            model = QStandardItemModel()
            for p in produtos:
                item = QStandardItem(f"ID: {p[0]} - Descrição: {p[1]} - Preço: {p[2]}")
                model.appendRow(item)
            self.ui.listaProduto.setModel(model)
            QMessageBox.information(self, "Sucesso", "Produtos listados com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao listar produtos: {e}")
        finally:
            cur.close()
            conn.close()

    def atualizar_produto(self):
        id_produto = self.ui.inputIdProduto.text()
        descricao = self.ui.inputDescricaoProduto_2.text()
        preco = self.ui.inputPrecoProduto_2.text()
        if not id_produto or not descricao or not preco:
            QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios!")
            return
        try:
            conn = self.conectar()
            cur = conn.cursor()
            cur.execute("UPDATE produtos SET descricao = %s, preco = %s WHERE id = %s", (descricao, preco, int(id_produto)))
            conn.commit()
            QMessageBox.information(self, "Sucesso", "Produto atualizado com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao atualizar produto: {e}")
        finally:
            cur.close()
            conn.close()

    def excluir_produto(self):
        selecionado = self.ui.listaProduto.selectedIndexes()
        if not selecionado:
            QMessageBox.warning(self, "Erro", "Selecione um produto para excluir!")
            return
        indice = selecionado[0]
        item_texto = indice.data()
        try:
            id_produto = int(item_texto.split(" - ")[0].replace("ID: ", ""))
        except ValueError:
            QMessageBox.warning(self, "Erro", "Não foi possível extrair o ID do produto!")
            return
        if not id_produto:
            QMessageBox.warning(self, "Erro", "ID do produto é obrigatório!")
            return
        try:
            conn = self.conectar()
            cur = conn.cursor()
            cur.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
            conn.commit()
            QMessageBox.information(self, "Sucesso", "Produto excluído com sucesso!")
            self.listar_produtos()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao excluir produto: {e}")
        finally:
            cur.close()
            conn.close()



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
