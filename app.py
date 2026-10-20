import sys
import subprocess
from configuracoes import *
from main import limpar, continuar
import cv2 
import numpy as np
import matplotlib.pyplot as plt
from urllib.parse import urlparse # Para checar o URL

dominio = { "i.imgur.com", "imgur.com", "iili.io"}
limpar()
print("SMART CAMERA INICIADA\n")


def ai(): 
    pass
def ajuda():
    limpar()
    print("Este projeto utilizamos a biblioteca OpenCV para analisar a imagem enviada\npara testar é preciso enviar uma imagem para um banco de dados de imagens como imgur\ne freeimagehost quando mandar a imagem clique no botao direito e copiar URL normalmente eles\nseguem um padrão como por exemplo:\nImgur tem um url inicial padrão: https://i.imgur.com/snWXh....\nFreeimagehost tem o padrão de URL: https://iili.io/nap....\n")
    continuar()
    smart()

def imagens():
    limpar()
    print("")
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

    
    return url
def smart():
    limpar()
    print("🖼️Insira uma imagem para ser analisada🖼️\n\n-- Recomendado URL hosts --\nhttps://imgur.com - https://freeimage.host/\n\nse precisar de ajuda digite: ajuda\nuse as imagens exemplos digitando: imagem\nse quiser sair digite: \n")
    url = input("Insira o URL da Imagem: ").lower()

    if url == "ajuda":
        ajuda()
    elif url == "imagem":
        imagens()
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
