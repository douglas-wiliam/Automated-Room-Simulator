import random, time, os
from tempo import tempo_normal, tempo_frio, tempo_quente
from bot import bot
import datetime
from tabelas import tabela_ambiente, tabela_tarefas

"""
Módulo para simulação do ambiente interno de uma casa.

CONVENÇÕES:        
    TEMPO:
        EH DADO EM MINUTOS
        0 EH MEIA NOITE
        12*3600 EH MEIO DIA
        E ASSIM VAI
        
    O tempo EH STRINGS
    
    O RESTO EH TUDO BOOLEANO
"""      
class ambiente(object):
    def __init__(self):
        #Atributos naturais
        self.mov_count = 0
        self.temperatura = random.uniform(21, 29)
        self.chuva = random.choice([True, False])
        self.porta = random.choice([True, False])
        self.movimento =     random.choice([True, False])
        self.tempo = random.choice(["Normal", "Quente", "Frio"])
        
        #Atributos de atuadores
        self.ar_condicionado = False
        self.aquecedor = False
        self.lampada = False
        self.porta = False
        self.televisão = False
        self.janela = False

    def alterar_tempo(self):
        aux_num = random.uniform(0,200)
        if(aux_num < 0.1):
            #0.05% de chance de mudar de clima por segundo.
            self.tempo = random.choice(["Normal", "Quente", "Frio"])
            print("Tempo mudou para " + str(self.tempo) + ".")
            
        aux_num = random.uniform(0,150)
        if(aux_num < 0.1):
            #% de chance de começar a chover ou parar de chover.
            self.chuva = not self.chuva
            if(self.chuva):
                print("Começou a chover.")
            else:
                print("Parou de chover.")
                   
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
intervalo_prints = 2
ambiente.tempo = 'Normal'
bot_decisao = bot()

tabela_ambiente = tabela_ambiente(ambiente)
tabela_tarefas = tabela_tarefas(bot_decisao.controlador.lista_tarefas)

while(True):
    if(GLOBAL_TEMPO > 24*3600):
        #Resetar contador de tempo ao final do dia
        GLOBAL_TEMPO = 0
    else:
        #Passagem do tempo
        GLOBAL_TEMPO += 2

    ambiente.alterar_tempo()
    bot_decisao.check_task(ambiente)

    if(GLOBAL_TEMPO%600 == 0):
        time.sleep(intervalo_prints)
        os.system('clear')
        """
        print("Hora: " + str(datetime.timedelta(seconds=GLOBAL_TEMPO)))
        print("Temperatura: " + str(round(ambiente.temperatura, 2)))
        print("Chuva: " + str(ambiente.chuva))
        print("Tempo: " + str(ambiente.tempo))
        print("Timer movimento: " + str(ambiente.mov_count))
        
        print("Ar condicionado: " + str(ambiente.ar_condicionado))
        print("Aquecedor: " + str(ambiente.aquecedor))
        print("Lâmpada: " + str(ambiente.lampada))
        print("Porta: " + str(ambiente.porta))
        print("Janela: " + str(ambiente.ar_condicionado))
        print("Televisão: " + str(ambiente.televisão))
        print("--------------------------------------")
        """
        ### TABELA DE DADOS ###
        tabela_ambiente.print_table(GLOBAL_TEMPO)
        print("===================================")
        tabela_tarefas.print_table()
        print("============================================================")
        lista_tarefas = bot_decisao.controlador.lista_tarefas
        for index in lista_tarefas:
            print(index.nome)

    if(GLOBAL_TEMPO%5 == 0):
        #Simulação de usuário alterando o ambiente.
        bot_decisao.acao_usuario()
        aux_num = random.uniform(0,100)

        if(aux_num < 0.2):
            #0.2% de chance de movimento. Reseta contagem
            print("Usuário executou movimento.")
            ambiente.mov_count = 0