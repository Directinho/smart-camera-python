
""" SPRINT PASSADA """
"""
==== SMARTCAMERA AI ====
 
1 - Detectar cenário automaticamente
2 - Ver histórico de fotos
3 - Sair
 
Escolha uma opção:
"""
 
# ==========================================
# HISTÓRICO DE FOTOS
# ==========================================
 
historico_foto = []
 
 
# ==========================================
# LISTA COM TODOS OS MODOS DE CÂMERA
# ==========================================
 
# ==========================================
# FUNÇÕES DOS CENÁRIOS
# ==========================================
 
def modo_pessoa():
 
    modo_retrato = True
 
    print("\n===== AJUSTE DE IA =====")
    print("- Modo Retrato ativado")
    print("- Ajuste de desfoque no fundo")
    print("- Otimização de tom de pele")
 
    print("\n===== RESULTADO =====")
    print("Foto com aparência profissional!")
 
    print(f"\nModo Retrato: {modo_retrato}")
 
 
def modo_grupo():
 
    modo_ultrawide = True
 
    print("\n===== AJUSTE DE IA =====")
    print("- Ativar lente Ultrawide")
    print("- Habilitar alinhamento de rosto")
    print("- Aplicar enquadramento automático")
 
    print("\n===== RESULTADO =====")
    print("Todos aparecem corretamente na foto!")
 
    print(f"\nModo Ultrawide: {modo_ultrawide}")
 
 
def modo_comida():
 
    modo_food = True
 
    print("\n===== AJUSTE DE IA =====")
    print("- Ativar modo comida")
    print("- Acrescentar saturação")
    print("- Aumentar nitidez")
 
    print("\n===== RESULTADO =====")
    print("Comida mais atraente na foto!")
 
    print(f"\nModo Comida: {modo_food}")
 
 
def modo_documento():
 
    modo_scanner = True
 
    print("\n===== AJUSTE DE IA =====")
    print("- Modo Scanner ativado")
    print("- Perspectiva corrigida")
    print("- Contraste aprimorado")
 
    print("\n===== RESULTADO =====")
    print("Documento legível escaneado!")
 
    print(f"\nModo Scanner: {modo_scanner}")
 
 
def modo_show():
 
    modo_noturno = True
 
    print("\n===== AJUSTE DE IA =====")
    print("- Modo Noturno ativado")
    print("- Estabilização habilitada")
    print("- Redução de ruído aplicada")
 
    print("\n===== RESULTADO =====")
    print("Melhor qualidade em ambientes escuros!")
 
    print(f"\nModo Noturno: {modo_noturno}")
 
 
def modo_animal():
 
    modo_acao = True
 
    print("\n===== AJUSTE DE IA =====")
    print("- Modo de ação ativado")
    print("- Alta velocidade de obturador")
    print("- Rastreamento de movimento ativado")
 
    print("\n===== RESULTADO =====")
    print("Menos fotos borradas!")
 
    print(f"\nModo Ação: {modo_acao}")
 
 
def modo_paisagem():
 
    modo_hdr = True
 
    print("\n===== AJUSTE DE IA =====")
    print("- HDR ativado")
    print("- Ultrawide habilitado")
    print("- Alcance dinâmico otimizado")
 
    print("\n===== RESULTADO =====")
    print("Mais detalhes na paisagem!")
 
    print(f"\nModo HDR: {modo_hdr}")
 
 
def modo_objeto():
 
    modo_macro = True
 
    print("\n===== AJUSTE DE IA =====")
    print("- Modo macro ativado")
    print("- Foco preciso ativado")
    print("- Refino de detalhes ativado")
 
    print("\n===== RESULTADO =====")
    print("Imagem detalhada do objeto!")
 
    print(f"\nModo Macro: {modo_macro}")
 
 
# ==========================================
# FUNÇÃO 1 - CONTEXTUAL CAMERA
# ==========================================
 
def contextual_camera():
 
    print("\n===== CONTEXTUAL CAMERA =====")
 
    print("Cenários possíveis:")
    print("- Pessoa")
    print("- Grupo")
    print("- Comida")
    print("- Documento")
    print("- Show")
    print("- Animal")
    print("- Paisagem")
    print("- Objeto")
 
    cenario = input("\nO cenário detectado foi: ").strip().lower()
 
    # ======================================
    # VALIDAÇÃO
    # ======================================
 
    cena_valida = [
        "pessoa",
        "grupo",
        "comida",
        "documento",
        "show",
        "animal",
        "paisagem",
        "objeto"
    ]
 
    if cenario not in cena_valida:
        print("\n[ERRO] Cena inválida detectada!")
        return
 
    # ======================================
    # HISTÓRICO
    # ======================================
 
    historico_foto.append(cenario)
 
    print(f"\nCenário detectado: {cenario}")
 
    # ======================================
    # CHAMADA DAS FUNÇÕES
    # ======================================
 
    if cenario == "pessoa":
        modo_pessoa()
 
    elif cenario == "grupo":
        modo_grupo()
 
    elif cenario == "comida":
        modo_comida()
 
    elif cenario == "documento":
        modo_documento()
 
    elif cenario == "show":
        modo_show()
 
    elif cenario == "animal":
        modo_animal()
 
    elif cenario == "paisagem":
        modo_paisagem()
 
    elif cenario == "objeto":
        modo_objeto()
 
 
# ==========================================
# FUNÇÃO 2 - HISTÓRICO
# ==========================================
 
def view_history():
 
    print("\n===== HISTÓRICO DE FOTOS =====")
 
    # Validação
    if len(historico_foto) == 0:
        print("Não há fotos registradas!")
        return
 
    # Exibir histórico
    for index, item in enumerate(historico_foto, start=1):
        print(f"{index} - {item}")
 
 
# ==========================================
# FUNÇÃO 3 - MODOS DE CÂMERA
# ==========================================
 
 
# ==========================================
# MENU PRINCIPAL
# ==========================================
 
while True:
 
    print("\n===================================")
    print("         SMARTCAMERA AI")
    print("===================================")
 
    print("1 - Detectar cenário automaticamente")
    print("2 - Ver histórico de fotos")
    print("3 - Sair")
 
    opcao = input("\nEscolha uma opção: ")
 
    # ======================================
    # VALIDAÇÃO
    # ======================================
 
    if not opcao.isdigit():
        print("\n[ERRO] Digite um número válido!")
        continue
 
    opcao = int(opcao)
 
    # ======================================
    # OPÇÕES DO MENU
    # ======================================
 
    if opcao == 1:
        contextual_camera()
 
    elif opcao == 2:
        view_history()
 
    elif opcao == 3:
        print("\nFechando SmartCamera AI...")
        print("Obrigado por utilizar o sistema!")
        break
 
    else:
        print("\n[ERRO] Opção inválida!")