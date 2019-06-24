from bot import bot
import random, time, os, sys
from ambiente import ambiente
from tabelas import tabela_ambiente, tabela_tarefas
from _global import insert_message, print_messages
from estado_atmosferico import estado_atmosferico_normal, estado_atmosferico_frio, estado_atmosferico_quente


ambiente = ambiente()
TEMPO_GLOBAL = 0
intervalo_prints = 1.0
ambiente.estado_atmosferico = 'Normal'
bot_decisao = bot()

tabela_ambiente = tabela_ambiente(ambiente)
tabela_tarefas = tabela_tarefas(bot_decisao.controlador.escalonador.tarefas_lista)

event_flag = False

while(True):
    time.sleep(intervalo_prints)

    if(TEMPO_GLOBAL%600 == 0 or event_flag):
        if(event_flag):
            time.sleep(0.7)
            event_flag = False

    os.system('clear')

    if(TEMPO_GLOBAL > 24*3600):
        #Resetar contador de tempo ao final do dia
        TEMPO_GLOBAL = 0
    else:
        #Passagem do tempo
        TEMPO_GLOBAL += 1
        if(bot_decisao.controlador.escalonador.tarefa_exec != None):
            nome = bot_decisao.controlador.escalonador.tarefa_exec.nome
            deadline = bot_decisao.controlador.escalonador.tarefa_exec.deadline
            tempo_exec = bot_decisao.controlador.escalonador.tarefa_exec.tempo_exec
            tempo_req = bot_decisao.controlador.escalonador.tarefa_exec.tempo_req
        else:
            nome = "Nenhuma"
            deadline = 0
            tempo_exec = 0
            tempo_req = 0

    #Tarefas periódicas
    ambiente.alterar_estado_atmosferico(TEMPO_GLOBAL)
    bot_decisao.check_task(ambiente)
    if(bot_decisao.controlador.escalonador.check_deadlines()):
        #checar se alguma tarefa teve a deadline estourada
        event_flag = True

    #### ATUADORES ####
    exec_ = bot_decisao.controlador.escalonador.executar()
    if(exec_ != None):
        #Checar se há algo executando, ligar a flag caso positivo.
        event_flag = True
        
        #Checar se a tarefa foi concluida.
        if(exec_ == 'JANELA_ABRIR_c'):
            bot_decisao.controlador.JANELA_ABRIR = False
            ambiente.janela = False

        if(exec_ == 'JANELA_FECHAR_c'):
            bot_decisao.controlador.JANELA_FECHAR = False
            ambiente.janela = True
            print("------ JANELA FECHADA -------")

        if(exec_ == 'PORTA_ABRIR_c'):
            bot_decisao.controlador.PORTA_ABRIR = False
            ambiente.porta = False

        if(exec_ == 'PORTA_FECHAR_c'):
            bot_decisao.controlador.PORTA_FECHAR = False
            ambiente.porta = True

        if(exec_ == 'ARCOND_LIGAR_c'):
            bot_decisao.controlador.ARCOND_LIGAR = False
            ambiente.lampada = True

        if(exec_ == 'ACORND_DESLIG_c'):
            bot_decisao.controlador.ARCOND_DESLIG  = False
            ambiente.lampada = False

        if(exec_ == 'AQUECE_LIGAR_c'):
            bot_decisao.controlador.AQUECE_LIGAR  = False
            ambiente.aquecedor = True

        if(exec_ == 'AQUECE_DESLIG_c'):
            bot_decisao.controlador.AQUECE_DESLIG = False
            ambiente.aquecedor = False

        if(exec_ == 'LAMPAD_LIGAR_c'):
            bot_decisao.controlador.LAMPAD_LIGAR = False
            ambiente.lampada = True

        if(exec_ == 'LAMPAD_DESLIG_c'):
            bot_decisao.controlador.LAMPAD_DESLIG = False
            ambiente.lampada = False

        if(exec_ == 'TV_LIGAR_c'):
            bot_decisao.controlador.TV_LIGAR = False
            ambiente.televisão = True

        if(exec_ == 'TV_DESLIG_c'):
             bot_decisao.controlador.TV_DESLIG = False
             ambiente.televisão = False 

    if(TEMPO_GLOBAL%2 == 0):
        #Simulação de usuário alterando o ambiente.
        event_flag = bot_decisao.acao_usuario(ambiente)
        aux_num = random.uniform(0,100)

        if(aux_num < 0.2):
            #0.2% de chance de movimento. Reseta contagem
            insert_message("Usuário executou movimento.")
            event_flag = True
            ambiente.mov_count = 0

    ### TABELAS DE DADOS ###
    tabela_ambiente.print_table(TEMPO_GLOBAL)
    print("===================================")
    print("Executando:" + str(nome))
    print("Deadline: " + str(deadline))
    print("T. Exe: " + str(tempo_exec))
    print("T. Req: " + str(tempo_req))
    tabela_tarefas.print_table()
    print("===========================================================================")
    print_messages()
