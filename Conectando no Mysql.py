import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="turmaa",
)
meucursor= banco.cursor()
pesquisa = 'select * from alunos;'
meucursor.execute(pesquisa)
resultado = meucursor.fetchall()
for x in resultado:
    print(x)

nome1=input("Informe o nome do aluno:")
telefone1=int(input("Digite número do aluno:"))
sql = "INSERT INTO alunos (nome, telefone) VALUES (%s,%s)"
data = (nome1,telefone1)
banco.commit()


meucursor.close()
banco.close()