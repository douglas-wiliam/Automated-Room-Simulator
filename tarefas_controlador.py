#Módulo de controle de tarefas da IA.
import random
class _tarefa(object):
    def __init__(self, nome, n_id, deadline, tempo_exec):
        self.nome = nome
        self.id = n_id
        self.deadline = deadline
        self.tempo_exec = tempo_exec

class escalonador():
    #Fazer escalonador algoritmo EDF.
    def __init__(self):
        return None

class controle_tarefas():
    def __init__(self):
        self.ID_COUNT = 0

        #Flags para verificar as tarefas já existentes na fila.
        #As flags são setadas novamente para falta quando elas saírem da fila.
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

        self.lista_tarefas = list()

    def cria_tarefa(self, nome):

        ###JANELA###
        if(nome == 'JANELA_ABRIR' and not self.JANELA_ABRIR):
            deadline = 0
            tempo_exec = random.randint(5,25)
            tarefa = _tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.lista_tarefas.append(tarefa)
            self.JANELA_ABRIR = True
            print('JANELA_ABRIR')
            self.ID_COUNT += 1

        if(nome == 'JANELA_FECHAR' and not self.JANELA_FECHAR):
            deadline = 0
            tempo_exec = random.randint(5,25)
            tarefa = _tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.lista_tarefas.append(tarefa)
            self.JANELA_FECHAR = True
            print('JANELA_FECHAR')
            self.ID_COUNT += 1

        ###PORTA###
        if(nome == 'PORTA_ABRIR' and not self.PORTA_ABRIR):
            deadline = 3
            tempo_exec = random.randint(25,35)
            tarefa = _tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.lista_tarefas.append(tarefa)
            self.PORTA_ABRIR = True
            print('PORTA_ABRIR')
            self.ID_COUNT += 1

        if(nome == 'PORTA_FECHAR' and not self.PORTA_FECHAR):
            deadline = 3
            tempo_exec = random.randint(25,35)
            tarefa = _tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.lista_tarefas.append(tarefa)
            self.PORTA_FECHAR = True
            print('FECHAR_PORTA')
            self.ID_COUNT += 1

        ###AR_CONDICIONADO###
        if(nome == 'ARCOND_LIGAR' and not self.ARCOND_LIGAR):
            deadline = 2
            tempo_exec = random.randint(5,10)
            tarefa = _tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.lista_tarefas.append(tarefa)
            self.ARCOND_LIGAR = True
            print('ARCOND_LIGAR')
            self.ID_COUNT += 1

        if(nome == 'ARCOND_DESLIG' and not self.ARCOND_DESLIG):
            deadline = 2
            tempo_exec = random.randint(5,10)
            tarefa = _tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.lista_tarefas.append(tarefa)
            self.ARCOND_DESLIG = True
            print('ARCOND_DESLIG')
            self.ID_COUNT += 1

        ###AQUECEDOR###
        if(nome == 'AQUECE_LIGAR' and not self.AQUECE_LIGAR):
            deadline = 2
            tempo_exec = random.randint(10,20)
            tarefa = _tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.lista_tarefas.append(tarefa)
            self.AQUECE_LIGAR = True
            print('AQUECE_LIGAR')
            self.ID_COUNT += 1

        if(nome == 'AQUECE_DESLIG' and not self.AQUECE_DESLIG):
            deadline = 2
            tempo_exec = random.randint(10,20)
            tarefa = _tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.lista_tarefas.append(tarefa)
            self.ARCOND_DESLIG = True
            print('AQUECE_DESLIG')
            self.ID_COUNT += 1

        ###LAMPADA###
        if(nome == 'LAMPAD_LIGAR' and not self.LAMPAD_LIGAR):
            deadline = 2
            tempo_exec = random.randint(3,5)
            tarefa = _tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.lista_tarefas.append(tarefa)
            self.LAMPAD_LIGAR = True
            print('LAMPAD_LIGAR')
            self.ID_COUNT += 1

        if(nome == 'LAMPAD_DESLIG' and not self.LAMPAD_DESLIG):
            deadline = 2
            tempo_exec = random.randint(3,5)
            tarefa = _tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.lista_tarefas.append(tarefa)
            self.LAMPAD_DESLIG = True
            print('LAMPAD_DESLIG')
            self.ID_COUNT += 1

        ###LAMPADA###
        if(nome == 'TV_LIGAR' and not self.TV_LIGAR):
            deadline = 2
            tempo_exec = random.randint(3,5)
            tarefa = tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.lista_tarefas.append(tarefa)
            self.TV_LIGAR = True
            print('TV_LIGAR')
            self.ID_COUNT += 1
            

        if(nome == 'TV_DESLIG' and not self.TV_DESLIG):
            deadline = 2
            tempo_exec = random.randint(3,5)
            tarefa = tarefa(nome, self.ID_COUNT, deadline, tempo_exec)
            self.lista_tarefas.append(tarefa)
            self.TV_DESLIG = True
            print('TV_DESLIG')
            self.ID_COUNT += 1

        else:
            tarefa = None

        return tarefa