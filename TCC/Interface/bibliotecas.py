import sqlite3
import subprocess
from time import sleep
import ast
import arrow
import os
# from TCC.Interface.PopupCompleto1 import Ui_Form


Interface = f'{os.getcwd()}'
localContent = f'{Interface[:len(Interface)-10]}\\localContent.db'
InterfaceDB = f'{Interface}\\Interface\\InterfaceDB.db'


def horarios():
    atual = arrow.now()
    # data_criado = arrow.Arrow(2022, int(elemento[6][3:]), int(elemento[6][:2]))

    horario_atual = atual.format('HH:mm')
    dia_atual = atual.format('DD')
    mes_atual = atual.format('MM')

    # dia_atual = atual.format('DD/MM')
    # dia_semana = data_criado.shift(weeks=+1).format('DD/MM')
    # dia_mes = data_criado.shift(months=+1).format('DD/MM')
    #
    # dia_semana = f"['{dia_semana}']"
    # dia_atual = f"['{dia_atual}']"
    # dia_mes = f"['{dia_mes}']"

    return horario_atual, dia_atual, mes_atual



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
    cursor.execute('SELECT * FROM Mensagens WHERE dia != "Diária" AND dia != "Semanal" AND dia != "Mensal" AND dia != "Personalizada" ORDER BY dia ASC, horario ASC ')

    try:
        for elemento in cursor.fetchall():
            elemento = list(elemento)

            __agendar(elemento, 'Envio', cursor)
            listaRetorno.append(elemento)
        return listaRetorno
    except:
        return None



def extrairMensagensPersonalizada(cursor):
    listaRetorno = []
    cursor.execute('DELETE FROM Personalizada')
    cursor.execute(
        'SELECT * FROM Mensagens WHERE dia = "Personalizada" ORDER BY status DESC, horario ASC ')

    try:
        for elemento in cursor.fetchall():
            elemento = list(elemento)
            __agendar(elemento, 'Personalizada', cursor)
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
        listaRetorno.append(elemento)

    return listaRetorno



def extrairHorarios(cursor):
    listaRetorno = []
    # cursor.execute('DELETE FROM Diaria')
    cursor.execute(
        'SELECT horario FROM Mensagens ORDER BY status DESC, dia ASC, horario ASC ')


    for elemento in cursor.fetchall():
        list(elemento)
        # print(elemento)
        listaRetorno.append(elemento[0])

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

    elif tipo == 'Envio':
            cursor.execute('INSERT INTO Envio (mensagens, horario, dia, remetente, tipo_remetente, contem_midia, data_criada, hora_criada, nome_rotina,'
                           'executar_erro, status)'
            'VALUES (?,?,?,?,?,?,?,?,?,?,?)', (elemento[0], elemento[1], elemento[2], elemento[3], elemento[4], elemento[5],
                                             elemento[6], elemento[7], elemento[8], elemento[9], elemento[10]))
    else:
            cursor.execute('INSERT INTO Personalizada (mensagens, horario, dia, remetente, tipo_remetente, contem_midia, data_criada, hora_criada, nome_rotina,'
                           'executar_erro, status)'
            'VALUES (?,?,?,?,?,?,?,?,?,?,?)', (elemento[0], elemento[1], elemento[9], elemento[3], elemento[4], elemento[5],
                                             elemento[6], elemento[7], elemento[8], "False", elemento[10]))




def mensagensPassadas(cursor):

    while True:
        info = extrairMensagensEnvio(cursor)[0]
        mes = info[2][2:4]
        dia = info[2][5:7]

        dia_int = int(f'{mes}{dia}')
        dia_atual_int = int(f'{horarios()[2]}{horarios()[1]}')

        if dia_atual_int >= dia_int:
            hora = info[1][:2]
            minuto = info[1][3:]
            horario_int = int(int(f'{hora}{minuto}'))
            horario_atual_int = int(horarios()[0][:2] + horarios()[0][3:])
            if horario_atual_int > horario_int:
                if info[9] == 'True':
                    cursor.execute(
                        'INSERT INTO Mensagens (mensagens, horario, dia, remetente, tipo_remetente,'
                        'contem_midia, data_criada, hora_criada, nome_rotina,'
                        'executar_erro, status)'
                        'VALUES (?,?,?,?,?,?,?,?,?,?,?)',
                        (info[0], horarios()[0], f"['{horarios()[2]}/{int(horarios()[1]) + 1}']", info[3], info[4],
                         info[5],
                         info[6], info[7], info[8], info[9], info[10]))

                verificarDBNormal(cursor)
            else:
                break
        else:
            break




def returnPath():
    return localContent





def atualizarDados(cursor):
    extrairMensagensEnvio(cursor)
    extrairMensagensSemanal(cursor)
    extrairMensagensMensal(cursor)
    extrairMensagensDiaria(cursor)
    extrairMensagensPersonalizada(cursor)
    try:
        mensagensPassadas(cursor)
    except:
        pass



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

    pasta = cursor.fetchone()[0] + '\SendDaily.exe'


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

    pasta = cursor.fetchone()[0] + '\SendSemanal.exe'


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

    pasta = cursor.fetchone()[0] + '\SendMensal.exe'



    __apagarRotina('OneTickMensagemMensal')


    dataAtual = horarios()[1]

    rotina = subprocess.run(
        f'schtasks /create /tn OneTickMensagemMensal /tr {pasta} /SC MONTHLY /ST {horario} /D {dataAtual}', shell=True,
        text=True)



def criarRotinaNormal(cursor):
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



    __apagarRotina('OneTickMensagemNormal')

    rotina = subprocess.run(
        f'schtasks /create /tn OneTickMensagemNormal /tr {pasta}  /SC ONCE /ST {horario} /SD {data}/2022 ', shell=True,
    text=True)





def criarRotinaPersonalizada(cursor):
    try:
        info = extrairMensagensPersonalizada(cursor)[0]
    except:
        __apagarRotina('OneTickMensagemPersonalizada')
        return None

    horario = info[1]


    cursor.execute('SELECT * FROM informacoes')

    pasta = cursor.fetchone()[0] + '\SendPersonalizada.exe'


    __apagarRotina('OneTickMensagemPersonalizada')


    traducaoDias = {
        "Domingo" : "SUN",
        "Sábado" : "SAT",
        "Sexta-feira" : "FRI",
        "Quinta-feira" : "THU",
        "Quarta-feira" : "WED",
        "Terça-feira" : "TUE",
        "Segunda-feira" : "MON",
    }


    datas = info[9]

    datas = ast.literal_eval(datas)
    diasFormatados = ''
    count = 0



    for data in datas:
        count += 1
        if count == 1:
            diasFormatados += traducaoDias[data]
        elif count <= len(datas):
            diasFormatados += ','
            diasFormatados += traducaoDias[data]



    rotina = subprocess.run(
        f'schtasks /create /tn OneTickMensagemPersonalizada /tr {pasta} /SC weekly /D {diasFormatados} /ST {horario}',
        shell=True,
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

    pasta = cursor.fetchone()[0] + '\SendDaily.exe'



    __apagarRotina('OneTickMensagemDiaria')

    rotina = subprocess.run(
        f'schtasks /create /tn OneTickMensagemDiaria /tr {pasta} /SC DAILY /ST {horario}', shell=True,
        text=True)


#ATUALIZA OS VALORES DA SEMANA AO CONCLUIR INTERFACE
def atualizarRotinaSemanalInterface(cursor):
    info = extrairMensagensSemanal(cursor)[0]

    horario = info[1]

    cursor.execute('SELECT * FROM informacoes')

    pasta = cursor.fetchone()[0] + '\SendSemanal.exe'



    __apagarRotina('OneTickMensagemSemanal')

    rotina = subprocess.run(
        f'schtasks /create /tn OneTickMensagemSemanal /tr {pasta} /SC WEEKLY /ST {horario}', shell=True,
        text=True)


#ATUALIZA OS VALORES DA MENSAL AO CONCLUIR INTERFACE
def atualizarRotinaMensalInterface(cursor):
    info = extrairMensagensMensal(cursor)[0]
    horario = info[1]

    cursor.execute('SELECT * FROM informacoes')

    pasta = cursor.fetchone()[0] + '\SendMensal.exe'



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



    __apagarRotina('OneTickMensagemNormal')

    rotina = subprocess.run(
        f'schtasks /create /tn OneTickMensagemNormal /tr {pasta}  /SC ONCE /ST {horario} /SD {data}/2022 ', shell=True,
    text=True)



# ATUALIZA OS VALORES DA DIARIA AO CONCLUIR INTERFACE
def atualizarRotinaPersonalizadaInterface(cursor):
    info = extrairMensagensPersonalizada(cursor)[0]

    horario = info[1]

    cursor.execute('SELECT * FROM informacoes')

    pasta = cursor.fetchone()[0] + '\SendPersonalizada.exe'



    __apagarRotina('OneTickMensagemPersonalizada')

    traducaoDias = {
        "Domingo": "SUN",
        "Sábado": "SAT",
        "Sexta-feira": "FRI",
        "Quinta-feira": "THU",
        "Quarta-feira": "WED",
        "Terça-feira": "TUE",
        "Segunda-feira": "MON",
    }

    datas = info[9]


    datas = ast.literal_eval(datas)
    diasFormatados = ''
    count = 0

    for data in datas:
        count += 1
        if count == 1:
            diasFormatados += traducaoDias[data]
        elif count <= len(datas):
            diasFormatados += ','
            diasFormatados += traducaoDias[data]




    rotina = subprocess.run(
        f'schtasks /create /tn OneTickMensagemPersonalizada /tr {pasta} /SC weekly /D {diasFormatados} /ST {horario}',
        shell=True,
        text=True)
    # subprocess.run(f'schtasks /change /tn testeCMDbanana /st 14:00 ', shell=True, text=True, input='')


    # self.rotina = subprocess.run(
    #     f'schtasks /Delete /tn testeCMDbanana /F', shell=True,
    #     text=True)


        # self.rotina = subprocess.run('where python', shell=True, capture_output=True, text=True)




def verificarDBNormal(cursor):
    if extrairMensagensEnvio(cursor):
        filaMensagens = extrairMensagensEnvio(cursor)[0]
        cursor.execute('UPDATE Mensagens SET status = "ENVIADO" WHERE mensagens = ? AND dia = ? AND data_criada = ? AND hora_criada = ? AND nome_rotina = ?',
                       (filaMensagens[0], filaMensagens[2], filaMensagens[6], filaMensagens[7], filaMensagens[8]))

        cursor.execute('DELETE FROM Mensagens WHERE status = "ENVIADO" AND dia != "Diária" AND dia != "Semanal" AND dia != "Mensal" AND dia != "Personalizada"')

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
            'UPDATE Mensagens SET status = "ENVIADO" WHERE mensagens = ? AND data_criada = ? AND hora_criada = ? AND nome_rotina = ?',
            (filaMensagens[0], filaMensagens[6], filaMensagens[7], filaMensagens[8]))
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

    try:
        criarRotinaMensal(cursor)
        cursor.execute(
            'UPDATE Mensagens SET status = "ENVIADO" WHERE mensagens = ? AND data_criada = ? AND hora_criada = ? AND nome_rotina = ?',
            (filaMensagens[0], filaMensagens[6], filaMensagens[7], filaMensagens[8]))
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

    try:
        criarRotinaSemanal(cursor)
        cursor.execute(
            'UPDATE Mensagens SET status = "ENVIADO" WHERE mensagens = ? AND data_criada = ? AND hora_criada = ? AND nome_rotina = ?',
            (filaMensagens[0], filaMensagens[6], filaMensagens[7], filaMensagens[8]))
    except:

        __apagarRotina('OneTickMensagemSemanal')

    return filaMensagens



def apagarRotinasInterface(cursor):
    criarRotinaDiaria(cursor)
    criarRotinaMensal(cursor)
    criarRotinaNormal(cursor)
    criarRotinaSemanal(cursor)
    criarRotinaPersonalizada(cursor)
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

    if extrairMensagensPersonalizada(cursor):
        atualizarRotinaPersonalizadaInterface(cursor)



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
    conexao = sqlite3.connect(rf'{localContent}')
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




def apagarTodasRotinas(cursor):
    cursor.execute('DELETE FROM Mensagens')
    criarRotinaNormal(cursor)
    criarRotinaDiaria(cursor)
    criarRotinaSemanal(cursor)
    criarRotinaMensal(cursor)
    criarRotinaPersonalizada(cursor)





def atualizarLogin(cursor, numero):
    if numero == 1:
        cursor.execute('UPDATE Login SET logado = ?, ultimo_acesso = ?, cor_status = ?', (numero, horarios()[0], "rgb(85, 255, 127)",))
    elif numero == 0:
        cursor.execute('UPDATE Login SET logado = ?, ultimo_acesso = ?, cor_status = ?', (numero, horarios()[0], "rgb(255, 0, 0)",))
    else:
        cursor.execute('UPDATE Login SET logado = ?, ultimo_acesso = ?, cor_status = ?', (1, horarios()[0], "rgb(255, 0, 0)",))






 #------------------------------------------------------#










conexao = sqlite3.connect(rf'{localContent}')
cursor = conexao.cursor()
#



atualizarDados(cursor)
# criarRotinaPersonalizada(cursor)
# atualizarRotinaPersonalizadaInterface(cursor)
# print(extrairMensagensEnvio(cursor))
# apagarTodasRotinas(cursor)
# atualizarRotinasInterface(cursor)
# verificarDBNormal(cursor)
# verificarDBDiaria(cursor)

#
conexao.commit()
cursor.close()
conexao.close()