# from dicionario import modos, modo_pessoa, modo_objeto, modo_paisagem, modo_animal, modo_comida, modo_documento, modo_evento, modo_grupo

print("SMART SELECIONADO\n\nAPP CAMERA CARREGADO")
"""
Dicionarios
"""

fotos = 0
pessoa = False
pessoas = 0
documento = False
show = False
animal = False
comida = False


def tirar_foto(fotos):
    fotos += 1
    print("📸 Foto tirada!")
    return fotos


def add_pessoa(pessoa, pessoas):
    pessoas += 1
    pessoa = True
    print(f"--🙍 PESSOA ADICIONADA COM SUCESSO\nQuantidade de Pessoas: {pessoas}\nPossui pessoas na camera? {pessoa}")


def rem_pessoa(pessoa, pessoas):
    if pessoas > 0:
        pessoas -= 1
        if pessoas == 0:
            pessoa == False
        print(f"➖🙍 PESSOA REMOVIDA COM SUCESSO\nQuantidade de Pessoas: {pessoas}")
    else:
        print("Não há pessoas para remover.")


def add_documento(documento):
    documento = True
    print(f"📃 DOCUMENTO ADICIONADO COM SUCESSO\nDocumento = {documento}")


def rem_documento(documento):
    documento = False
    print(f"DOCUMENTO REMOVIDO COM SUCESSO\nDocumento: {documento}")


def ir_show(show):
    show = True
    print(f"VIAGEM PARA O SHOW COM SUCESSO\nShow: {show}")


def sair_show(show):
    show = False
    print(f"VOCÊ SAIU DO SHOW COM SUCESSO\nShow?: {show}")


def add_animal(animal):
    animal = True
    print(f"ANIMAL ADICIONADO COM SUCESSO\nAnimais?: {animal}")


def rem_animal(animal):
    animal = False
    print(f"ANIMAL REMOVIDO COM SUCESSO\nAnimais?: {animal}")


def add_comida(comida):
    comida = True
    print(f"MAÇÃ ADICIONADA COM SUCESSO\nComidas?: {comida}")


def rem_comida(comida):
    comida = False
    print(f"MAÇÃ REMOVIDA COM SUCESSO\nComidas?: {comida}")


def galeria(fotos):
    print(f"Quantidade de fotos: {fotos}")


def smart():
    while True:
        print("SmartCamera AI\n📷1 - Tirar foto\n-- 🕹️ CONTROLE DE SUJEITOS NO AMBIENTE:--\n🙍2 - Inserir uma Pessoa\n🙍2. - Remover uma Pessoa\n📃3- Inserir um Documento Escrito\n📃3.- Remover Documento\n🎸4- Viajar para um Show\n🎸4.- Sair do Show\n🐕5 - Inserir um Cachorro\n🐕5. - Remover Cachorro\n🍎6- Inserir uma maçã\n🍎6. - Remover Maçã\n🗺️7- Galeria do Celular\n❌0 - Encerrar Programa")
        opcao = input("Controle: ").strip()
        if opcao == "1": # Tirar foto
            tirar_foto(fotos)
        elif opcao == "2": # Adicionar pessoa
            add_pessoa(pessoa, pessoas)
        elif opcao == "2.":
            rem_pessoa(pessoa, pessoas)
        elif opcao == "3":
            add_documento(documento)
        elif opcao == "3.":
            rem_documento(documento)
        elif opcao == "4":
            ir_show(show)
        elif opcao == "4.":
            sair_show(show)
        elif opcao == "5":
            add_animal(animal)
        elif opcao == "5.":
            rem_animal(animal)
        elif opcao == "6":
            add_comida(comida)
        elif opcao == "6.":
            rem_comida(comida)
        elif opcao == "7":
            galeria(fotos)
        elif opcao == "0":
            print("fechando programa")
            break
        else:
            print("Opção inválida. Tente novamente.")


smart()