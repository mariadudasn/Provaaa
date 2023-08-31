from classes import *
import os

def main ():
    contTarefas = 0
    lista = ToDoList() 

    sair = False
    while sair == False:
        try:
            os.system ("cls")
            print("---MENU - ToDoList---")
            print("01 - ADICIONAR TAREFAS")
            print("02 - EXCLUIR TAREFAS")
            print("03 - LISTAR TAREFAS")
            print("00 - SAIR")
            print("--------")
            print (" ")

            print ("Qual opção deseja?")
            menu = int(input(">> "))
            os.system ("pause")

            match menu:
                case 1:
                    os.system ("cls")
                    print ("---ADICIONAR TAREFAS---")
                    contTarefas += 1
                    indice = contTarefas
                    descricao = input ("Qual é a tarefa? - ")

                    lista.adiconar_tarefa(indice, descricao)
                    print ("Tarefa adicionada")
                    os.system ("pause")

                case 2:
                    os.system("cls")
                    print ("---LISTA DE TAREFAS---")
                    lista.listar_tarefas()
                    os.system ("pause")
                    indice = int(input("Qual tarefa deseja excluir? Digite o indice: \n >> "))
                    lista.excluir_tarefa(indice)
                    os.system ("pause")

                case 3:
                    os.system("cls")
                    print ("---LISTA DE TAREFAS---")
                    lista.listar_tarefas()
                    os.system ("pause")

                case 0:
                    print ("SAINDO...")
                    print ("------")
                    sair = True

                case _:
                    print("Valor inválido")
                    print ("-------")

        except Exception:
            print ("Valor inválido")
            print(" ")
            os.system("pause")