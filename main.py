# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 01:03:28 2022

@author: joe
"""

from numpy import where
import pytube
from moviepy.editor import *
from os import remove, rename
import os
import sys
import pygame
def app():
        
    iniciar = True
    while iniciar:
        url = input('Link del video: ')
        if len(url) > 0:
            descargar_video(url)
            iniciar = False
        else:
            print("No a ingresado ningún link")
    
def descargar_video(link_video):
    power = True
    while power:
        if 'www.youtube.com' or 'youtu.be' in link_video:
            yt = pytube.YouTube(link_video)
            name_video = yt.title
            lista_formatos = yt.streams.all()
            #for formatos in lista_formatos:
            #    print(formatos)

            descarga = yt.streams.get_by_itag('17')
            descarga.download('videos/')
            documentos = os.listdir('/Users/joe/Desktop/Programas/yt_descargas/videos')
            # print(documentos)
            video_converte = ''
            for name in documentos:
                video_converte += name
            convertir_mp3(video_converte)
            power = False
        else:
            print("A ocurrido un erro, link invalido")





def convertir_mp3(nombre_archivo):
    # print(nombre_archivo)
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
    documentos = os.listdir('/Users/joe/Desktop/Programas/yt_descargas/musica')
    # print(documentos)
    if musica_nombre in documentos:
        pygame.mixer.init()
        pygame.mixer.music.load('musica/'+musica_nombre)
        # pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.play()
    
    iniciar = True
    while iniciar:
        opcion = input("> ")

        if opcion == '!stop' or opcion == 'stop':
            pygame.mixer.music.pause()
        elif opcion == '!play' or opcion == 'play':
            pygame.mixer.music.unpause()
        
        elif 'www.youtube.com' or 'youtu.be' in opcion:
            descargar_video(opcion)

        elif opcion == '!vol 50' or opcion == 'vol 50':
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume + 0.5)
        else:
            print("¡Comando  invalido!")
    
app()
