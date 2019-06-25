import random
from estado_atmosferico import estado_atmosferico_normal, estado_atmosferico_frio, estado_atmosferico_quente
from _global import insert_message

class ambiente(object):
    def __init__(self):
        #Atributos naturais
        self.mov_count = 0
        self.temperatura = random.uniform(5, 30)
        self.chuva = random.choice([True, False])
        self.porta = random.choice([True, False])
        self.sujeira = True
        self.estado_atmosferico = random.choice(["Normal", "Quente", "Frio"])
        
        #Atributos de atuadores
        self.ar_condicionado = False
        self.aquecedor = False
        self.lampada = False
        self.janela = False #False - Aberto, True - Fechado
        self.porta = False #False - Aberto, True - Fechado
        self.televisão = False
        self.aspirador = False


    def alterar_estado_atmosferico(self, tempo_global):
        aux_num = random.uniform(0,200)
        if(aux_num < 0.1):
            #0.1% de chance de mudar de estado atmosférico por segundo.
            self.estado_atmosferico = random.choice(["Normal", "Quente", "Frio"])
            insert_message("estado_atmosferico mudou para " + str(self.estado_atmosferico) + ".")
            
        aux_num = random.uniform(0,150)
        if(aux_num < 0.1):
            #% de chance de começar a chover ou parar de chover.
            self.chuva = not self.chuva
            if(self.chuva):
                insert_message("Começou a chover.")
            else:
                insert_message("Parou de chover.")
                   
        self.mov_count += 1
        
        """ Mudança de temperatura e estado atmosférico """
        if(self.estado_atmosferico == "Normal"):
            self.temperatura = estado_atmosferico_normal(self.temperatura, tempo_global)

                
        if(self.estado_atmosferico == "Quente"):
            self.temperatura = estado_atmosferico_quente(self.temperatura, tempo_global)

                        
        if(self.estado_atmosferico == "Frio"):
            self.temperatura = estado_atmosferico_frio(self.temperatura, tempo_global)
        