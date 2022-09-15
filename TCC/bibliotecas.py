import sqlite3

def salvar_db(msg, numero_contato, vezes, cursor):
    cursor.execute('INSERT INTO mensagem(texto, numero_contato, vezes_texto)'
                   'VALUES(?, ?, ?)', (msg, numero_contato, vezes))




def extrair_dados():
    pass


conexao = sqlite3.connect('localContent.db')
cursor = conexao.cursor()
salvar_db('fala', 5547988314131, 1, cursor)


conexao.commit()
cursor.close()
conexao.close()