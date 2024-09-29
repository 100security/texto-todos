# 100SECURITY
# Converter Texto <> Todos os Formatos
# Por: Marcos Henrique
# Site: www.100security.com.br

import os
import re
import unicodedata
import base64
import binascii
from barcode.codex import Code128
from barcode.writer import ImageWriter
from pyzbar.pyzbar import decode
from PIL import Image
from colorama import Fore, Style

# Limpar a Tela
def clear_screen():
    if os.name == 'nt':  # Se for Windows
        os.system('cls')
    else:  # Se for Linux ou macOS
        os.system('clear')

clear_screen()

# Inicializa o Colorama
from colorama import init
init(autoreset=True)

# Banner
projeto = f"{Style.BRIGHT}{Fore.YELLOW}# - - - - - - - - 100SECURITY - - - - - - - - #\n"
titulo = f"{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Conversor de Texto para Vários Formatos"
github = f"{Fore.WHITE}github.com/100security/{Style.BRIGHT}{Fore.LIGHTCYAN_EX}texto-todos"
instagram = f"{Style.BRIGHT}{Fore.WHITE}Instagram: {Fore.WHITE}{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}@100security"

# Exibe o texto com as cores e com uma nova linha entre eles
print(f"{projeto}\n{titulo}\n{github}\n{instagram}")

# Funções de Conversão

# ASCII - Converte texto para ASCII
def text_to_ascii(text):
    ascii_values = [ord(character) for character in text]
    return ' '.join(map(str, ascii_values))

# Base64 - Converte texto para Base64
def text_to_base64(text):
    message_bytes = text.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode('utf-8')

# Binary - Converte texto para binário
def text_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)

# Braille - Dicionário de Braille e função de conversão
BRAILLE_CODE_DICT = {
    'A': '⠁', 'B': '⠃', 'C': '⠉', 'D': '⠙', 'E': '⠑', 'F': '⠋',
    'G': '⠛', 'H': '⠓', 'I': '⠊', 'J': '⠚', 'K': '⠅', 'L': '⠇',
    'M': '⠍', 'N': '⠝', 'O': '⠕', 'P': '⠏', 'Q': '⠟', 'R': '⠗',
    'S': '⠎', 'T': '⠞', 'U': '⠥', 'V': '⠧', 'W': '⠺', 'X': '⠭',
    'Y': '⠽', 'Z': '⠵', '1': '⠼⠁', '2': '⠼⠃', '3': '⠼⠉',
    '4': '⠼⠙', '5': '⠼⠑', '6': '⠼⠋', '7': '⠼⠛', '8': '⠼⠓',
    '9': '⠼⠊', '0': '⠼⠚', ' ': '⠶'
}
def text_to_braille(text):
    text = text.upper()
    return ''.join(BRAILLE_CODE_DICT.get(char, '') for char in text)

# Emojis - Dicionário de Emojis e função de conversão
EMOJI_CODE_DICT = {
    'A': '😀', 'B': '😃', 'C': '😄', 'D': '😁', 'E': '😆', 'F': '😅',
    'G': '😂', 'H': '🤣', 'I': '😊', 'J': '😇', 'K': '🙂', 'L': '🙃',
    'M': '😉', 'N': '😌', 'O': '😍', 'P': '🥰', 'Q': '😘', 'R': '😗',
    'S': '😙', 'T': '😚', 'U': '😋', 'V': '😛', 'W': '😝', 'X': '😜',
    'Y': '🤪', 'Z': '🤩', '1': '1️⃣', '2': '2️⃣', '3': '3️⃣', '4': '4️⃣',
    '5': '5️⃣', '6': '6️⃣', '7': '7️⃣', '8': '8️⃣', '9': '9️⃣', '0': '0️⃣',
    ' ': '⬜'
}
def text_to_emoji(text):
    text = text.upper()
    return ''.join(EMOJI_CODE_DICT.get(char, '') for char in text)

# Morse - Dicionário de Morse e função de conversão
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': '/'
}
def text_to_morse(text):
    text = text.upper()
    return ' '.join(MORSE_CODE_DICT.get(char, '') for char in text)

# Funções de Código de Barras

# Função para remover acentos e caracteres não suportados
def remover_acentos_e_caracteres_especiais(text):
    normalized_text = unicodedata.normalize('NFKD', text)
    text_sem_acentos = re.sub(r'[^\w\s]', '', normalized_text)
    text_substituido = text_sem_acentos.replace(' ', '_')
    return text_substituido

# Função para gerar código de barras
def gerar_codigo_de_barras(text, output_image):
    try:
        text_limpo = remover_acentos_e_caracteres_especiais(text)
        if not text_limpo:
            raise ValueError("O texto inserido não contém caracteres válidos para Code 128.")
        
        writer = ImageWriter()
        writer.text = ''  # Remove o texto legível do código de barras
        writer_options = {'write_text': False}
        
        codigo_de_barras = Code128(text_limpo, writer=writer)
        codigo_de_barras.save(output_image, options=writer_options)
        print(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}Código de barras salvo como {output_image}.png")
    
    except ValueError as ve:
        print(f"{Style.BRIGHT}{Fore.RED}Erro: {ve}")
    
    except Exception as e:
        print(f"{Style.BRIGHT}{Fore.RED}Erro ao gerar código de barras: {e}")

# Função para ler código de barras de uma imagem
def ler_codigo_de_barras(image_path):
    try:
        img = Image.open(image_path)
        decoded_objects = decode(img)
        if decoded_objects:
            for obj in decoded_objects:
                decoded_text = obj.data.decode('utf-8').replace('_', ' ')
                print(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}Código de Barras detectado: {decoded_text}")
                salvar_em_arquivo('codbarras.txt', decoded_text)
        else:
            print(f"{Style.BRIGHT}{Fore.RED}Nenhum código de barras detectado na imagem.")
    except Exception as e:
        print(f"{Style.BRIGHT}{Fore.RED}Erro ao ler código de barras: {e}")

# Função para salvar o conteúdo em um arquivo
def salvar_em_arquivo(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}Resultado salvo em {file_name}")

# Função para exibir o menu
def exibir_menu():
    print(f"\n{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}- - - - - - - - - - M E N U - - - - - - - - - -\n")
    print(f"{Style.BRIGHT}{Fore.WHITE}1 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTCYAN_EX}Texto {Style.NORMAL}{Fore.WHITE}para {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}ASCII")
    print(f"{Style.BRIGHT}{Fore.WHITE}2 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTCYAN_EX}Texto {Style.NORMAL}{Fore.WHITE}para {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Base64")
    print(f"{Style.BRIGHT}{Fore.WHITE}3 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTCYAN_EX}Texto {Style.NORMAL}{Fore.WHITE}para {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Binário")
    print(f"{Style.BRIGHT}{Fore.WHITE}4 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTCYAN_EX}Texto {Style.NORMAL}{Fore.WHITE}para {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Braille")
    print(f"{Style.BRIGHT}{Fore.WHITE}5 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTCYAN_EX}Texto {Style.NORMAL}{Fore.WHITE}para {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Emojis")
    print(f"{Style.BRIGHT}{Fore.WHITE}6 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTCYAN_EX}Texto {Style.NORMAL}{Fore.WHITE}para {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Morse")
    print(f"{Style.BRIGHT}{Fore.WHITE}7 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTCYAN_EX}Texto {Style.NORMAL}{Fore.WHITE}para {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Código de Barras")
    print(f"{Style.BRIGHT}{Fore.WHITE}8 {Style.NORMAL}{Fore.WHITE}- Ler {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Código de Barras de Imagem")
    print(f"{Style.BRIGHT}{Fore.WHITE}9 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTCYAN_EX}Texto {Style.NORMAL}{Fore.WHITE}para {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Todos os Formatos")
    print(f"{Style.BRIGHT}{Fore.WHITE}0 {Style.NORMAL}{Fore.WHITE}- {Style.BRIGHT}{Fore.LIGHTRED_EX}Sair\n")

# Função principal
def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            texto = input("Digite o Texto a ser convertido para ASCII: ")
            resultado = text_to_ascii(texto)
            salvar_em_arquivo('ascii.txt', resultado)
            print(f"Resultado em ASCII: {resultado}")
        
        elif opcao == '2':
            texto = input("Digite o Texto a ser convertido para Base64: ")
            resultado = text_to_base64(texto)
            salvar_em_arquivo('base64.txt', resultado)
            print(f"Resultado em Base64: {resultado}")
        
        elif opcao == '3':
            texto = input("Digite o Texto a ser convertido para Binário: ")
            resultado = text_to_binary(texto)
            salvar_em_arquivo('binary.txt', resultado)
            print(f"Resultado em Binário: {resultado}")
        
        elif opcao == '4':
            texto = input("Digite o Texto a ser convertido para Braille: ")
            resultado = text_to_braille(texto)
            salvar_em_arquivo('braille.txt', resultado)
            print(f"Resultado em Braille: {resultado}")
        
        elif opcao == '5':
            texto = input("Digite o Texto a ser convertido para Emojis: ")
            resultado = text_to_emoji(texto)
            salvar_em_arquivo('emoji.txt', resultado)
            print(f"Resultado em Emojis: {resultado}")
        
        elif opcao == '6':
            texto = input("Digite o Texto a ser convertido para Morse: ")
            resultado = text_to_morse(texto)
            salvar_em_arquivo('morse.txt', resultado)
            print(f"Resultado em Código Morse: {resultado}")
        
        elif opcao == '7':
            texto = input("Digite o Texto a ser convertido para Código de Barras: ")
            output_image = 'codbarras'  # A extensão .png será adicionada automaticamente
            gerar_codigo_de_barras(texto, output_image)
        
        elif opcao == '8':
            image_path = input("Digite o nome da imagem com o Código de Barras (ex: codbarras.png): ")
            ler_codigo_de_barras(image_path)
        
        elif opcao == '9':
            texto = input("Digite o Texto a ser convertido para Todos os Formatos: ")
            ascii_result = text_to_ascii(texto)
            base64_result = text_to_base64(texto)
            binary_result = text_to_binary(texto)
            braille_result = text_to_braille(texto)
            emoji_result = text_to_emoji(texto)
            morse_result = text_to_morse(texto)
            gerar_codigo_de_barras(texto, 'codbarras')

            salvar_em_arquivo('ascii.txt', ascii_result)
            salvar_em_arquivo('base64.txt', base64_result)
            salvar_em_arquivo('binary.txt', binary_result)
            salvar_em_arquivo('braille.txt', braille_result)
            salvar_em_arquivo('emoji.txt', emoji_result)
            salvar_em_arquivo('morse.txt', morse_result)

            print(f"Todos os formatos foram gerados e salvos.")
        
        elif opcao == '0':
            print(f"{Style.BRIGHT}{Fore.LIGHTRED_EX}Saindo...")
            break

        else:
            print(f"{Style.BRIGHT}{Fore.RED}Opção inválida. Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    main()
