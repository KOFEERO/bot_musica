# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 01:03:28 2022

@author: joe
"""

from re import A
from numpy import vdot, where
import pytube
from moviepy.editor import *
from os import link, remove, rename
import os
import sys
import pygame
def app():
        
    iniciar = True
    while iniciar:
        print("Ingrese la url de la canción")
        print("Ejemplo: !yt https://youtu.be/p2FZvPLWf_M")
        url = input('> ')
        if len(url) > 0:
            descargar_video(url)
            iniciar = False
        else:
            print("No a ingresado ningún link")
    
def descargar_video(link_video):
    power = True
    while power:
        if '!yt' in link_video:
            video_d = link_video[4:]

            if 'www.youtube.com' or 'youtu.be' in video_d: #vdot
                yt = pytube.YouTube(video_d)
                name_video = yt.title

                descarga = yt.streams.get_by_itag('17')
                descarga.download('videos/')
                documentos = os.listdir('/Users/joe/Desktop/Programas/bot_music/videos')
                # print(documentos)
                video_converte = ''
                for name in documentos:
                    video_converte += name
                musica_exists = os.listdir('/Users/joe/Desktop/Programas/bot_music/musica')
                if video_converte[:-5]+'.mp3' in musica_exists:
                    os.remove(f'videos/{video_converte}')
                    reproducir_audio(video_converte[:-5]+'.mp3') 
                else:
                     convertir_mp3(video_converte)
        else:
            # print("A ocurrido un error, comando invalido")
            print("Use: !yt link video")
            app()





def convertir_mp3(nombre_archivo):
    print("Aguarde unos segundos, porfavor...")
    musica_nombre = nombre_archivo[:-5]+'.mp3'
    ruta = f'videos/{nombre_archivo}'
    ruta_mp3 = f"musica/{musica_nombre}"
    videoClip = VideoFileClip(ruta)
    audioclip = videoClip.audio
    audioclip.write_audiofile(ruta_mp3)

    audioclip.close()
    videoClip.close()

    os.remove(ruta)

    reproducir_audio(musica_nombre)

def reproducir_audio(musica_nombre):
    print(f"Reproducindo: {musica_nombre[:-4]} - By KOFFERO")
    documentos = os.listdir('/Users/joe/Desktop/Programas/bot_music/musica')
    # print(documentos)
    if musica_nombre in documentos:
        pygame.mixer.init()
        pygame.mixer.music.load('musica/'+musica_nombre)
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play()
    iniciar = True
    while iniciar:
        opcion = input("> ")
       

        if opcion == '!pause' or opcion == 'pause':
            pygame.mixer.music.pause()
        elif opcion == '!play' or opcion == 'play':
            pygame.mixer.music.unpause()
        elif '!yt' in opcion:
            descargar_video(opcion)
            app()
        elif opcion == '!repeat':
            reproducir_audio(musica_nombre)
        elif opcion == '!vol 0':
            pygame.mixer.music.set_volume(0)
        elif opcion == '!vol 10':
            pygame.mixer.music.set_volume(0.1)
        elif opcion == '!vol 50':
            pygame.mixer.music.set_volume(0.6)
        elif opcion == '!vol 100':
            pygame.mixer.music.set_volume(1.0)
    
app()
