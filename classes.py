class ToDoList:
    def __init__(self):
        self.tarefas = {}

    def adiconar_tarefa (self, indice, descricao):
        self.indice = indice
        self.descricao = descricao
        self.tarefas[self.indice] = [self.descricao]

    def excluir_tarefa (self, indice):
        self.indice = indice
        for indice in self.tarefas.items():
            del self.tarefas[self.indice]
            print ("Tarefa excluída")
    
    def listar_tarefas(self):
        for chave,valor in self.tarefas.items():
            print (f"{chave} - Tarefa: {valor [0]}")

