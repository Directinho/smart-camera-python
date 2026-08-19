import subprocess
import sys



grupo = ["João Vitor", "Milenna de Moraes", "Henrique Luiz", "Gabriela do Rozario", "Lucas Salvador"]

erro = "Opção desconhecida"


def opcao1():

    try:

        subprocess.run([sys.executable, "assets/smart.py"])

    except FileNotFoundError:

        print("Erro ao abrir")

def opcao2():

    try:

        subprocess.run([sys.executable, "./assets/cronograma.py"])

    except FileNotFoundError:

        print("Erro ao abrir")

""" Inicio do loop """

def opcoes():
    while True:
        print("\nSmartCamera AI\n\n1 - SmartCamera BETA\n2 - Opção 2\n3 - Ver Grupo\n4 - Sair do Sistema")
        opcao = input("Insira o valor: ")
        if opcao == "1":
            print("\nopcao 1 escolhida!\n")
            opcao1()
            break
            
        elif opcao == "2":
            print("\nopcao 2 escolhida\n")
            opcao2()
        elif opcao == "3":
            print(grupo)    

        elif opcao == "4":
            print("Fechando programa")
            break

        else:
            print(erro)



opcoes()