from pytube import YouTube
from pytube import Playlist
from tkinter import filedialog, simpledialog, messagebox
from moviepy.editor import *
import os

#Função que irá converter os arquivos para MP3
def converter_arquivos():
    arquivo = nome.replace('mp4', 'mp3')
    FILETOCONVERT = AudioFileClip(nome)
    FILETOCONVERT.write_audiofile(arquivo)
    FILETOCONVERT.close()

#Abre a caixa de texto para inserir o link do video ou playlist
url = simpledialog.askstring(title='YouTube - Downloader', prompt="Cole Aqui a URL do YouTube: \t\t\t\t\t\t\t")

#Coleta o diretório para seleção da pasta downloads
user = os.getlogin()
os.chdir(f'C:/Users/{user}/Downloads')

#Verifica se é um link válido do youtube
try:
    if url.find('youtube') != -1:
        
        #Verifica se o link é uma Playlist
        if url.find('/playlist') != -1:
            print('playlist')
            p = Playlist(url)
            nova_pasta = p.title
            try:
                cria_pasta = os.mkdir(path=f'{nova_pasta}')
            except FileExistsError:
                pass
            os.chdir(f'C:/Users/{user}/Downloads/{nova_pasta}')
            atual = os.getcwd()
            print(f"diretorio mudou apos criar a pasta >>> {atual}")
            print(f'Baixando videos da playlist {p.title}')

            for video in p.videos:
                print(f" >>> Baixando video: {video.title}")
                video.streams.first().download()

            print("Download da PlayList concluido.")

        #Verifica se o link é apenas um video
        elif url.find('/watch') != -1:
            # print('Single Video')
            nova_pasta = 'YouTube_Downloader'
            try:
                cria_pasta = os.mkdir(path=f'{nova_pasta}')
            except FileExistsError:
                pass
            os.chdir(f'C:/Users/{user}/Downloads/{nova_pasta}')
            atual = os.getcwd()
            # print(f"diretorio mudou apos criar a pasta >>> {atual}")
            YouTube(url).streams.first().download()
            yt = YouTube(url)
    else:
        print('Não é um link do Youtube')

except:
    pass

#verifica se o usuário deseja converter arquivos
opcao = messagebox.askquestion(title='YouTube - Downloader', message='Deseja formatar os arquivos?')
if opcao == 'yes':

    #Verifica se o usuario deseja excluir os arquivos originais
    origem = filedialog.askopenfilenames(title='YouTube - Downloader')
    opcao = messagebox.askquestion(title='YouTube - Downloader', message='Deseja excluir os arquivos de Origem após a conversão?')
    if opcao == 'yes':
        for nome in origem:
            converter_arquivos()
            os.remove(nome)

    elif opcao == 'no':
        for nome in origem:
            converter_arquivos()
            
    print('Finalizando o Programa!')
else:
    print('Finalizando o Programa!')