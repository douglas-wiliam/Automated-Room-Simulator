import random
from tempo import tempo_normal, tempo_frio, tempo_quente
from _global import insert_message

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


    def alterar_tempo(self, tempo_global):
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
            self.temperatura = tempo_normal(self.temperatura, tempo_global)

                
        if(self.tempo == "Quente"):
            self.temperatura = tempo_quente(self.temperatura, tempo_global)

                        
        if(self.tempo == "Frio"):
            self.temperatura = tempo_frio(self.temperatura, tempo_global)
        