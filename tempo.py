# -*- coding: utf-8 -*-
import random
"""
Módulo para variações de temperatura de acordo com o tempo
"""
def tempo_sol(temp_atual, tempo):
    temp_max = 45
    temp_min = -5
    
    if(temp_atual > temp_max):
        #Não pode aumentar a temperatura
        #Pode só diminuir
        temp_nova = temp_atual + random.uniform(-2,0)
        
    if(temp_atual < temp_min):
        #Não pode diminuir a temperatura
        #Pode só aumentar
        temp_nova = temp_atual + random.uniform(0,2)
        
    return temp_nova