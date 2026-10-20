import os
import requests
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError(
        "GEMINI_API_KEY nao encontrada."
    )

cliente = genai.Client(api_key=api_key)


def analisar_imagem(url: str):
    try:
        print("\nBaixando imagem...")
        resposta = requests.get(
            url,
            timeout=20,
            headers={"User-Agent": "SmartCamera/1.0"}
        )
        resposta.raise_for_status()

        content_type = (
            resposta.headers.get("Content-Type", "")
            .split(";")[0]
            .strip()
            .lower()
        )

        tipos_validos = {
            "image/jpeg",
            "image/jpg",
            "image/png",
            "image/webp",
            "image/gif",
            "image/bmp",
        }

        if content_type not in tipos_validos:
            print(
                f"\nErro: o endereço não retornou uma imagem válida.\n"
                f"Content-Type recebido: {content_type or 'desconhecido'}\n"
                "Use um link direto da imagem (ex: terminando em .png, .jpg, etc)."
            )
            return

        tamanho = len(resposta.content)
        if tamanho > 8 * 1024 * 1024:
            print(
                f"\nErro: a imagem é muito grande ({tamanho / 1024 / 1024:.1f} MB).\n"
                "O limite atual é 8 MB."
            )
            return

        print("Imagem baixada \nEnviando para o Gemini...\n")

        imagem = types.Part.from_bytes(
            data=resposta.content,
            mime_type=content_type
        )

        resposta_gemini = cliente.models.generate_content(
            model="gemini-3.8-flash",
            contents=[
                "Fale o que está vendo em poucas palavras (Exemplo: Um carro vermelho)"
                "Seja claro, objetivo e completo.",
                imagem
            ]
        )

        print("-------------------------------------------------")
        print("DESCRIÇÃO DA IMAGEM PELO SMART CAMERA AI + GEMINI")
        print("-------------------------------------------------")
        print(resposta_gemini.text.strip())
        print("-------------------------------------------------")

    except requests.exceptions.RequestException as e:
        print(f"\nErro ao baixar a imagem: {e}")
    except Exception as e:
        print(f"\nErro ao analisar a imagem com o Gemini: {e}")