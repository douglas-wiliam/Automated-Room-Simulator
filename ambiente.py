import random, time, os
from tempo import tempo_normal, tempo_frio, tempo_quente
from bot import bot

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
        self.tempo_count = 0
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

    def passar_tempo(self):
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

        aux_num = random.uniform(0,100)
        if(aux_num < 0.2):
            #0.2% de chance de movimento. Reseta contagem
            print("Usuário executou movimento.")
            self.mov_count = 0
            
        if(self.tempo_count > 18*3600):    
            aux_num = random.uniform(0,100)
            if(aux_num < 0.5 and self.lampada == False):
                print("Usuário ligou a lâmpada.")
                #0.5% de chance de ligar luz.
                self.lampada = True
            
        aux_num = random.uniform(0,100)
        if(aux_num < 0.5 and self.porta == False):
            #0.5% de chance de abrir porta.
            print("Usuário abriu a porta.")
            self.porta = True    

        if(self.tempo_count > 24*3600):
            #Resetar contador de tempo ao final do dia
            self.tempo_count = 0
            
            
        self.tempo_count += 1
        self.mov_count += 1
        
        """ Mudança de temperatura e tempo """
        if(self.tempo == "Normal"):
            self.temperatura = tempo_normal(self.temperatura, self.tempo_count)

                
        if(self.tempo == "Quente"):
            self.temperatura = tempo_quente(self.temperatura, self.tempo_count)

                        
        if(self.tempo == "Frio"):
            self.temperatura = tempo_frio(self.temperatura, self.tempo_count)
        
        
#############################################################################
ambiente = ambiente()
intervalo_prints = 2
ambiente.tempo = 'Normal'
bot_decisao = bot()
while(True):
    ambiente.passar_tempo()
    bot_decisao.check_task(ambiente)
    if(ambiente.tempo_count%1800 == 0):
        time.sleep(intervalo_prints)
        os.system('cls')
        print("Hora: " + str(ambiente.tempo_count/3600))
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
        