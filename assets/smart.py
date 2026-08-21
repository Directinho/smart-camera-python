from dicionario import (
    modos,
    modo_pessoa,
    modo_grupo,
    modo_documento,
    modo_evento,
    modo_paisagem,
    modo_objeto,
    modo_comida,
    modo_animal
)

print("SMART SELECIONADO")

def tirar_foto(fotos):
    fotos += 1
    print("📸 Foto tirada com sucesso!")
    return fotos


def modo_log_ativado(modo_dict):
    for chave in modo_dict:
        modo = modo_dict[chave]
        modo["valor"] = True
        for config in modo["config"]:
            config["ativo"] = True

        print(f"\n✅ {modo['log']}")
        print(f"   → {modo['sobre']}")
        for cfg in modo["config"]:
            status = "Ativado" if cfg["ativo"] else "Desativado"
            print(f"     • {cfg['opcao']}: {status}")
    return modo_dict


def modo_log_desativado(modo_dict):
    for chave in modo_dict:
        modo = modo_dict[chave]
        modo["valor"] = False
        for config in modo["config"]:
            config["ativo"] = False
        print(f"\n❌ Modo {modo['modo']} desativado")
    return modo_dict


def add_pessoa(pessoa, pessoas, modo_pessoa):
    pessoas += 1
    pessoa = True
    print(f"--🙍 PESSOA ADICIONADA COM SUCESSO\nQuantidade de Pessoas: {pessoas}\nPossui pessoas na camera? {pessoa}")
    modo_pessoa = modo_log_ativado(modo_pessoa)
    return pessoa, pessoas, modo_pessoa


def rem_pessoa(pessoa, pessoas, modo_pessoa):
    if pessoas > 0:
        pessoas -= 1
        print(f"\n➖ Pessoa removida com sucesso!")
        print(f"   Quantidade de pessoas: {pessoas}")
        if pessoas == 0:
            pessoa = False
            modo_pessoa = modo_log_desativado(modo_pessoa)
    else:
        print("\nJá não tem pessoas")
    return pessoa, pessoas, modo_pessoa


def add_documento(documento, modo_documento):
    documento = True
    print(f"📃 DOCUMENTO ADICIONADO COM SUCESSO\nDocumento = {documento}")
    modo_documento = modo_log_ativado(modo_documento)
    return documento, modo_documento


def rem_documento(documento, modo_documento):
    if documento:
        documento = False
        print(f"DOCUMENTO REMOVIDO COM SUCESSO\nDocumento: {documento}")
        modo_documento = modo_log_desativado(modo_documento)
    else:
        print("\n⚠️  Não há documento para remover.")
    return documento, modo_documento


def ir_show(show, modo_evento):
    show = True
    print(f"VIAGEM PARA O SHOW COM SUCESSO\nShow: {show}")
    modo_evento = modo_log_ativado(modo_evento)
    return show, modo_evento


def sair_show(show, modo_evento):
    if show:
        show = False
        print(f"VOCÊ SAIU DO SHOW COM SUCESSO\nShow?: {show}")
        modo_evento = modo_log_desativado(modo_evento)
    else:
        print("\n⚠️  Você não está em um show.")
    return show, modo_evento


def add_animal(animal, modo_animal):
    animal = True
    print(f"ANIMAL ADICIONADO COM SUCESSO\nAnimais?: {animal}")
    modo_animal = modo_log_ativado(modo_animal)
    return animal, modo_animal


def rem_animal(animal, modo_animal):
    if animal:
        animal = False
        print(f"ANIMAL REMOVIDO COM SUCESSO\nAnimais?: {animal}")
        modo_animal = modo_log_desativado(modo_animal)
    else:
        print("\n⚠️  Não há animal para remover.")
    return animal, modo_animal


def add_comida(comida, modo_comida):
    comida = True
    print(f"MAÇÃ ADICIONADA COM SUCESSO\nComidas?: {comida}")
    modo_comida = modo_log_ativado(modo_comida)
    return comida, modo_comida


def rem_comida(comida, modo_comida):
    if comida:
        comida = False
        print(f"MAÇÃ REMOVIDA COM SUCESSO\nComidas?: {comida}")
        modo_comida = modo_log_desativado(modo_comida)
    else:
        print("\n⚠️  Não tem comida para ser removida")
    return comida, modo_comida


def galeria(fotos):
    print(f"\n🗺️  Galeria do celular")
    print(f"   Total de fotos: {fotos}")


def smart():
    fotos = 0
    pessoa = False
    pessoas = 0
    documento = False
    show = False
    animal = False
    comida = False

    while True:
        print("SmartCamera AI\n📷1 - Tirar foto\n-- 🕹️ CONTROLE DE SUJEITOS NO AMBIENTE:--\n🙍2 - Inserir uma Pessoa\n🙍2. - Remover uma Pessoa\n📃3- Inserir um Documento Escrito\n📃3.- Remover Documento\n🎸4- Viajar para um Show\n🎸4.- Sair do Show\n🐕5 - Inserir um Cachorro\n🐕5. - Remover Cachorro\n🍎6- Inserir uma maçã\n🍎6. - Remover Maçã\n🗺️7- Galeria do Celular\n❌0 - Encerrar Programa")

        try:
            opcao = input("🕹️Controle: ").strip()

            if opcao == "1":
                fotos = tirar_foto(fotos)

            elif opcao == "2":
                pessoa, pessoas, modo_pessoa = add_pessoa(pessoa, pessoas, modo_pessoa)

            elif opcao == "2.":
                pessoa, pessoas, modo_pessoa = rem_pessoa(pessoa, pessoas, modo_pessoa)

            elif opcao == "3":
                documento, modo_documento = add_documento(documento, modo_documento)

            elif opcao == "3.":
                documento, modo_documento = rem_documento(documento, modo_documento)

            elif opcao == "4":
                show, modo_evento = ir_show(show, modo_evento)

            elif opcao == "4.":
                show, modo_evento = sair_show(show, modo_evento)

            elif opcao == "5":
                animal, modo_animal = add_animal(animal, modo_animal)

            elif opcao == "5.":
                animal, modo_animal = rem_animal(animal, modo_animal)

            elif opcao == "6":
                comida, modo_comida = add_comida(comida, modo_comida)

            elif opcao == "6.":
                comida, modo_comida = rem_comida(comida, modo_comida)

            elif opcao == "7":
                galeria(fotos)

            elif opcao == "0":
                print("\nPrograma fechado!")
                break

            else:
                print("\n❌ Opção não reconhecida")

        except Exception as e:
            print(f"\n⚠️  Erro: {e}")
            print("Tente novamente")

        input("\nclique no  enter para voltar ao menu")


smart()

smart()