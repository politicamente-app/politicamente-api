import os
import re

# --- CONFIGURAÇÃO ---
SOURCE_FILE = 'update_source.txt'
FILE_HEADER_PATTERN = re.compile(r'## Arquivo: (.*?)\n')

def apply_updates():
    """
    Lê o arquivo de código-fonte consolidado e distribui o conteúdo
    para os arquivos e pastas corretos dentro da estrutura do projeto.
    """
    print("⚙️  Iniciando a atualização do projeto...")

    try:
        with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ Erro: O arquivo de origem '{SOURCE_FILE}' não foi encontrado.")
        print("Por favor, copie o código do nosso chat, salve como 'update_source.txt' na raiz do projeto e tente novamente.")
        return

    # Separa o conteúdo em blocos, usando "---" como delimitador principal
    blocks = content.split('\n---\n')

    files_created_or_updated = 0

    for block in blocks:
        # Pula blocos vazios ou que não sejam de arquivos
        if not block.strip():
            continue

        # Procura pelo cabeçalho do arquivo no bloco
        match = FILE_HEADER_PATTERN.search(block)
        if not match:
            continue

        # Extrai o caminho do arquivo e o código-fonte
        filepath = match.group(1).strip()

        # O código começa após o cabeçalho completo
        code_content = block[match.end():].strip()

        try:
            # Garante que o diretório onde o arquivo será salvo exista
            directory = os.path.dirname(filepath)
            if directory:
                os.makedirs(directory, exist_ok=True)

            # Escreve o conteúdo no arquivo, sobrescrevendo se já existir
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(code_content)

            print(f"✔️ Arquivo '{filepath}' criado/atualizado com sucesso.")
            files_created_or_updated += 1

        except IOError as e:
            print(f"❌ Erro ao escrever o arquivo '{filepath}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


    if files_created_or_updated > 0:
        print(f"\n🎉 Processo concluído! {files_created_or_updated} arquivos foram atualizados.")
    else:
        print("\n⚠️ Nenhum arquivo para atualizar foi encontrado no arquivo de origem.")


if __name__ == "__main__":
    apply_updates()