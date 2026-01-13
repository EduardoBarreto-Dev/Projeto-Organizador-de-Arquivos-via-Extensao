# -------------- Importações --------------
from pathlib import Path
import shutil
from datetime import datetime

# ------ Pegando os arquivos------ 
arquivos = Path('Section 14 - Projeto Organizador de Arquivos/organizador')

# ------ Percorrendo os arquivos ------ 
def separar_arquivos_por_pastas():
    try:
        quantidade_arquivos, extensoes = 0, []
        with open('Section 14 - Projeto Organizador de Arquivos/registro.log', encoding = 'utf-8', mode = 'r+') as log:
            for file in arquivos.iterdir():
                
                # Criando as pastas (caso não existam)
                Path(f'Section 14 - Projeto Organizador de Arquivos/organizador/pasta_{file.suffix}').mkdir(exist_ok=True)

                # ------ Movendo arquivos ------

                if file.is_file():
                    pasta_origem = Path(f'Section 14 - Projeto Organizador de Arquivos/organizador/{file.name}')

                    pasta_destino = Path(f'Section 14 - Projeto Organizador de Arquivos/organizador/pasta_{file.suffix}')

                    shutil.move(pasta_origem, pasta_destino)

                    # ------ Registrando no log ------ 
                    
                    
                    # Informações do log
                    data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                    arquivo_name = file.name
                    conteudo = f'{data_hora} - {arquivo_name}: {pasta_destino}'

                    # colocando no arquivo
                    log.write(f'{conteudo}\n')

                    quantidade_arquivos += 1
                    extensoes.append(file.suffix) if not file.suffix in extensoes else None

        return quantidade_arquivos, extensoes
    
    except Exception as e:
        print(f"Ocorreu uma exceção: {e}")
        quit()

    

# ------ Removendo itens das pastas ------
def remover_arquivos_das_pastas():
    try:
        for file in arquivos.rglob('*'):
            if not file.is_file():
                for file2 in file.glob('*'):
                    caminho_atual = Path(file2)
                    caminho_destino = Path(r'Section 14 - Projeto Organizador de Arquivos\organizador')
                    shutil.move(caminho_atual, caminho_destino)

    except Exception as e:
        print(f"Ocorreu uma exceção: {e}")
        quit()

resultado = separar_arquivos_por_pastas()
print(f'Quantidade de extensões: {resultado[0]}\nExtensões presentes: {resultado[1]}')