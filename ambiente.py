import random, time, os, sys
from tempo import tempo_normal, tempo_frio, tempo_quente
from bot import bot
import datetime
from tabelas import tabela_ambiente, tabela_tarefas
from _global import insert_message, print_messages



class ambiente(object):
    def __init__(self):
        #Atributos naturais
        self.mov_count = 0
        self.temperatura = random.uniform(5, 30)
        self.chuva = random.choice([True, False])
        self.porta = random.choice([True, False])
        self.movimento = random.choice([True, False])
        self.tempo = random.choice(["Normal", "Quente", "Frio"])
        
        #Atributos de atuadores
        self.ar_condicionado = False
        self.aquecedor = False
        self.lampada = False
        self.janela = False #False - Aberto, True - Fechado
        self.porta = False #False - Aberto, True - Fechado
        self.televisão = False


    def alterar_tempo(self):
        aux_num = random.uniform(0,200)
        if(aux_num < 0.1):
            #0.05% de chance de mudar de clima por segundo.
            self.tempo = random.choice(["Normal", "Quente", "Frio"])
            insert_message("Tempo mudou para " + str(self.tempo) + ".")
            
        aux_num = random.uniform(0,150)
        if(aux_num < 0.1):
            #% de chance de começar a chover ou parar de chover.
            self.chuva = not self.chuva
            if(self.chuva):
                insert_message("Começou a chover.")
            else:
                insert_message("Parou de chover.")
                   
        self.mov_count += 1
        
        """ Mudança de temperatura e tempo """
        if(self.tempo == "Normal"):
            self.temperatura = tempo_normal(self.temperatura, GLOBAL_TEMPO)

                
        if(self.tempo == "Quente"):
            self.temperatura = tempo_quente(self.temperatura, GLOBAL_TEMPO)

                        
        if(self.tempo == "Frio"):
            self.temperatura = tempo_frio(self.temperatura, GLOBAL_TEMPO)
        
        
#############################################################################

ambiente = ambiente()
GLOBAL_TEMPO = 0
intervalo_prints = 0.05
ambiente.tempo = 'Normal'
bot_decisao = bot()

tabela_ambiente = tabela_ambiente(ambiente)
tabela_tarefas = tabela_tarefas(bot_decisao.controlador.escalonador.tarefas_lista)

event_flag = False

#### TESTE ####
bot_decisao.controlador.cria_tarefa('JANELA_FECHAR')
"""
bot_decisao.controlador.cria_tarefa('PORTA_FECHAR')
bot_decisao.controlador.cria_tarefa('LAMPAD_LIGAR')
bot_decisao.controlador.cria_tarefa('ARCOND_LIGAR')
bot_decisao.controlador.cria_tarefa('AQUECE_LIGAR')
bot_decisao.controlador.cria_tarefa('TV_LIGAR')

bot_decisao.controlador.cria_tarefa('JANELA_ABRIR')
bot_decisao.controlador.cria_tarefa('PORTA_ABRIR')
bot_decisao.controlador.cria_tarefa('LAMPAD_DESLIG')
bot_decisao.controlador.cria_tarefa('ARCOND_DESLIG')
bot_decisao.controlador.cria_tarefa('AQUECE_DESLIG')
bot_decisao.controlador.cria_tarefa('TV_DESLIG')
"""

while(True):
    time.sleep(intervalo_prints)

    if(GLOBAL_TEMPO%600 == 0 or event_flag):
        if(event_flag):
            time.sleep(0.7)
            event_flag = False

    os.system('clear')

    if(GLOBAL_TEMPO > 24*3600):
        #Resetar contador de tempo ao final do dia
        GLOBAL_TEMPO = 0
    else:
        #Passagem do tempo
        GLOBAL_TEMPO += 1
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
    ambiente.alterar_tempo()
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

    if(GLOBAL_TEMPO%5 == 0):
        #Simulação de usuário alterando o ambiente.
        event_flag = bot_decisao.acao_usuario()
        aux_num = random.uniform(0,100)

        if(aux_num < 0.2):
            #0.2% de chance de movimento. Reseta contagem
            insert_message("Usuário executou movimento.")
            event_flag = True
            ambiente.mov_count = 0

    ### TABELAS DE DADOS ###
    tabela_ambiente.print_table(GLOBAL_TEMPO)
    print("===================================")
    print("Executando:" + str(nome))
    print("Deadline: " + str(deadline))
    print("T. Exe: " + str(tempo_exec))
    print("T. Req: " + str(tempo_req))
    tabela_tarefas.print_table()
    print("===========================================================================")
    print_messages()
