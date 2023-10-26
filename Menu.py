import pymysql

conexao = pymysql.connect(host='localhost', user='root', password='', database='MeusDados', autocommit= True)

cursor = conexao.cursor()

#comando = 'CREATE DATABASE MeusDados'
#comando = ('CREATE TABLE Aluno(ID INT NOT NULL AUTO_INCREMENT, Nome VARCHAR(50), Idade INT, PRIMARY KEY(ID))')

#Criando funções
def cadastrar():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cursor.execute("INSERT INTO Aluno(Nome, Idade)" "VALUES (%s, %s)", (nome,idade))
    print("Registro cadastrado com sucesso :)")

def atualizar():
    id = int(input("Digite o ID do registro a ser atualizado: "))
    cursor.execute('SELECT ID FROM Aluno WHERE ID = %s', (id))
    resultado = cursor.fetchone()
    if resultado is not None:
        novo_nome = input("Digite seu nome: ")
        nova_idade = int(input("Digite sua idade: "))
        cursor.execute('UPDATE Aluno SET Nome = %s, Idade = %s WHERE ID = %s', (novo_nome, nova_idade, id))
    else:
        print("ID não encontrado :(")
def listar():
    cursor.execute('SELECT * FROM Aluno')
    registros = cursor.fetchall()
    for registro in registros:
        print(f"ID: {registro[0]}, Nome = {registro[1]}, Idade= {registro[2]}")
def deletar():
    id= int(input("Digite o ID que deseja deletar: "))
    cursor.execute('SELECT ID FROM Aluno WHERE ID = %s', (id))
    resultado = cursor.fetchone()
    if resultado is not None:
        cursor.execute('DELETE FROM Aluno WHERE ID = %S', (id))
    else:
        print("ID não encontrado :/")

while True:
    print("-- MENU --")
    print("[1] - CADASTRAR")
    print("[2] - ATUALIZAR")
    print("[3] - LISTAR")
    print("[4] - DELETAR")

    opcoes = input("Escolha uma ação: ")

    if opcoes == '1':
        cadastrar()
    elif opcoes == '2':
        atualizar()
    elif opcoes == '3':
        listar()
    elif opcoes == '4':
        deletar()
    else:
        print("Ação não disponível :/")
conexao.close()
