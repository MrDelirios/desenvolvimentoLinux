import sqlite3

class Model:
    def __init__(self, nome_db='bancotp3.db'):
        self.nome_db = nome_db
        self.init_tables()

    def connect(self):
        return sqlite3.connect(self.nome_db)

    def execute_query(self, query, params=(), fetch=False):
        with self.connect () as connection:
            cursor = connection.cursor()
            cursor.execute(query, params)
            if fetch:
                return cursor.fetchall()
            connection.commit()

    def init_tables(self):
        try:
            # Criação da tabela cliente
            self.execute_query('''
                CREATE TABLE IF NOT EXISTS cliente (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nome TEXT NOT NULL, 
                    cpf TEXT NOT NULL,
                    endereco TEXT NOT NULL
                    )
            ''')
            # Criação da tabela produto
            self.execute_query('''
                CREATE TABLE IF NOT EXISTS produto (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL, 
                    valor REAL NOT NULL
                    )
            ''')
            # Criação da tabela venda
            self.execute_query('''
                CREATE TABLE IF NOT EXISTS venda (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    qtde INTEGER NOT NULL,
                    valor_total TEXT NOT NULL,
                    id_cliente INTEGER NOT NULL,
                    id_produto INTEGER NOT NULL,
                    FOREIGN KEY (id_cliente) REFERENCES cliente (id) ON DELETE CASCADE,
                    FOREIGN KEY (id_produto) REFERENCES produto (id) ON DELETE CASCADE
                    )
            ''')

            print("Tabelas criadas com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao criar tabelas: {e}")

    #CRUD

    # Create
    def create_cliente(self, params):
        self.execute_query('''
            INSERT INTO cliente (nome, cpf, endereco) VALUES (?, ?, ?)
        ''', params)

    def create_produto(self, params):
        self.execute_query('''
            INSERT INTO produto (nome, valor) VALUES (?, ?)
        ''', params)

    def create_venda(self, params):
        self.execute_query('''
            INSERT INTO venda (qtde, valor_total, id_cliente, id_produto) VALUES (?, ?, ?, ?)
        ''', params)
    
    # Read
    def read_cliente(self, nome):
        query = "SELECT * FROM cliente WHERE nome = ?"
        return self.execute_query(query, (nome,), fetch=True)
    
    def read_produto(self, nome):
        query = "SELECT * FROM produto WHERE nome = ?"
        return self.execute_query(query, (nome,), fetch=True)
    
    def read_venda(self, id_cliente, id_produto):
        query = "SELECT * FROM venda WHERE id_cliente = ? AND id_produto = ?"
        return self.execute_query(query, (id_cliente, id_produto), fetch=True)

    # def read_produto(self, id_produto=None, nome=None, valor=None):
    #     query = "SELECT * FROM produto WHERE 1=1"
    #     params = ()

    #     if id_produto is not None:
    #         query += " AND id = ?"
    #         params += (id_produto,)
    #     if nome is not None:
    #         query += " AND nome = ?"
    #         params += (nome,)
    #     if valor is not None:
    #         query += " AND valor = ?"
    #         params += (valor,)

    #     return self.execute_query(query, params, fetch=True)

    # def read_venda(self, id_venda = None, qtde = None, valor_total = None, id_cliente = None, id_produto = None):
    #     query = "SELECT * FROM venda WHERE 1=1"
    #     params = ()

    #     if id_venda is not None:
    #         query += " AND id = ?"
    #         params += (id_venda,)
    #     if qtde is not None:
    #         query += " AND qtde = ?"
    #         params += (qtde,)
    #     if valor_total is not None:
    #         query += " AND valor_total = ?"
    #         params += (valor_total,)
    #     if id_cliente is not None:
    #         query += " AND id_cliente = ?"
    #         params += (id_cliente,)
    #     if id_produto is not None:
    #         query += " AND id_produto = ?"
    #         params += (id_produto)

    #     return self.execute_query(query, params, fetch=True)

    # Update
    def update_cliente(self, params):
        self.execute_query('''
            UPDATE cliente
            SET nome = ?, cpf = ?, endereco = ?
            WHERE id = ?;
        ''', params)
    def update_produto(self, params):
        self.execute_query('''
            UPDATE produto
            SET nome = ?, valor = ?
            WHERE id = ?;
        ''', params)
    # def update_venda(self, params):
    #     self.execute_query('''
    #         UPDATE venda
    #         SET qtde = ?, valor_total = ?, id_cliente = ?, id_produto = ?
    #         WHERE id = ?
    #     ''', params)

    # Delete
    def delete_cliente(self, params):
        self.execute_query('''
            DELETE FROM cliente WHERE id = ?;
        ''', params)
    def delete_produto(self, params):
        self.execute_query('''
            DELETE FROM produto WHERE id = ?;
        ''', params)
    # def delete_venda(self, id_venda):
    #     self.execute_query('''
    #         DELETE FROM venda WHERE id = ?;
    #     ''', (id_venda,))

