# 📁 Organizador de Arquivos por Extensão

Um programa Python que organiza automaticamente arquivos em uma pasta, movendo-os para subpastas de acordo com suas extensões.

## 🎯 Funcionalidades

- ✅ **Organização Automática**: Percorre todos os arquivos de uma pasta e os organiza por extensão
- ✅ **Criação Dinâmica de Pastas**: Cria subpastas automaticamente para cada tipo de extensão encontrada
- ✅ **Registro de Operações**: Registra todas as ações em um arquivo de log com data, hora e detalhes da movimentação
- ✅ **Resumo Executivo**: Exibe ao final um relatório com a quantidade de arquivos organizados e extensões encontradas

## 📋 Requisitos

- Python 3.6+
- Nenhuma dependência externa (usa apenas bibliotecas padrão do Python)

## 🚀 Como Usar

1. **Preparar os arquivos**: Coloque todos os arquivos que deseja organizar na pasta `organizador/`

2. **Executar o programa**:
```bash
python main.py
```

3. **Verificar os resultados**:
   - Os arquivos serão movidos para subpastas nomeadas como `pasta_.extensao`
   - Consulte `registro.log` para histórico detalhado de todas as operações

## 📊 Exemplo de Saída

Após executar o programa, você verá algo como:

```
Quantidade de extensões: 2
Extensões presentes: ['.txt', '.jpg']
```

### Estrutura de Diretórios (Antes e Depois)

**Antes:**
```
organizador/
├── arquivo1.txt
├── documento.pdf
├── imagem.jpg
└── relatorio.xlsx
```

**Depois:**
```
organizador/
├── pasta_.txt/
│   ├── arquivo1.txt
│   └── relatorio_semanal.txt
├── pasta_.pdf/
│   └── documento.pdf
├── pasta_.jpg/
│   └── imagem.jpg
└── pasta_.xlsx/
    └── relatorio.xlsx
```

## 📝 Registro de Log

O arquivo `registro.log` mantém um histórico de todas as operações com as seguintes informações:

```
13/01/2026 14:32:45 - arquivo1.txt: Section 14 - Projeto Organizador de Arquivos/organizador/pasta_.txt
13/01/2026 14:32:46 - documento.pdf: Section 14 - Projeto Organizador de Arquivos/organizador/pasta_.pdf
```

## 🛠️ Funcionalidades Principais

### `separar_arquivos_por_pastas()`
Função principal que:
- Itera sobre todos os arquivos da pasta `organizador`
- Cria pastas para cada extensão encontrada
- Move os arquivos para as pastas correspondentes
- Registra cada operação no log

**Retorno**: Tupla contendo (quantidade de arquivos movidos, lista de extensões encontradas)

### `remover_arquivos_das_pastas()`
Função auxiliar que desfaz a organização, movendo todos os arquivos de volta para a pasta raiz.

## ⚠️ Observações Importantes

- O programa utiliza `pathlib.Path` para manipulação de caminhos (compatível com diferentes sistemas operacionais)
- A função `shutil.move()` move os arquivos (não cria cópias)
- O log é aberto em modo append (`r+`), preservando histórico anterior
- Exceções são capturadas e exibidas com mensagens descritivas

## 📚 Tecnologias Utilizadas

- **pathlib**: Para manipulação de caminhos de arquivos
- **shutil**: Para operações de mover arquivos
- **datetime**: Para timestamps no registro de log

## 🔧 Melhorias Futuras

- Adicionar interface gráfica (tkinter ou PyQt)
- Permitir seleção de diretório via argumento de linha de comando
- Suporte para filtros de extensão personalizados
- Validação de espaço em disco antes de mover arquivos
- Opção para desfazer alterações

## 📄 Licença

Este projeto é de código aberto e pode ser utilizado livremente.

## 👨‍💻 Autor

Desenvolvido como projeto educacional para consolidar conhecimentos em manipulação de arquivos e operações em sistema de arquivos com Python.
