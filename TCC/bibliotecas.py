import sqlite3
import subprocess
from time import sleep
import ast
import arrow
import os
# from TCC.Interface.PopupCompleto1 import Ui_Form



def horarios():
    atual = arrow.now()
    # data_criado = arrow.Arrow(2022, int(elemento[6][3:]), int(elemento[6][:2]))

    horario_atual = atual.format('HH:mm')
    dia_atual = atual.format('DD')
    # dia_atual = atual.format('DD/MM')
    # dia_semana = data_criado.shift(weeks=+1).format('DD/MM')
    # dia_mes = data_criado.shift(months=+1).format('DD/MM')
    #
    # dia_semana = f"['{dia_semana}']"
    # dia_atual = f"['{dia_atual}']"
    # dia_mes = f"['{dia_mes}']"

    return horario_atual, dia_atual



# MOSTRA E ATUALIZA TODOS OS ELEMENTOS DO TABLE DIARIA
def extrairMensagensDiaria(cursor):
    listaRetorno = []
    cursor.execute('DELETE FROM Diaria')
    cursor.execute(
        'SELECT * FROM Mensagens WHERE dia = "Diária" ORDER BY status DESC, horario ASC ')

    try:
        for elemento in cursor.fetchall():
            elemento = list(elemento)
            __agendar(elemento, 'Diária', cursor)
            listaRetorno.append(elemento)
        return listaRetorno
    except:
        return None




# MOSTRA E ATUALIZA TODOS OS ELEMENTOS DO TABLE SEMANAL
def extrairMensagensSemanal(cursor):
    listaRetorno = []
    cursor.execute('DELETE FROM Semanal')
    cursor.execute(
        'SELECT * FROM Mensagens WHERE dia = "Semanal" ORDER BY status DESC, horario ASC ')

    try:
        for elemento in cursor.fetchall():
            elemento = list(elemento)
            __agendar(elemento, 'Semanal', cursor)
            listaRetorno.append(elemento)
        return listaRetorno
    except:
        return None



# MOSTRA E ATUALIZA TODOS OS ELEMENTOS DO TABLE MENSAL
def extrairMensagensMensal(cursor):
    listaRetorno = []
    cursor.execute('DELETE FROM Mensal')
    cursor.execute(
        'SELECT * FROM Mensagens WHERE dia = "Mensal" ORDER BY status DESC, horario ASC ')

    try:
        for elemento in cursor.fetchall():
            elemento = list(elemento)
            __agendar(elemento, 'Mensal', cursor)
            listaRetorno.append(elemento)
        return listaRetorno
    except:
        return None



# MOSTRA E ATUALIZA TODOS OS ELEMENTOS DO TABLE ENVIO
def extrairMensagensEnvio(cursor):
    listaRetorno = []
    cursor.execute('DELETE FROM Envio')
    cursor.execute('SELECT * FROM Mensagens WHERE dia != "Diária" AND dia != "Semanal" AND dia != "Mensal" ORDER BY dia ASC, horario ASC ')

    try:
        for elemento in cursor.fetchall():
            elemento = list(elemento)
            __agendar(elemento, 'Envio', cursor)
            listaRetorno.append(elemento)
        return listaRetorno
    except:
        return None





def extrairMensagens(cursor):
    listaRetorno = []
    # cursor.execute('DELETE FROM Diaria')
    cursor.execute(
        'SELECT * FROM Mensagens ORDER BY status DESC, dia ASC, horario ASC ')


    for elemento in cursor.fetchall():
        list(elemento)
        # print(elemento)
        listaRetorno.append(elemento)

    return listaRetorno


#CURSOR INTERFACE.DB
def extrairContatos(cursor):
    listaContatos = {}
    cursor.execute(
        'SELECT * FROM Contatos ORDER BY nome ASC')

    for elemento in cursor.fetchall():
        listaContatos[elemento[0]] = elemento[1]

    return listaContatos


# PEGA OS VALORES DADOS PELA UI E TRANSFORMA DE ACORDO COM SEUS VALORES
# def converterParaEnvio(cursor):
#
#     cursor.execute('SELECT * FROM Mensagens ORDER BY dia ASC, horario ASC')
#
#     for elemento in cursor.fetchall():
#         elemento = list(elemento)
#
#         if 'Diária' in elemento[2]:
#             elemento[2] = elemento[2].replace('Diária', horario(elemento)[0])
#         elif 'Semanal' in elemento[2]:
#             elemento[2] = elemento[2].replace('Semanal', horario(elemento)[1])
#         elif 'Mensal' in elemento[2]:
#             elemento[2] = elemento[2].replace('Mensal', horario(elemento)[2])
#         # elemento[0] = ast.literal_eval(elemento[0])
#         # elemento[3] = ast.literal_eval(elemento[3])
#         # elemento[2] = ast.literal_eval(elemento[2])
#         __agendar(elemento, 'Envio')
#     extrairMensagensEnvio(cursor)




# SALVA TODOS AS INFORMAÇÕES PARA O ENVIO DA MENSAGEM
def __agendar(elemento, tipo, cursor):

    if tipo =='Diária':
            cursor.execute('INSERT INTO Diaria (mensagens, horario, dia, remetente, tipo_remetente, contem_midia, data_criada, hora_criada, nome_rotina,'
                           'executar_erro, status)'
            'VALUES (?,?,?,?,?,?,?,?,?,?,?)', (elemento[0], elemento[1], elemento[2], elemento[3], elemento[4], elemento[5],
                                     elemento[6], elemento[7], elemento[8], elemento[9], elemento[10]))
    elif tipo == 'Semanal':
            cursor.execute('INSERT INTO Semanal (mensagens, horario, dia, remetente, tipo_remetente, contem_midia, data_criada, hora_criada, nome_rotina,'
                           'executar_erro, status)'
            'VALUES (?,?,?,?,?,?,?,?,?,?,?)', (elemento[0], elemento[1], elemento[2], elemento[3], elemento[4], elemento[5],
                                     elemento[6], elemento[7], elemento[8], elemento[9], elemento[10]))

    elif tipo == 'Mensal':
            cursor.execute('INSERT INTO Mensal (mensagens, horario, dia, remetente, tipo_remetente, contem_midia, data_criada, hora_criada, nome_rotina,'
                           'executar_erro, status)'
            'VALUES (?,?,?,?,?,?,?,?,?,?,?)', (elemento[0], elemento[1], elemento[2], elemento[3], elemento[4], elemento[5],
                                     elemento[6], elemento[7], elemento[8], elemento[9], elemento[10]))

    else:
            cursor.execute('INSERT INTO Envio (mensagens, horario, dia, remetente, tipo_remetente, contem_midia, data_criada, hora_criada, nome_rotina,'
                           'executar_erro, status)'
            'VALUES (?,?,?,?,?,?,?,?,?,?,?)', (elemento[0], elemento[1], elemento[2], elemento[3], elemento[4], elemento[5],
                                             elemento[6], elemento[7], elemento[8], elemento[9], elemento[10]))










def atualizarDados(cursor):
    extrairMensagensEnvio(cursor)
    extrairMensagensSemanal(cursor)
    extrairMensagensMensal(cursor)
    extrairMensagensDiaria(cursor)




# def checkAlteracoes():
#     elemento = Ui_Form.
#     cursor.execute(
#         'INSERT INTO Mensagens (mensagens, horario, dia, remetente, tipo_remetente, contem_midia, data_criada, hora_criada)'
#         'VALUES (?,?,?,?,?,?,?,?)', (elemento[0], elemento[1], elemento[2], elemento[3], elemento[4], elemento[5],
#                                      elemento[6], elemento[7]))




def alterar_horario(horario, elemento):
    subprocess.run(f'schtasks /change /tn testeCMDbanana /st 15:00 /ru SYSTEM', shell=True, text=True)
    sleep(3)
    subprocess.run(f'', shell=True, text=True)



def __apagarRotina(tn):
    rotina = subprocess.run(
        f'schtasks /Delete /tn {tn} /F', shell=True,
        text=True)



def criarRotinaDiaria(cursor):
    try:
        info = extrairMensagensDiaria(cursor)[1]
    except:
        try:
            info = extrairMensagensDiaria(cursor)[0]
        except:
            __apagarRotina('OneTickMensagemDiaria')
            return None

    horario = info[1]

    cursor.execute('SELECT * FROM informacoes')

    pasta = cursor.fetchone()[0] + '\Send.exe'
    print(pasta)
    print(horario)

    __apagarRotina('OneTickMensagemDiaria')

    rotina = subprocess.run(
        f'schtasks /create /tn OneTickMensagemDiaria /tr {pasta} /SC DAILY /ST {horario}', shell=True,
        text=True)




def criarRotinaSemanal(cursor):
    try:
        info = extrairMensagensSemanal(cursor)[1]
    except:
        try:
            info = extrairMensagensSemanal(cursor)[0]
        except:
            __apagarRotina('OneTickMensagemSemanal')
            return None

    horario = info[1]

    cursor.execute('SELECT * FROM informacoes')

    pasta = cursor.fetchone()[0] + '\Send.exe'
    print(pasta)
    print(horario)

    __apagarRotina('OneTickMensagemSemanal')

    rotina = subprocess.run(
        f'schtasks /create /tn OneTickMensagemSemanal /tr {pasta} /SC WEEKLY /ST {horario}', shell=True,
        text=True)



def criarRotinaMensal(cursor):
    try:
        info = extrairMensagensMensal(cursor)[1]
    except:
        try:
            info = extrairMensagensMensal(cursor)[0]
        except:
            __apagarRotina('OneTickMensagemMensal')
            return None

    horario = info[1]

    cursor.execute('SELECT * FROM informacoes')

    pasta = cursor.fetchone()[0] + '\Send.exe'
    print(pasta)
    print(horario)

    __apagarRotina('OneTickMensagemMensal')


    print(horarios()[1])
    dataAtual = horarios()[1]

    rotina = subprocess.run(
        f'schtasks /create /tn OneTickMensagemMensal /tr {pasta} /SC MONTHLY /ST {horario} /D {dataAtual}', shell=True,
        text=True)



def criarRotinaNormal(cursor):
    try:
        info = extrairMensagensEnvio(cursor)[1]
    except:
        try:
            info = extrairMensagensEnvio(cursor)[0]
        except:
            __apagarRotina('OneTickMensagemNormal')
            return None

    horario = info[1]
    data = ast.literal_eval(info[2])[0]
    data = f'{data[3:]}/{data[:2]}'


    cursor.execute('SELECT * FROM informacoes')

    pasta = cursor.fetchone()[0] + '\Send.exe'
    print(pasta)
    print(horario, data)

    __apagarRotina('OneTickMensagemNormal')

    rotina = subprocess.run(
        f'schtasks /create /tn OneTickMensagemNormal /tr {pasta}  /SC ONCE /ST {horario} /SD {data}/2022 ', shell=True,
    text=True)


    # subprocess.run(f'schtasks /change /tn testeCMDbanana /st 14:00 ', shell=True, text=True, input='')


    # self.rotina = subprocess.run(
    #     f'schtasks /Delete /tn testeCMDbanana /F', shell=True,
    #     text=True)


        # self.rotina = subprocess.run('where python', shell=True, capture_output=True, text=True)



#ATUALIZA OS VALORES DA DIARIA AO CONCLUIR INTERFACE
def atualizarRotinaDiariaInterface(cursor):
    info = extrairMensagensDiaria(cursor)[0]

    horario = info[1]

    cursor.execute('SELECT * FROM informacoes')

    pasta = cursor.fetchone()[0] + '\Send.exe'
    print(pasta)
    print(horario)

    __apagarRotina('OneTickMensagemDiaria')

    rotina = subprocess.run(
        f'schtasks /create /tn OneTickMensagemDiaria /tr {pasta} /SC DAILY /ST {horario}', shell=True,
        text=True)


#ATUALIZA OS VALORES DA SEMANA AO CONCLUIR INTERFACE
def atualizarRotinaSemanalInterface(cursor):
    info = extrairMensagensSemanal(cursor)[0]

    horario = info[1]

    cursor.execute('SELECT * FROM informacoes')

    pasta = cursor.fetchone()[0] + '\Send.exe'
    print(pasta)
    print(horario)

    __apagarRotina('OneTickMensagemSemanal')

    rotina = subprocess.run(
        f'schtasks /create /tn OneTickMensagemSemanal /tr {pasta} /SC WEEKLY /ST {horario}', shell=True,
        text=True)


#ATUALIZA OS VALORES DA MENSAL AO CONCLUIR INTERFACE
def atualizarRotinaMensalInterface(cursor):
    info = extrairMensagensMensal(cursor)[0]
    horario = info[1]

    cursor.execute('SELECT * FROM informacoes')

    pasta = cursor.fetchone()[0] + '\Send.exe'
    print(pasta)
    print(horario)

    __apagarRotina('OneTickMensagemMensal')

    dataAtual = str(horarios()[1])

    rotina = subprocess.run(
        f'schtasks /create /tn OneTickMensagemMensal /tr {pasta} /SC MONTHLY /ST {horario} /D {dataAtual}', shell=True,
        text=True)


#ATUALIZA OS VALORES DA NORMAL AO CONCLUIR INTERFACE
def atualizarRotinaNormalInterface(cursor):
    info = extrairMensagensEnvio(cursor)[0]

    horario = info[1]
    data = ast.literal_eval(info[2])[0]
    data = f'{data[3:]}/{data[:2]}'


    cursor.execute('SELECT * FROM informacoes')

    pasta = cursor.fetchone()[0] + '\Send.exe'
    print(pasta)
    print(horario, data)

    __apagarRotina('OneTickMensagemNormal')

    rotina = subprocess.run(
        f'schtasks /create /tn OneTickMensagemNormal /tr {pasta}  /SC ONCE /ST {horario} /SD {data}/2022 ', shell=True,
    text=True)


    # subprocess.run(f'schtasks /change /tn testeCMDbanana /st 14:00 ', shell=True, text=True, input='')


    # self.rotina = subprocess.run(
    #     f'schtasks /Delete /tn testeCMDbanana /F', shell=True,
    #     text=True)


        # self.rotina = subprocess.run('where python', shell=True, capture_output=True, text=True)




def verificarDBNormal(cursor):
    if extrairMensagensEnvio(cursor):
        filaMensagens = extrairMensagensEnvio(cursor)[0]
        print(filaMensagens)
        cursor.execute('UPDATE Mensagens SET status = "ENVIADO" WHERE mensagens = ? AND data_criada = ? AND hora_criada = ?',
                       (filaMensagens[0],filaMensagens[6], filaMensagens[7]))

        cursor.execute('DELETE FROM Mensagens WHERE status = "ENVIADO" ')

        criarRotinaNormal(cursor)
        return filaMensagens
    else:
        __apagarRotina('OneTickMensagemNormal')







def verificarDBDiaria(cursor):
    filaMensagens = extrairMensagensDiaria(cursor)[0]
    cursor.execute('SELECT * FROM Diaria WHERE status = "PENDENTE"')
    if not cursor.fetchall():
        cursor.execute(
            'UPDATE Mensagens SET status = "PENDENTE" WHERE dia = "Diária" AND status = "ENVIADO"')
        atualizarDados(cursor)

    try:
        criarRotinaDiaria(cursor)
        cursor.execute(
            'UPDATE Mensagens SET status = "ENVIADO" WHERE mensagens = ? AND data_criada = ? AND hora_criada = ?',
            (filaMensagens[0], filaMensagens[6], filaMensagens[7]))
    except:
        __apagarRotina('OneTickMensagemDiaria')

    return filaMensagens





def verificarDBMensal(cursor):
    filaMensagens = extrairMensagensMensal(cursor)[0]
    cursor.execute('SELECT * FROM Mensal WHERE status = "PENDENTE"')
    if not cursor.fetchall():
        cursor.execute(
            'UPDATE Mensagens SET status = "PENDENTE" WHERE dia = "Mensal" AND status = "ENVIADO"')
        atualizarDados(cursor)

    print(filaMensagens)
    try:
        criarRotinaMensal(cursor)
        cursor.execute(
            'UPDATE Mensagens SET status = "ENVIADO" WHERE mensagens = ? AND data_criada = ? AND hora_criada = ?',
            (filaMensagens[0], filaMensagens[6], filaMensagens[7]))
    except:
        __apagarRotina('OneTickMensagemMensal')

    return filaMensagens




def verificarDBSemanal(cursor):
    filaMensagens = extrairMensagensSemanal(cursor)[0]
    cursor.execute('SELECT * FROM Semanal WHERE status = "PENDENTE"')
    if not cursor.fetchall():
        cursor.execute(
            'UPDATE Mensagens SET status = "PENDENTE" WHERE dia = "Semanal" AND status = "ENVIADO"')
        atualizarDados(cursor)

    print(filaMensagens)
    try:
        criarRotinaSemanal(cursor)
        cursor.execute(
            'UPDATE Mensagens SET status = "ENVIADO" WHERE mensagens = ? AND data_criada = ? AND hora_criada = ?',
            (filaMensagens[0], filaMensagens[6], filaMensagens[7]))
    except:

        __apagarRotina('OneTickMensagemSemanal')

    return filaMensagens



def apagarRotinasInterface(cursor):
    criarRotinaDiaria(cursor)
    criarRotinaMensal(cursor)
    criarRotinaNormal(cursor)
    criarRotinaSemanal(cursor)
    atualizarRotinasInterface(cursor)


def atualizarRotinasInterface(cursor):
    if extrairMensagensDiaria(cursor):
        atualizarRotinaDiariaInterface(cursor)

    if extrairMensagensMensal(cursor):
        atualizarRotinaMensalInterface(cursor)

    if extrairMensagensEnvio(cursor):
        atualizarRotinaNormalInterface(cursor)

    if extrairMensagensSemanal(cursor):
        atualizarRotinaSemanalInterface(cursor)



def resetarRotinas(cursor):
    if extrairMensagensDiaria(cursor):
        criarRotinaDiaria(cursor)

    if extrairMensagensMensal(cursor):
        criarRotinaMensal(cursor)

    if extrairMensagensEnvio(cursor):
        criarRotinaNormal(cursor)

    if extrairMensagensSemanal(cursor):
        criarRotinaSemanal(cursor)




def extrairLogin():
    conexao = sqlite3.connect(r'C:\Users\Usuario\PycharmProjects\Git\tccteam\TCC\localContent.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM Login')
    fetch = cursor.fetchone()
    login = fetch[0]
    ultimo_acesso = fetch[1]
    cor_status = fetch[2]

    conexao.commit()
    cursor.close()
    conexao.close()

    return login, ultimo_acesso, cor_status





def atualizarLogin(cursor, numero):
    if numero == 1:
        cursor.execute('UPDATE Login SET logado = ?, ultimo_acesso = ?, cor_status = ?', (numero, horario(), "rgb(85, 255, 127)"))
    else:
        cursor.execute('UPDATE Login SET logado = ?, ultimo_acesso = ?, cor_status = ?', (numero, horario(), "rgb(255, 0, 0)"))






 #------------------------------------------------------#











conexao = sqlite3.connect(r'C:\Users\Usuario\PycharmProjects\Git\tccteam\TCC\localContent.db')
cursor = conexao.cursor()
#

atualizarDados(cursor)
# apagarRotinasInterface(cursor)
# atualizarRotinasInterface(cursor)
# criarRotinaMensal(cursor)
# extrairContatos(cursor)
# atualizarRotinasInterface(cursor)
# print(extrairMensagens(cursor))
# atualizarLogin(cursor, 0)
# verificarDBSemanal(cursor)
# print(extrairLogin()[0])
# print(horario())
# print(extrairMensagens(cursor))
# print(extrairMensagensDiaria(cursor))
# verificarDBDiaria(cursor)
# verificarDBMensal(cursor)
# verificarDBDiaria(cursor)
# print(extrairMensagensDiaria(cursor))
# resetarRotinas(cursor)
# resetarRotinas(cursor)
# print(extrairMensagensDiaria(cursor))
#
conexao.commit()
cursor.close()
conexao.close()