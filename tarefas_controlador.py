# Módulo de controle de tarefas da IA.
import random
import time
import os
from _global import insert_message


class tarefa(object):
    def __init__(self, nome, n_id, deadline, tempo_req):
        self.nome = nome
        self.id = n_id
        # Deadline dado em tempo relativo (tempo da deadline - tempo atual)
        self.deadline = deadline
        self.tempo_exec = 1
        self.tempo_req = tempo_req

        self.event_flag = False  # Flag para printar quando algo ocorrer.


class escalonador():
    # Algoritmo EDF.
    # Preemptivo
    # Sem tempo de chaveamento
    def __init__(self):
        self.tarefas_lista = list()
        self.tarefa_exec = None

    def inserir_tarefa(self, tarefa):
        self.tarefas_lista.append(tarefa)
        self.tarefas_lista.sort(key=lambda x: x.deadline, reverse=False)

    def check_deadlines(self):
        if(len(self.tarefas_lista) <= 0):
            return False

        for tarefa in self.tarefas_lista:
            tarefa.deadline -= 1
            if(tarefa.deadline <= 0):
                insert_message("A tarefa " + tarefa.nome +
                               " teve sua deadline estourada.")
                insert_message("Removendo tarefa da lista...")
                self.tarefas_lista.remove(tarefa)
                return tarefa.nome + "_r"

        return None

    def executar(self):
        if(self.tarefa_exec == None):
            # Ausência de tarefa no processador. Pegar a do topo da lista.
            if(len(self.tarefas_lista) <= 0):
                return None

            if(self.tarefas_lista[0] != None):
                # Checa se a lista tem pelo menos uma tarefa pronta para executar.
                self.tarefa_exec = self.tarefas_lista.pop(0)
                insert_message(
                    "A tarefa " + self.tarefa_exec.nome + " está sendo executada.")
                return self.tarefa_exec.nome
            else:
                # Ausência de tarefa na fila.
                return None

        else:
            # Tarefa presente no processador.
            self.tarefa_exec.tempo_exec += 1

            # Checar se a tarefa foi concluída.
            if(self.tarefa_exec.tempo_exec >= self.tarefa_exec.tempo_req):
                nome = self.tarefa_exec.nome
                insert_message("A tarefa " + nome + " foi concluída.")
                self.tarefa_exec = None
                return nome + "_c"

            # Tarefa presente no processador.
            else:
                # Checa se há outra tarefa com deadline menor na fila
                if(len(self.tarefas_lista) > 0):
                    if(self.tarefas_lista[0].deadline < self.tarefa_exec.deadline):
                        insert_message(
                            "A tarefa " + self.tarefa_exec.nome + " sofreu preempção.")
                        self.inserir_tarefa(self.tarefa_exec)
                        self.tarefa_exec = self.tarefas_lista.pop(0)
                        return None
                else:
                    return 'Executando'


class controle_tarefas():
    def __init__(self):
        self.ID_COUNT = 0

        # Flags para verificar as tarefas já existentes na fila.
        # As flags são setadas novamente para falta quando elas saírem da fila.
        #   Isso será feito durante o escalonamento.
        self.JANELA_ABRIR = False
        self.JANELA_FECHAR = False

        self.PORTA_ABRIR = False
        self.PORTA_FECHAR = False

        self.ARCOND_LIGAR = False
        self.ARCOND_DESLIG = False

        self.AQUECE_LIGAR = False
        self.AQUECE_DESLIG = False

        self.LAMPAD_LIGAR = False
        self.LAMPAD_DESLIG = False

        self.TV_LIGAR = False
        self.TV_DESLIG = False

        self.ASPIRA = False

        self.escalonador = escalonador()

    def cria_tarefa(self, nome):

        ###JANELA###
        if(nome == 'JANELA_ABRIR' and not self.JANELA_ABRIR):
            deadline = 10
            tempo_exec = random.randint(5, 10)
            tarefa_ = tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.escalonador.inserir_tarefa(tarefa_)
            self.JANELA_ABRIR = True
            self.ID_COUNT += 1

        elif(nome == 'JANELA_FECHAR' and not self.JANELA_FECHAR):
            deadline = 10
            tempo_exec = random.randint(5, 10)
            tarefa_ = tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.escalonador.inserir_tarefa(tarefa_)
            self.JANELA_FECHAR = True
            self.ID_COUNT += 1

        ###PORTA###
        elif(nome == 'PORTA_ABRIR' and not self.PORTA_ABRIR):
            deadline = 12
            tempo_exec = random.randint(8, 12)
            tarefa_ = tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.escalonador.inserir_tarefa(tarefa_)
            self.PORTA_ABRIR = True
            self.ID_COUNT += 1

        elif(nome == 'PORTA_FECHAR' and not self.PORTA_FECHAR):
            deadline = 15
            tempo_exec = random.randint(10, 15)
            tarefa_ = tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.escalonador.inserir_tarefa(tarefa_)
            self.PORTA_FECHAR = True
            self.ID_COUNT += 1

        ###AR_CONDICIONADO###
        elif(nome == 'ARCOND_LIGAR' and not self.ARCOND_LIGAR):
            deadline = 18
            tempo_exec = random.randint(5, 10)
            tarefa_ = tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.escalonador.inserir_tarefa(tarefa_)
            self.ARCOND_LIGAR = True
            self.ID_COUNT += 1

        elif(nome == 'ARCOND_DESLIG' and not self.ARCOND_DESLIG):
            deadline = 18
            tempo_exec = random.randint(5, 10)
            tarefa_ = tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.escalonador.inserir_tarefa(tarefa_)
            self.ARCOND_DESLIG = True
            self.ID_COUNT += 1

        ###AQUECEDOR###
        elif(nome == 'AQUECE_LIGAR' and not self.AQUECE_LIGAR):
            deadline = 18
            tempo_exec = random.randint(5, 10)
            tarefa_ = tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.escalonador.inserir_tarefa(tarefa_)
            self.AQUECE_LIGAR = True
            self.ID_COUNT += 1

        elif(nome == 'AQUECE_DESLIG' and not self.AQUECE_DESLIG):
            deadline = 18
            tempo_exec = random.randint(5, 10)
            tarefa_ = tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.escalonador.inserir_tarefa(tarefa_)
            self.ARCOND_DESLIG = True
            self.ID_COUNT += 1

        ###LAMPADA###
        elif(nome == 'LAMPAD_LIGAR' and not self.LAMPAD_LIGAR):
            deadline = 5
            tempo_exec = random.randint(1, 3)
            tarefa_ = tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.escalonador.inserir_tarefa(tarefa_)
            self.LAMPAD_LIGAR = True
            self.ID_COUNT += 1

        elif(nome == 'LAMPAD_DESLIG' and not self.LAMPAD_DESLIG):
            deadline = 3
            tempo_exec = random.randint(1, 3)
            tarefa_ = tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.escalonador.inserir_tarefa(tarefa_)
            self.LAMPAD_DESLIG = True
            self.ID_COUNT += 1

        ###TELEVISÃO###
        elif(nome == 'TV_LIGAR' and not self.TV_LIGAR):
            deadline = 5
            tempo_exec = random.randint(1, 4)
            tarefa_ = tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.escalonador.inserir_tarefa(tarefa_)
            self.TV_LIGAR = True
            self.ID_COUNT += 1

        elif(nome == 'TV_DESLIG' and not self.TV_DESLIG):
            deadline = 3
            tempo_exec = random.randint(1, 3)
            tarefa_ = tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.escalonador.inserir_tarefa(tarefa_)
            self.TV_DESLIG = True
            self.ID_COUNT += 1

        ###ASPIRADOR DE PÓ###
        elif(nome == 'ASPIRA' and not self.ASPIRA):
            deadline = 800
            tempo_exec = random.randint(300, 400)
            tarefa_ = tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.escalonador.inserir_tarefa(tarefa_)
            self.ASPIRA = True
            self.ID_COUNT += 1

        else:
            tarefa_ = None

        return tarefa_
