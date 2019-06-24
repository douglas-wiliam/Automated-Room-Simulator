# -*- coding: utf-8 -*-
import random
"""
Módulo para variações de temperatura de acordo com o estado atmosférico
"""

def estado_atmosferico_normal(temperatura_atual, tempo_count):
    #Normalizando a temperatura
    temperatura_nova = temperatura_atual
    if(temperatura_atual < 0):
        #Se a temperatura atual for menor que 20 graus, ela irá aumentar gradualmente até atingir esse valor.
        temperatura_nova += random.uniform(0, 0.1)/50
        
    elif(temperatura_atual > 30):
        #Se a temperatura atual for menor que 20 graus, ela irá aumentar gradualmente até atingir esse valor.
        temperatura_nova += random.uniform(-0.1, 0)/50
        
    else:
        #Variando a temperatura semi-aleatoriamente
        if(tempo_count < 3600*6):
            #Variação de temperatura antes das 6
            temperatura_nova += random.uniform(-0.2, 0)/50
        elif(tempo_count < 3600*18):
            #Variação de temperatura antes das 18
            temperatura_nova += random.uniform(-0.2, 0.2)/50
        else:
            #Variação de temperatura antes das 24
            temperatura_nova += random.uniform(-0.2,0)/50
        
    return temperatura_nova

def estado_atmosferico_quente(temperatura_atual, tempo_count):
    #Normalizando a temperatura
    temperatura_nova = temperatura_atual
    if(temperatura_atual < 28):
        #Se a temperatura atual for menor que 20 graus, ela irá aumentar gradualmente até atingir esse valor.
        temperatura_nova += random.uniform(0, 0.2)/50
        
    elif(temperatura_atual > 45):
        #Se a temperatura atual for menor que 20 graus, ela irá aumentar gradualmente até atingir esse valor.
        temperatura_nova += random.uniform(-0.2, 0)/50 
    else:
        #Variando a temperatura semi-aleatoriamente
        if(tempo_count < 3600*6):
            #Variação de temperatura antes das 6
            temperatura_nova += random.uniform(-0.2, 0.2)/50
        elif(tempo_count < 3600*18):
            #Variação de temperatura antes das 18
            temperatura_nova += random.uniform(-0.2, 0.3)/50
        else:
            #Variação de temperatura antes das 24
            temperatura_nova += random.uniform(-0.2, 0.2)/50
            
    return temperatura_nova
            
def estado_atmosferico_frio(temperatura_atual, tempo_count):
    #Normalizando a temperatura
    temperatura_nova = temperatura_atual
    if(temperatura_atual < -5):
        #Se a temperatura atual for menor que 20 graus, ela irá aumentar gradualmente até atingir esse valor.
        temperatura_nova += random.uniform(0, 0.2)/50
        
    elif(temperatura_atual > 16):
        #Se a temperatura atual for menor que 20 graus, ela irá aumentar gradualmente até atingir esse valor.
        temperatura_nova += random.uniform(-0.2, 0)/50      
    else:
        #Variando a temperatura semi-aleatoriamente
        if(tempo_count < 3600*6):
            #Variação de temperatura antes das 6
            temperatura_nova += random.uniform(-0.25, 0.2)/50
        elif(tempo_count < 3600*18):
            #Variação de temperatura antes das 18
            temperatura_nova += random.uniform(-0.3, 0.3)/50
        else:
            #Variação de temperatura antes das 24
            temperatura_nova += random.uniform(-0.25, 0.2)/50
            
    return temperatura_nova