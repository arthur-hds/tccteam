import sqlite3

def salvar_db(msg, numero_contato, vezes, horario, cursor):
    cursor.execute('INSERT INTO mensagem(texto, numero_contato, vezes_texto, horario)'
                   'VALUES(?, ?, ?, ?)', (msg, numero_contato, vezes, horario))


def extrair_dados():

    cursor.execute('SELECT * FROM mensagem ORDER BY horario DESC')
    for elemento in cursor.fetchall():
        print(f'{elemento[0]} - {elemento[1]} - {elemento[2]} - {elemento[3]} - {elemento[4]}')
    pass


conexao = sqlite3.connect('localContent.db')
cursor = conexao.cursor()
# salvar_db('fala', 5547988314131, 1, '11:30',cursor)
extrair_dados()

conexao.commit()
cursor.close()
conexao.close()