# Versão simples do tradutor TXT
from deep_translator import GoogleTranslator 
import os

# Caminhos dos arquivos
input_file = r'c:\Users\jedua\Desktop\novas\dialogue.txt' #alterar para o caminho do arquivo de entrada
output_file = r'c:\Users\jedua\Desktop\novas\dialogue_traduzido.txt' #alterar para o caminho do arquivo de saída
# Verifica se o arquivo de entrada existe
# Se o arquivo não existir, o script não fará nada e informará o que o arquivo não foi encontrado
# Se o arquvivo existir, o script irá ler o arquivo, traduzir linha por linha e salvar o resultado em um novo arquivo
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_file(content, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(content)

def translate_lines(lines):
    translator = GoogleTranslator(source='auto', target='pt')
    translated = []
    for line in lines:
        clean_line = line.strip()
        if clean_line == '':
            translated.append('\n')
        else:
            try:
                traduzida = translator.translate(clean_line)
                if traduzida:  # verifica se não é None
                    translated.append(traduzida + '\n')
                else:
                    print(f"[!] Resposta vazia para: {clean_line}")
                    translated.append(clean_line + '\n')  # mantém original
            except Exception as e:
                print(f"Erro ao traduzir linha: {clean_line}")
                print(e)
                translated.append(clean_line + '\n')  # fallback para original
    return translated

if os.path.exists(input_file):
    print("Lendo o arquivo original...")
    original_lines = read_file(input_file)

    print("Traduzindo linha por linha...")
    translated_lines = translate_lines(original_lines)

    print("Salvando a tradução...")
    write_file(translated_lines, output_file)

    print("Abrindo no Bloco de Notas...")
    os.system(f'notepad {output_file}')

    print("Tradução finalizada com sucesso!")
else:
    print(f"Arquivo não encontrado: {input_file}")

# Versão Automatica do Tradutor TXT
from deep_translator import GoogleTranslator
import os

print("Tradutor de Arquivos TXT - powered by Deep Translator\n")

# Pede o caminho do arquivo original
input_file = input("Caminho de onde está o arquivo .txt que será traduzido:\n> ").strip()

# Pede o nome para o arquivo traduzido (sem extensão)
output_name = input("Nome para o arquivo traduzido (sem .txt):\n> ").strip()
output_file = os.path.join(os.path.dirname(input_file), output_name + ".txt")

# Pede o idioma de destino
target_language = input("Idioma (ex: pt, en, es, fr, de, ja, ru):\n> ").strip().lower()

def traduzir_linhas(linhas, destino):
    linhas_traduzidas = []
    for idx, linha in enumerate(linhas):
        linha = linha.strip()
        if linha == "":
            linhas_traduzidas.append("")
            continue
        try:
            traduzida = GoogleTranslator(source='auto', target=destino).translate(linha)
            print(f"✓ Linha {idx+1} traduzida.")
        except Exception as e:
            print(f"Erro ao traduzir linha {idx+1}: {e}")
            traduzida = linha  # mantém original se falhar
        linhas_traduzidas.append(traduzida)
    return linhas_traduzidas

try:
    with open(input_file, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    linhas_traduzidas = traduzir_linhas(linhas, target_language)

    with open(output_file, 'w', encoding='utf-8') as saida:
        for linha in linhas_traduzidas:
            saida.write(linha + '\n')

    print(f"\nTradução finalizada! Arquivo salvo em: {output_file}")
    os.system(f'notepad "{output_file}"')  # Abre no bloco de notas
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o caminho que você digitou.")
except Exception as e:
    print(f"Erro inesperado: {e}")
