from texttable import Texttable
import datetime

class tabela_ambiente():
    def __init__(self, ambiente):
        self.ambiente = ambiente
        self.table = Texttable()

    def print_table(self, global_time):
        self.table.reset()
        self.table.set_deco(Texttable.HEADER)
        self.table.set_cols_dtype(['t',  # text
                              't',  # float 
                            ])
        self.table.set_cols_align(["l", "r"])
 
        self.table.add_rows([["Informações do ambiente", ""],
                       ["Hora: ", str(datetime.timedelta(seconds=global_time))],
                       ["Temperatura: ", str(round(self.ambiente.temperatura, 2))],
                       ["Chuva: ", str(self.ambiente.chuva)],
                       ["Tempo: ", str(self.ambiente.tempo)],
                       [" ", " "],
                       ["Último movimento foi há: ", str(datetime.timedelta(seconds=self.ambiente.mov_count))],
                       ["Ar condicionado: ", str(self.ambiente.ar_condicionado)],
                       ["Aquecedor: ", str(self.ambiente.aquecedor)],
                       ["Lâmpada: ", str(self.ambiente.lampada)],
                       ["Porta: ", str(self.ambiente.porta)],
                       ["Janela: ", str(self.ambiente.ar_condicionado)],
                       ["Televisão: ", str(self.ambiente.televisão)]])
        
        print(self.table.draw())

class tabela_tarefas():
    def __init__(self, lista_tarefas):
        self.lista = lista_tarefas
        self.table = Texttable()

    def print_table(self):
        self.table.reset()
        self.table.set_deco(Texttable.HEADER)
        self.table.set_cols_dtype(['t',  # text
                              't',  # text
                              't', #text
                              't'  #text            
                            ])
        self.table.set_cols_align(["c", "c", "c", "c"])
 
        self.table.add_rows([["Fila de tarefas", "", "", ""],
                            ["ID: ", "Nome: ", "Deadline: ", "T. Execução: "]]
                            )
        for tarefa in self.lista:
            self.table.add_row([str(tarefa.id), str(tarefa.nome), str(tarefa.deadline), str(tarefa.tempo_exec)])

        print(self.table.draw())