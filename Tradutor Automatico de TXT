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
