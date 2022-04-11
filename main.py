# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 01:03:28 2022

@author: joe
"""

import pytube
from moviepy.editor import *
from os import remove, rename
import os
import sys
import pygame
import glob
def app():
    # Creamos los directorios donde se descargaran los videos y musicas
    if os.path.exists('videos/') and os.path.exists('musica/'):
        print()
    else:
        os.mkdir('videos/')
        os.mkdir('musica/')    
    iniciar = True
    # Aquí es primordial que los usuarios puedan usar el bot sin haber puesto un link valido
    while iniciar:
        volumen = 1.0
        print("Ingrese la url de la canción")
        print("Ejemplo: !yt https://youtu.be/p2FZvPLWf_M")
        url = input('> ')
        # Si el link es valido, se descarga el video, tambien le damos un volumen por defecto
        if len(url) > 0:
            descargar_video(url, volumen)
        else:
            print("No a ingresado ningún link")
    
def descargar_video(link_video, volumen):
    power = True
    while power:
        if '!yt' in link_video:
            video_d = link_video[4:]
            # Si la url contiene estos fragmento significa que es una url valida
            # y se comenzará la descarga
            if 'www.youtube.com' or 'youtu.be' in video_d: #vdot
                yt = pytube.YouTube(video_d)
                name_video = yt.title
                descarga = yt.streams.get_by_itag('17')
                descarga.download('videos/')
                # Con esta lineas vamos a saber la musicas que ya está descargada
                documentos = os.listdir('/home/iori/bot_musica/videos')
                # print(documentos)
                video_converte = ''
                for name in documentos:
                    video_converte += name
                musica_exists = os.listdir('/home/iori/bot_musica/musica')
                # si ya está la canción, se omite la descarga.
                if video_converte[:-5]+'.mp3' in musica_exists:
                    os.remove(f'videos/{video_converte}')
                    # automaticamente lo reproducimos con un volumen por defecto
                    reproducir_audio(video_converte[:-5]+'.mp3', volumen) 
                else:
                    # sino se descarga el video, y luego lo pasamos a mp3
                     convertir_mp3(video_converte, volumen)
        else:
            # print("A ocurrido un error, comando invalido")
            print("Use: !yt link video")
            app()





def convertir_mp3(nombre_archivo, volumen):
    # Aqui lo que hacemos es pasar los videos mp4 a mp3
    print("Aguarde unos segundos, porfavor...")
    musica_nombre = nombre_archivo[:-5]+'.mp3'
    ruta = f'videos/{nombre_archivo}'
    ruta_mp3 = f"musica/{musica_nombre}"
    videoClip = VideoFileClip(ruta)
    audioclip = videoClip.audio
    audioclip.write_audiofile(ruta_mp3)

    audioclip.close()
    videoClip.close()
    # Una vez se hay hecho la conversión, eliminamos el archivo .mp4 para liberar espacio
    os.remove(ruta)
    # Seguido lo reproducimos con la función siguiente y con un volumen por defecto
    reproducir_audio(musica_nombre, volumen)

def reproducir_audio(musica_nombre, volumen):
    os.system('clear')
    print(f"Reproducindo: {musica_nombre[:-4]} - By KOFFERO")
    documentos = os.listdir('/home/iori/bot_musica/musica')
    # print(documentos)
    if musica_nombre in documentos:
        pygame.mixer.init()
        pygame.mixer.music.load('musica/'+musica_nombre)
        pygame.mixer.music.set_volume(volumen)
        pygame.mixer.music.play()
        
    iniciar = True
    # Agregue está sección para controlar la musica en reprodución
    # Pausar
    # Play
    # Repetir
    # Control de volumen volumen
    while iniciar:

        opcion = input("> ")

        if opcion == '!pause' or opcion == 'pause':
            pygame.mixer.music.pause()
        elif opcion == '!play' or opcion == 'play':
            pygame.mixer.music.unpause()
        elif '!yt' in opcion: # esta parte es la que dectecta una url valida
            descargar_video(opcion, volumen) # y llama a la función de descarga mas arriba
            app()
        elif opcion == '!vol 0':
            pygame.mixer.music.set_volume(0)
            volumen = 0
        elif opcion == '!vol 10':
            pygame.mixer.music.set_volume(0.1)
            volumen = 0.1
        elif opcion == '!vol 50':
            pygame.mixer.music.set_volume(0.6)
            volumen = 0.6
        elif opcion == '!vol 100':
            pygame.mixer.music.set_volume(1.0)
            volumen = 1.0
        elif opcion == '!exit': # Con está cerramos el programa y todas canciones se eliminan
            pygame.mixer.music.stop()
            eliminar_canciones()
        elif opcion == '!repeat':
            reproducir_audio(musica_nombre, volumen)

def eliminar_canciones():
    ruta_musicas = glob.glob('musica/*.mp3')
    for musica in ruta_musicas:
        try:
            os.remove(musica)
        except OSError as e:
            print(f"Error: {e.strerror}")
    sys.exit()
    
    
app()
