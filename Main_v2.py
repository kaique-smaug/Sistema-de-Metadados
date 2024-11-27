__version__ = '1.2.0'

from src.Mixed import Excel_folder
from datetime import datetime
from src.Files import Files
from src.Tkinter import Ttk_v2
from src.Excel import Excel
from src.Zip import Zip
import threading
import subprocess
from sys import executable
from os.path import dirname
from shutil import move

def run_command(path):
    """Executa um comando de shell para copiar arquivos."""
    try:
       # subprocess.run("chcp 65001", shell=True)
        result = subprocess.run(fr'{path}', shell=True, check=True, encoding="utf-8")
        return result.returncode

    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando {path}: {e}")
        return e.returncode

def file_copy_process(reponse_folder, rep, now, file, ttk):
    file.convert_file(rf'{reponse_folder}\copy_{rep(now)}.txt',
                      rf'{reponse_folder}\copy_{rep(now)}.bat')
    
    file.convert_file(rf'{reponse_folder}\copy_{rep(now)}_destiny.txt',
                      rf'{reponse_folder}\copy_{rep(now)}_destiny.bat')

    # Executa o arquivo .bat para iniciar a cópia
    exit_code = run_command(fr'{reponse_folder}\\copy_{rep(now)}_destiny.bat')
    
    # Atualiza a barra de progresso após a cópia
    ttk.progressbar_1.set(1)  # Finaliza a barra de progresso
    if exit_code == 0:
        ttk.close()

    return exit_code

def file_ren_process(reponse_folder, rep, now, file, ttk):
    file.convert_file(rf'{reponse_folder}\ren_{rep(now)}.txt',
                      rf'{reponse_folder}\ren_{rep(now)}.bat')

    exit_code = run_command(f'{reponse_folder}\\ren_{rep(now)}.bat')

    ttk.progressbar_1.set(1)  # Finaliza a barra de progresso
    if exit_code == 0:
        ttk.close()

    return exit_code

def zip_file(reponse_folder, zip, ttk):
    response = zip.ziping(fr'{reponse_folder}', fr'{reponse_folder}\Metadados_Carrefour.zip')
    
    ttk.progressbar_1.set(1)  # Finaliza a barra de progresso
    if response == 0:
        ttk.close()

def execute_just_vbs(path, reponse_excel):
    run_command(fr'cscript "{path}" "{reponse_excel}"')

def main():
    # Configurações iniciais
    path_atual = dirname(executable)
    
    zip = Zip.Zip()
    excel_file = Excel_folder.Excel_folder_()
    file = Files.Files()

    now = str(datetime.now().strftime('%m-%d'))
    rep = lambda rr: rr.replace('-', '.').replace('_', '.').replace('/', '.')

    ttk = Ttk_v2.Window('Metadados')
    reponse_folder = ttk.window_recursive(
        f'Digite o caminho onde deseja colocar as gravações \n Exemplo: N:\\folder\\subfolder1\\subfolder2\\Day - Month\\{rep(now)} ou {now}',
        'Digite o Diretório...'
    )
    print(f'aqui {reponse_folder}')

    ttk = Ttk_v2.Window('Metadados')
    reponse_excel = ttk.window_recursive(
        f'Digite o caminho onde deseja pegar a planilha de Seleção \n Exemplo: N:\\folder\\subfolder1\\subfolder2\\Day - Month\\Planilha',
       'Digite o Diretório...'
    )

    file.create(fr'{reponse_folder}')
    file.create_text(fr'{reponse_folder}\\Copy_{rep(now)}.txt')

    excel_file.openSpreadsheet(
        fr'{reponse_excel}', 'Planilha1',
        rf'{reponse_folder}\\copy_{rep(now)}.txt', 'LocalDeEstocagem', reponse_folder
    )

    file.adjust_bar(
        rf'{reponse_folder}\\copy_{rep(now)}.txt',
        rf'{reponse_folder}\\copy_{rep(now)}_destiny.txt'
    )

    ttk = Ttk_v2.Window('Metadados')
    ttk.wait("Copiando arquivos, por favor aguarde...")

    # Inicia o processo de cópia em uma nova thread
    copy_thread = threading.Thread(target=file_copy_process, args=(reponse_folder, rep, now, file, ttk))

    copy_thread.start()
    
    ttk.mainloop()  # Inicia o loop da interface gráfica enquanto a cópia está sendo executada

    ttk = Ttk_v2.Window('Metadados')
    ttk.fineshed('Copia finalizada.')

    file.create_text(fr'{reponse_folder}\ren_{rep(now)}.txt')

    excel = Excel.Excel(fr'{reponse_excel}')
    excel.load_for_xtract('Planilha1', '\\', 8, 1000)

    excel_file.formula(reponse_excel, 'Planilha1', reponse_folder)

    excel = Excel.Excel(fr'{reponse_excel}')
    excel.remove_formula('Planilha1')

    excel_file.openSpreadsheet(fr'{reponse_excel}', 'Planilha1',
                               rf'{reponse_folder}\ren_{rep(now)}.txt',
                               'KEY_FORMATED')

    ttk = Ttk_v2.Window('Metadados')
    # Mostra mensagem de carregamento
    ttk.wait("Renomeando arquivos, por favor aguarde...")
    
    execute_ren = threading.Thread(target=file_ren_process, args=(reponse_folder, rep, now, file, ttk))
    execute_ren.start()
    #execute_ren.join()

    ttk.mainloop() 

    ttk = Ttk_v2.Window('Metadados')
    ttk.fineshed('Renomeação finalizada.')

    file.delete(rf'{reponse_folder}\ren_{rep(now)}.txt')
    file.delete(rf'{reponse_folder}\ren_{rep(now)}.bat')
    file.delete(rf'{reponse_folder}\\copy_{rep(now)}.bat')
    file.delete(rf'{reponse_folder}\\copy_{rep(now)}_destiny.bat')

    ttk = Ttk_v2.Window('Metadados')
    # Mostra mensagem de carregamento
    ttk.wait("Zipando arquivos, por favor aguarde...")

    execute_zip = threading.Thread(target=zip_file, args=(reponse_folder, zip, ttk))
    execute_zip.start()

    ttk.mainloop() 
    
    ttk = Ttk_v2.Window('Metadados')
    ttk.fineshed('Processo finalizado.')

# Executa a função main
if __name__ == "__main__":
    main()