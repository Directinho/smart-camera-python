import subprocess
import sys



grupo = ["João Vitor", "Milenna de Moraes", "Henrique Luiz", "Gabriela do Rozario", "Lucas Salvador"]

erro = "Opção desconhecida"


def opcao1():

    try:

        subprocess.run([sys.executable, "smart.py"], cwd="assets")

    except Exception:

        print("Erro ao abrir")


# Inicio do loop 

def opcoes():
    while True:
        print("\nSmartCamera AI\n1 - SmartCamera BETA\n2- Ver Grupo\n3- Sair do Sistema")
        opcao = input("Insira o valor: ")
        if opcao == "1":
            print("\nopcao 1 escolhida!\n")
            opcao1()
            
        elif opcao == "2":
            print(grupo)    

        elif opcao == "3":
            print("Fechando programa")
            break

        else:
            print(erro)



opcoes()