from deep_translator import GoogleTranslator
import os

# Caminhos dos arquivos
input_file = r'c:\Users\jedua\Desktop\novas\teste 3.txt' #alterar para o caminho do arquivo de entrada
output_file = r'c:\Users\jedua\Desktop\novas\teste 3 traduzido.txt' #alterar para o caminho do arquivo de saída
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
