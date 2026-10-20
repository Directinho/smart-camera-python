import subprocess
import sys
import os


grupo = ["João Vitor", "Milenna de Moraes", "Henrique Luiz", "Gabriela do Rozario", "Lucas Salvador"]

erro = "Opção desconhecida"


def opcao1():

    try:

        subprocess.run([sys.executable, "smart.py"], cwd="assets")

    except Exception:

        print("Erro ao abrir")

def opcao2():
    try:
        subprocess.run([sys.executable, "app.py"])
    except Exception:
        print("Erro ao abrir")
def integrantes():
    print("João Vitor\nMilenna de Moraes\nHenrique Luiz\nGabriela de Rozario\nLucas Salvador\n")
    continuar()
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')
def continuar():
    input("Aperte qualquer tecla para voltar")
    limpar()
    return
# Inicio do loop 
def opcoes():
    limpar()
    print("\nSmartCamera AI\n1 - SmartCamera BETA\n2- SmartCamera AI\n3- Ver Grupo\n4- Sair do Sistema")
    opcao = input("Insira o valor: ")
    if opcao == "1":  
        opcao1()
    elif opcao == "2":
        opcao2()
    elif opcao == "3":
        limpar()
        integrantes()

    elif opcao == "4":
        limpar()
        print("Fechando programa")

    else:
        print(erro)



if __name__ == '__main__':
    opcoes()
