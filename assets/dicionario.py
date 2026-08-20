modos = {
    "modos_smart": [
        {"id": 1, "modo": "pessoa"},
        {"id": 2, "modo": "grupo"},
        {"id": 3, "modo": "documento"},
        {"id": 4, "modo": "evento"},
        {"id": 5, "modo": "paisagem"},
        {"id": 6, "modo": "comida"},
        {"id": 7, "modo": "animal"},
        {"id": 8, "modo": "objeto"}  # adicionei porque você criou o dicionário
    ]
}

modo_pessoa = {
    "retrato": {
        "modo": "retrato",
        "sobre": "Ativa o modo retrato da câmera",
        "config": [
            {"id": 1, "opcao": "Modo Retrato Ativado", "ativo": False},
            {"id": 2, "opcao": "Ajuste de desfoque no fundo", "ativo": False},
            {"id": 3, "opcao": "Otimização de tom de pele", "ativo": False}
        ],
        "valor": False,
        "log": "Smart Camera reconheceu uma Pessoa"
    }
}

modo_grupo = {
    "ultrawide": {
        "modo": "ultrawide",
        "sobre": "Ativa o modo ultrawide da câmera",
        "config": [
            {"id": 1, "opcao": "Ativar lente Ultrawide", "ativo": False},
            {"id": 2, "opcao": "Habilitar alinhamento de rosto", "ativo": False},
            {"id": 3, "opcao": "Aplicar enquadramento automático", "ativo": False}
        ],
        "valor": False,
        "log": "Smart Camera reconheceu um Grupo"
    }
}

modo_documento = {
    "scanner": {
        "modo": "scanner",
        "sobre": "Ativa o modo scanner da câmera",
        "config": [
            {"id": 1, "opcao": "Modo Scanner ativado", "ativo": False},
            {"id": 2, "opcao": "Perspectiva corrigida", "ativo": False},
            {"id": 3, "opcao": "Contraste aprimorado", "ativo": False}
        ],
        "valor": False,
        "log": "Smart Camera reconheceu um documento"
    }
}

modo_evento = {
    "noturno": {
        "modo": "noturno",
        "sobre": "Ativa o modo noturno da câmera",
        "config": [
            {"id": 1, "opcao": "Modo Noturno ativado", "ativo": False},
            {"id": 2, "opcao": "Estabilização habilitada", "ativo": False},
            {"id": 3, "opcao": "Redução de ruído aplicada", "ativo": False}
        ],
        "valor": False,
        "log": "Smart Camera reconheceu que o usuário está em um evento ou show"
    }
}

modo_paisagem = {
    "hdr": {
        "modo": "hdr",
        "sobre": "Ativa o modo HDR da câmera",
        "config": [
            {"id": 1, "opcao": "HDR Ativado", "ativo": False},
            {"id": 2, "opcao": "Ultrawide habilitado", "ativo": False},
            {"id": 3, "opcao": "Alcance dinâmico otimizado", "ativo": False}
        ],
        "valor": False,
        "log": "Smart Camera reconheceu que o usuário está em um local aberto / paisagem"
    }
}

modo_objeto = {
    "macro": {
        "modo": "macro",
        "sobre": "Ativa o modo macro da câmera",
        "config": [
            {"id": 1, "opcao": "Modo macro ativado", "ativo": False},
            {"id": 2, "opcao": "Foco preciso ativado", "ativo": False},
            {"id": 3, "opcao": "Refino de detalhes ativado", "ativo": False}
        ],
        "valor": False,
        "log": "Smart Camera reconheceu um objeto"
    }
}

modo_comida = {
    "food": {
        "modo": "food",
        "sobre": "Ativa o modo comida da câmera",
        "config": [
            {"id": 1, "opcao": "Ativar modo comida", "ativo": False},
            {"id": 2, "opcao": "Acrescentar saturação", "ativo": False},
            {"id": 3, "opcao": "Aumentar nitidez", "ativo": False}
        ],
        "valor": False,
        "log": "Smart Camera reconheceu um alimento"
    }
}

modo_animal = {
    "animal": {
        "modo": "animal",
        "sobre": "Ativa o modo animal da câmera",
        "config": [
            {"id": 1, "opcao": "Modo de ação ativado", "ativo": False},
            {"id": 2, "opcao": "Alta velocidade de obturador", "ativo": False},
            {"id": 3, "opcao": "Rastreamento de movimento ativado", "ativo": False}
        ],
        "valor": False,
        "log": "Smart Camera reconheceu um animal"
    }
}