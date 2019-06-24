"""
Modelo IA Reativo Simples
"""
from tarefas_controlador import controle_tarefas
from _global import insert_message
import random
import time


class bot():
    def __init__(self):
        # Definição de atributos do ambientes que são relevantes para tomadas de decisão.
        """
        #Atributos naturais
        tempo_count = 0
        temperatura = random.uniform(21, 29)
        chuva = random.choice([True, False])
        porta = random.choice([True, False])
        movimento = random.choice([True, False])
        tempo = random.choice(["Normal", "Quente", "Frio"])
        **** 
        #Atributos de atuadores
        ar_condicionado = False
        aquecedor = False
        lampada = False
        porta = False
        televisão = False
        janela = False
        """
        self.controlador = controle_tarefas()

    def check_task(self, ambiente):
        # Decisões tomadas a partir de condicionais

        # Janela
        if(ambiente.chuva):
            # Fechar a janela em caso de chuva.
            if(ambiente.janela == False):
                self.controlador.cria_tarefa('JANELA_FECHAR')

        elif(ambiente.ar_condicionado == False and ambiente.aquecedor == False):
            # Abrir a janela caso ar condicionado ou aquecedor ligado.
            if(ambiente.janela == True):
                self.controlador.cria_tarefa('JANELA_ABRIR')

        # A temperatura ideal é 23.
        # Ar condicionado
        if(ambiente.mov_count > 900):
            # Desligar o ar condicionado caso não haja movimento por 15 minutos.
            # Tarefa desligar ar condicionado
            if(ambiente.ar_condicionado):
                self.controlador.cria_tarefa('ARCOND_DESLIG')

        # Ligar o ar condicionado caso a temperatura externa for superior a 32.
        if(ambiente.temperatura > 32):
            if(ambiente.ar_condicionado == False):
                if(ambiente.janela == False):
                    # Tarefa fechar janela
                    self.controlador.cria_tarefa('JANELA_FECHAR')

                # Tarefa ligar ar condicionador
                if(ambiente.ar_condicionado == False):
                    self.controlador.cria_tarefa('ARCOND_LIGAR')

        # Desligar o ar condicionado caso a temperatura externa for inferior a 20.
        if(ambiente.temperatura < 20):
            if(ambiente.ar_condicionado):
                self.controlador.cria_tarefa('ARCOND_DESLIG')

        # Aquecedor

        # Ligar o aquecedor caso a temperatura externa for inferior a 10.
        if(ambiente.temperatura < 10):
            if(ambiente.aquecedor == False):
                if(ambiente.janela == False):
                    # Tarefa fechar janela
                    self.controlador.cria_tarefa('JANELA_FECHAR')

                # Tarefa ligar aquecedor
                self.controlador.cria_tarefa('AQUECE_LIGAR')

        if(ambiente.temperatura > 20):
            if(ambiente.aquecedor):
                self.controlador.cria_tarefa('AQUECE_DESLIG')

        # Lâmpada
        if(ambiente.mov_count > 900):
            # Desligar a lâmpada caso não haja movimento em 15 min.
            if(ambiente.lampada):
                self.controlador.cria_tarefa('LAMPAD_DESLIG')

        # Porta
        if(ambiente.ar_condicionado and ambiente.mov_count > 300):
            # Fechar a porta após 5 minutos se o ar condicionado estiver ligado.
            if(ambiente.porta == False):
                self.controlador.cria_tarefa('PORTA_FECHAR')

        if(ambiente.mov_count > 300):
            # Fechar a porta e desligar a televisão se ela ficar aberta por mais de 5 minutos.
            if(ambiente.porta == False):
                self.controlador.cria_tarefa('PORTA_FECHAR')

            if(ambiente.televisão == True):
                self.controlador.cria_tarefa('TV_DESLIG')

        # Aspirador
        if(ambiente.sujeira == True and ambiente.mov_count > 20):
            if(ambiente.aspirador == False):
                ambiente.aspirador = True
                self.controlador.cria_tarefa('ASPIRA')

    def acao_usuario(self, ambiente):
        # Simula uma interação aleatória feita pelo usuário.
        # Gera tarefas de deadline curta
        event_flag = False
        aux_num = random.uniform(0, 100)
        if(aux_num < 10):
            if(ambiente.lampada == True):
                insert_message("Usuário desligou a lâmpada.")
                self.controlador.cria_tarefa('LAMPAD_DESLIG')
            else:
                insert_message("Usuário ligou a lâmpada.")
                self.controlador.cria_tarefa('LAMPAD_LIGAR')
            event_flag = True

        aux_num = random.uniform(0, 100)
        if(aux_num < 5):
            if(ambiente.porta == True):
                insert_message("Usuário abriu a porta.")
                self.controlador.cria_tarefa('PORTA_ABRIR')
            else:
                insert_message("Usuário fechou a porta.")
                self.controlador.cria_tarefa('PORTA_FECHAR')

            ambiente.sujeira == random.choice([True, False])
            event_flag = True

        aux_num = random.uniform(0, 100)
        if(aux_num < 20):
            if(ambiente.televisão == True):
                insert_message("Usuário desligou a televisão.")
                self.controlador.cria_tarefa('TV_DESLIG')
            else:
                insert_message("Usuário ligou a televisão.")
                self.controlador.cria_tarefa('TV_LIGAR')
            event_flag = True

        return event_flag
