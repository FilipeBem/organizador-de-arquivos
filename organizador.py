import os
import shutil
import PySimpleGUI as sg

sg.theme('Green')

# Define a função para organizar os arquivos
def organizar_arquivos(diretorio):
    # Cria um dicionário para armazenar as extensões e as pastas correspondentes
    extensoes = {
        '.pdf': 'PDFs',
        '.txt':'Texto',
        '.docx':'Texto',
        '.odt':'Texto',
        '.rtf':'Texto',
        '.tex':'Texto',
        '.log':'Texto',
        '.xlsx':'Planilhas',
        '.xls':'Planilhas',
        '.ods':'Planilhas',
        '.csv':'Planilhas',
        '.tsv':'Planilhas',
        '.docx':'Documentos',
        '.doc':'Documentos',
        '.pptx':'Documentos',
        '.ppt':'Documentos',
        '.odp':'Documentos',
        '.mp3':'Músicas',
        '.wav':'Músicas',
        '.wma':'Músicas',
        '.aac':'Músicas',
        '.flac':'Músicas',
        '.ogg':'Músicas',
        '.mp4':'Vídeos',
        '.avi':'Vídeos',
        '.mov':'Vídeos',
        '.wmv':'Vídeos',
        '.mkv':'Vídeos',
        '.flv':'Vídeos',
        '.webm':'Vídeos',
        '.m4v':'Vídeos',
        '.3gp':'Vídeos',
        '.jpg':'Imagens',
        '.jpeg':'Imagens',
        '.png':'Imagens',
        '.gif':'Imagens',
        '.bmp':'Imagens',
        '.svg':'Imagens',
        '.tiff':'Imagens',
        '.py':'Código fonte',
        '.java':'Código fonte',
        '.cpp':'Código fonte',
        '.html':'Código fonte',
        '.css':'Código fonte',
        '.js':'Código fonte',
        '.json':'Código fonte',
        '.xml':'Código fonte',
        '.yml':'Código fonte',
        '.yaml':'Código fonte',
        '.md':'Código fonte',
        '.sh':'Código fonte',
        '.bat':'Código fonte',
        '.ps1':'Código fonte',
        '.rb':'Código fonte',
        '.php':'Código fonte',
        '.go':'Código fonte',
        '.swift':'Código fonte',
        '.kt':'Código fonte',
        '.c':'Código fonte',
        '.h':'Código fonte',
        '.m':'Código fonte',
        '.mm':'Código fonte',
        '.pl':'Código fonte',
        '.lua':'Código fonte',
        '.r':'Código fonte',
        '.scala':'Código fonte',
        '.sql':'Código fonte',
        '.tcl':'Código fonte',
        '.vb':'Código fonte',
        '.vbs':'Código fonte',
        '.asm':'Código fonte',
        '.sln':'Código fonte',
        '.csproj':'Código fonte',
        '.vcxproj':'Código fonte',
        '.zip':'Arquivos compactados',
        '.rar':'Arquivos compactados',
        '.7z':'Arquivos compactados',
        '.tar.gz':'Arquivos compactados',
        '.tar.bz2':'Arquivos compactados',
        '.tar.xz':'Arquivos compactados',
        '.exe':'Programas',
        '.dmg':'Programas',
        '.deb':'Programas',
        '.rpm':'Programas',
        '.msi':'Programas',
        '.appimage':'Programas' 
    }
    
    # Percorre todos os arquivos no diretório
    for arquivo in os.listdir(diretorio):
        # Verifica se o arquivo é um arquivo e não uma pasta
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            # Obtém a extensão do arquivo
            extensao = os.path.splitext(arquivo)[1]
            # Verifica se a extensão está no dicionário
            if extensao in extensoes:
                # Cria a pasta correspondente, se ainda não existir
                pasta = os.path.join(diretorio, extensoes[extensao])
                if not os.path.exists(pasta):
                    os.mkdir(pasta)
                # Move o arquivo para a pasta correspondente
                shutil.move(os.path.join(diretorio, arquivo), os.path.join(pasta, arquivo))

# Define o layout da interface gráfica
layout = [
    [sg.Text('Diretório a ser organizado:'), sg.Input(key='diretorio'), sg.FolderBrowse()],
    [sg.Button('Organizar'), sg.Button('Sair')]
]

# Cria a janela da interface gráfica
janela = sg.Window('Organizador de Arquivos', layout)

# Define o event loop da interface gráfica
while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Sair':
        break
    elif evento == 'Organizar':
        diretorio = valores['diretorio']
        if os.path.exists(diretorio):
            organizar_arquivos(diretorio)
            sg.popup('Arquivos organizados com sucesso!')
        else:
            sg.popup('Diretório inválido!')

# Fecha a janela da interface gráfica
janela.close()