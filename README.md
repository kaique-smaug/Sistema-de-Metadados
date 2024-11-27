Ferramenta de automação de metadados
Esta ferramenta fornece automação para tarefas de manipulação de arquivos, como copiar, renomear e compactar arquivos. Ela se integra com planilhas do Excel para extração de metadados e usa uma interface gráfica de usuário para entrada do usuário.

Características
Cópia de arquivo : gera automaticamente .batarquivos para cópia de arquivo e os executa.
Renomeação de arquivos : usa dados de uma planilha do Excel para renomear arquivos sistematicamente.
Compactação de arquivos : compacta arquivos em um arquivo ZIP para armazenamento eficiente.
Integração com Excel : lê e processa metadados de planilhas do Excel.
Acompanhamento de progresso : exibe uma barra de progresso para tarefas em andamento e informa o usuário quando os processos são concluídos.
Multithreading : executa operações de arquivo em threads separadas para garantir uma interface de usuário responsiva.
Requisitos
Python 3.8 ou superior
Dependências:
datetime
threading
subprocess
shutil
os
Módulos personalizados:
src.Mixed.Excel_folder
src.Files
src.Tkinter.Ttk_v2
src.Excel
src.Zip
Instalação
Clone o repositório:
bater

Copiar código
git clone https://github.com/kaique-smaug/metadados-automation-tool.git
cd metadados-automation-tool
Instalar bibliotecas necessárias:
bater

Copiar código
pip install -r requirements.txt
Certifique-se de que a srcpasta contém os módulos personalizados ( Mixed, Files, Tkinter, Excel, Zip).
Uso
Execute o aplicativo
Execute o script executando:

bater

Copiar código
python main.py
Avisos do usuário
Insira o caminho da pasta para salvar os arquivos quando solicitado.
Especifique o caminho da planilha do Excel que contém metadados para operações de arquivo.
Processos
Cópia de arquivo : copia arquivos com base em metadados da planilha.
Renomear arquivo : renomeia arquivos usando regras predefinidas extraídas da planilha.
Compactação : arquiva arquivos em um único arquivo ZIP.
Visão geral do código
Principais funções
run_command(path)
Executa comandos shell para processar .batarquivos.

file_copy_process(reponse_folder, rep, now, file, ttk)
Lida com operações de cópia de arquivos e atualiza a barra de progresso.

file_ren_process(reponse_folder, rep, now, file, ttk)
Renomeia arquivos e informa o usuário quando o processo é concluído.

zip_file(reponse_folder, zip, ttk)
Compacta arquivos em um arquivo ZIP.

execute_just_vbs(path, reponse_excel)
Executa um VBScript com os parâmetros fornecidos.

main()
Orquestra todas as operações, desde a coleta de entradas do usuário até a execução de operações de arquivo.

Estrutura de pastas
css

Copiar código
metadados-automation-tool/
├── src/
│   ├── Mixed/
│   │   └── Excel_folder.py
│   ├── Files/
│   │   └── Files.py
│   ├── Tkinter/
│   │   └── Ttk_v2.py
│   ├── Excel/
│   │   └── Excel.py
│   ├── Zip/
│       └── Zip.py
├── main.py
└── README.md
Personalização
Atualizando caminhos de arquivo
Modifique os caminhos main()para refletir a estrutura do seu diretório local.

Estendendo a funcionalidade
A ferramenta pode ser estendida adicionando novos módulos ou modificando os existentes na srcpasta.

Versão
1.2.0
