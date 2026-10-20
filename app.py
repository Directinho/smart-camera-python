import sys
import subprocess
from main import limpar, continuar
import numpy as np
import matplotlib.pyplot as plt
from ai import analisar_imagem
from PIL import Image
from urllib.parse import urlparse # Para checar o URL

url = str("")
dominio = { "i.imgur.com", "imgur.com", "iili.io"}
imagem1 = "https://i.imgur.com/ePksvoq.png"
imagem2 = "https://i.imgur.com/fjJI94N.png"

limpar()
print("SMART CAMERA INICIADA\n")

def ai(url):
    limpar()
    print("SMART CAMERA AI")
    print("Analisando imagem com o Gemini...\n")
    analisar_imagem(url)
    continuar()
    smart()


def ajuda():
    limpar()
    print(
        "Este projeto utiliza a API do Google Gemini para analisar imagens.\n"
        "Para testar é preciso enviar uma imagem hospedada no Imgur ou Freeimage.host.\n"
        "Quando mandar a imagem, clique com o botão direito e copie o URL direto da imagem.\n\n"
        "Exemplos de padrões de URL:\n"
        "• Imgur: https://i.imgur.com/snWXh....\n"
        "• Freeimage.host: https://iili.io/nap....\n"
    )
    continuar()
    smart()


def imagens():
    limpar()
    print(
        "As imagens exemplos funcionam ao você digitar na entrada de URL\n"
        "os números de cada imagem, ou você pode apenas copiar o URL:\n\n"
        f"1 - Pato Com Óculos: {imagem1}\n"
        f"2 - Notebook: {imagem2}\n"
    )
    continuar()
    smart()

def checar(url):
    if not url or not isinstance(url, str):
        raise ValueError("A URL enviada não é dos dominios Imgur nem freeimage, tente novamente")
    url = url.strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    parsed = urlparse(url)
    nomehost = (parsed.hostname or "").lower()
    is_imgur = any(
nomehost == d or nomehost.endswith("." + d)
for d in dominio
    )
    if not is_imgur:
        limpar()
        print("URL não identificado nos Dominios, tente:\n https://imgur.com/ ou https://freeimage.host/")
        continuar()
        smart()
    else: 
        ai(url)
    
    return url
def smart():
    limpar()
    print("🖼️Insira uma imagem para ser analisada🖼️\n\n-- Recomendado URL hosts --\nhttps://imgur.com - https://freeimage.host/\n\nse precisar de ajuda digite: ajuda\nuse as imagens exemplos digitando: imagem\nse quiser sair digite: \n")
    url = input("Insira o URL da Imagem: ").lower()

    if url == "ajuda":
        ajuda()
    elif url == "imagem":
        imagens()
    elif url == "1":
        url = imagem1
        checar(url)
    elif url == "2":
        url = imagem2
        checar(url)
    elif url == "sair":
        limpar()
        app()
    
    else:
        checar(url)
def saiba_mais():
    pass
def voltar_menu():
    try:
        subprocess.run([sys.executable, "main.py"])
    except Exception:

        print("Erro ao abrir")



def app():
    print("SMARTCAMERA AI\n1- Iniciar Smart Camera AI\n2 - Saiba Mais\n3 - Voltar para o Menu Principal\n4 - Fechar programa")
    opcao = input("Insira uma opção: ")
    if opcao == "1":
        smart()
    elif opcao == "2":
        saiba_mais()
    elif opcao == "3":
        limpar()
        print("MENU PRINCIPAL INICIADO")
        voltar_menu()
    elif opcao == "4":
        limpar()
        print("Fechando Programa")
    else:
        print("Opção inválida")
        continuar()
        app()
if __name__ == '__main__':
    app()
