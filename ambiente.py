import random, time, os
from tempo import tempo_sol

"""
Módulo para simulação do ambiente interno de uma casa.

CONVENÇÕES:

    LUMINOSIDADE:
        0 É ESCURIDÃO COMPLETA
        5 É PENUMBRA
        8 É LUZ NATURAL TRÊS DA TARDE
        10 É LUZ ARTIFICIAL OU MEIO DIA
        
    TEMPO:
        EH DADO EM MINUTOS
        0 EH MEIA NOITE
        12*3600 EH MEIO DIA
        E ASSIM VAI
        
    O tempo EH STRINGS
    
    O RESTO EH TUDO BOOLEANO
"""      
    



class ambiente():
    def __init__(self):
        #Atributos naturais
        self.tempo_count = 0
        self.temperatura = random.uniform(-5, 35)
        self.luminosidade = 0
        self.chuva = random.choice([True, False])
        self.porta = random.choice([True, False])
        self.movimento = random.choice([True, False])
        self.tempo = random.choice(["Sol", "Sol entre nuvens", "Nublado", "Chuva"])
        
        #Atributos de atuadores
        self.ar_condicionado = False
        self.aquecedor = False
        self.cortina = False
        self.lampada = False
        self.porta = False
        self.televisão = False
        self.janela = False

    def passar_tempo(self):
        aux_num = 0
        if(self.tempo_count > 24*3600):
            self.tempo_count = 0
            
        self.tempo_count += 1
        aux_num = random.uniform(0,100)
        
        """ Mudança de temperatura e tempo """
        if(self.tempo == "Sol"):
            self.temperatura = tempo_sol(self.temperatura, self.tempo_count)

                
        if(self.tempo == "Sol entre nuvens"):
            self.temperatura = tempo_sol_entre_nuvens(self.temperatura, self.tempo_count)

                        
        if(self.tempo == "Chuva"):
            self.temperatura = tempo_chuva(self.temperatura, self.tempo_count)
    
        
        if(self.tempo == "Nublado"):
            self.temperatura = tempo_nublado(self.temperatura, self.tempo_count)
            #Verificação de mudanças de tempo via temperatura
        
        
#############################################################################
ambiente = ambiente()
ambiente.tempo = 'Sol'

while(True):
    ambiente.passar_tempo()
    if(ambiente.tempo_count%3600 == 0):
        print("Hora: " + str(ambiente.tempo_count/3600))
        print("Temperatura: " + str(ambiente.temperatura))
        print("Tempo: " + str(ambiente.tempo))
        