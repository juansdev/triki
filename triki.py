import sys
import pygame
from pygame.locals import *
from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw()

pygame.init()

FPS = 30 #Frames de pantalla
fpsClock = pygame.time.Clock()

#Configuracion de pantalla
screen = pygame.display.set_mode((340, 450), 0, 32)
pygame.display.set_caption('Triki')

#Colores
blanco = (255, 255, 255)
negro = (  0,   0,   0)
verde = (195,195,195)
gris   = (195,195,195)

#Funciones de Posicion
def posicionHijo(posicionCuadro,personalizado=False):
    x = posicionCuadro[0]
    y = posicionCuadro[1]
    if personalizado:
        return (x+100,y+25)
    else:
        return (x+50,y+50)
        # print(posicionCuadro)
def posicionPadre(posicion,anchoXAlto,horizontal=1,vertical=1,personalizado=False):
    x = posicion[0]
    y = posicion[1]
    ancho = anchoXAlto[0]
    alto = anchoXAlto[1]
    if horizontal == 2 and vertical == 1:
        margen = 20
        return (x+ancho+margen,1)
    elif horizontal == 3 and vertical == 1:
        margen = 20
        return (x+ancho+margen,1)
    elif horizontal == 1 and vertical == 2:
        margen = 20
        return (1,y+alto+margen)
    elif horizontal == 2 and vertical == 2:
        margen = 20
        return (x+ancho+margen,alto+margen)
    elif horizontal == 3 and vertical == 2:
        margen = 20
        return (x+ancho+margen,alto+margen)
    elif horizontal == 1 and vertical == 3:
        margen = 20
        return (1,y+alto+margen)
    elif horizontal == 2 and vertical == 3:
        margen = 20
        return (x+ancho+margen,y)
    elif horizontal == 3 and vertical == 3:
        margen = 20
        return (x+ancho+margen,y)
    elif horizontal == 2 and vertical == 4 and personalizado:
        margen = 20
        ancho = -50
        return (x+ancho,y+alto+margen)

#CUADROS PADRE
#POSICION CUADROS PADRE
#PRIMERA FILA
posicionPadreCuadro = [1,1]
anchoXAltoCuadro = [100, 100]
posicionPadreCuadro2 = posicionPadre(posicionPadreCuadro,anchoXAltoCuadro,2,1)
posicionPadreCuadro3 = posicionPadre(posicionPadreCuadro2,anchoXAltoCuadro,3,1)

#SEGUNDA FILA
posicionPadreCuadro4 = posicionPadre(posicionPadreCuadro,anchoXAltoCuadro,1,2)
posicionPadreCuadro5 = posicionPadre(posicionPadreCuadro4,anchoXAltoCuadro,2,2)
posicionPadreCuadro6 = posicionPadre(posicionPadreCuadro5,anchoXAltoCuadro,3,2)

#TERCERA FILA
posicionPadreCuadro7 = posicionPadre(posicionPadreCuadro4,anchoXAltoCuadro,1,3)
posicionPadreCuadro8 = posicionPadre(posicionPadreCuadro7,anchoXAltoCuadro,2,3)
posicionPadreCuadro9 = posicionPadre(posicionPadreCuadro8,anchoXAltoCuadro,3,3)

#CUARTA FILA
posicionPadreCuadro10 = posicionPadre(posicionPadreCuadro8,anchoXAltoCuadro,2,4,True)

#CUADROS HIJOS
#Fuente de Texto de los Cuadros Hijos
fuenteTexto = pygame.font.Font('freesansbold.ttf', 80)
fuenteTextoLimpiar = pygame.font.Font('freesansbold.ttf', 20)

#Color y Fuente de Texto a utilizar en los Cuadros Hijos
parametros_hijos = (True, negro, verde)
texto_del_cuadro_surface1 = fuenteTexto.render("", parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
texto_del_cuadro_surface2 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
texto_del_cuadro_surface3 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
texto_del_cuadro_surface4 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
texto_del_cuadro_surface5 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
texto_del_cuadro_surface6 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
texto_del_cuadro_surface7 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
texto_del_cuadro_surface8 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
texto_del_cuadro_surface9 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
texto_del_cuadro_surface10 = fuenteTextoLimpiar.render('LIMPIAR TABLERO', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
#POSICION CUADROS HIJO
#PRIMERA FILA
texto_del_cuadro_rect = texto_del_cuadro_surface1.get_rect()
texto_del_cuadro_rect.center = (posicionHijo(posicionPadreCuadro)) #Posicion del Cuadro

texto_del_cuadro_rect2 = texto_del_cuadro_surface2.get_rect()
texto_del_cuadro_rect2.center = (posicionHijo(posicionPadreCuadro2))

texto_del_cuadro_rect3 = texto_del_cuadro_surface3.get_rect()
texto_del_cuadro_rect3.center = (posicionHijo(posicionPadreCuadro3))

#SEGUNDA FILA
texto_del_cuadro_rect4 = texto_del_cuadro_surface4.get_rect()
texto_del_cuadro_rect4.center = (posicionHijo(posicionPadreCuadro4))

texto_del_cuadro_rect5 = texto_del_cuadro_surface5.get_rect()
texto_del_cuadro_rect5.center = (posicionHijo(posicionPadreCuadro5))

texto_del_cuadro_rect6 = texto_del_cuadro_surface6.get_rect()
texto_del_cuadro_rect6.center = (posicionHijo(posicionPadreCuadro6))

#TERCERA FILA
texto_del_cuadro_rect7 = texto_del_cuadro_surface7.get_rect()
texto_del_cuadro_rect7.center = (posicionHijo(posicionPadreCuadro7))

texto_del_cuadro_rect8 = texto_del_cuadro_surface8.get_rect()
texto_del_cuadro_rect8.center = (posicionHijo(posicionPadreCuadro8))

texto_del_cuadro_rect9 = texto_del_cuadro_surface9.get_rect()
texto_del_cuadro_rect9.center = (posicionHijo(posicionPadreCuadro9))

#LIMPIAR TABLERO
#CUARTA FILA
texto_del_cuadro_rect10 = texto_del_cuadro_surface10.get_rect()
texto_del_cuadro_rect10.center = (posicionHijo(posicionPadreCuadro10,True))

#Bloque Padre Detectado por Eventos de PyGames
cuadroPadre1 = pygame.Rect(posicionPadreCuadro[0],posicionPadreCuadro[1], anchoXAltoCuadro[0],anchoXAltoCuadro[1])
cuadroPadre2 = pygame.Rect(posicionPadreCuadro2[0],posicionPadreCuadro2[1], anchoXAltoCuadro[0],anchoXAltoCuadro[1])
cuadroPadre3 = pygame.Rect(posicionPadreCuadro3[0],posicionPadreCuadro3[1], anchoXAltoCuadro[0],anchoXAltoCuadro[1])
cuadroPadre4 = pygame.Rect(posicionPadreCuadro4[0],posicionPadreCuadro4[1], anchoXAltoCuadro[0],anchoXAltoCuadro[1])
cuadroPadre5 = pygame.Rect(posicionPadreCuadro5[0],posicionPadreCuadro5[1], anchoXAltoCuadro[0],anchoXAltoCuadro[1])
cuadroPadre6 = pygame.Rect(posicionPadreCuadro6[0],posicionPadreCuadro6[1], anchoXAltoCuadro[0],anchoXAltoCuadro[1])
cuadroPadre7 = pygame.Rect(posicionPadreCuadro7[0],posicionPadreCuadro7[1], anchoXAltoCuadro[0],anchoXAltoCuadro[1])
cuadroPadre8 = pygame.Rect(posicionPadreCuadro8[0],posicionPadreCuadro8[1], anchoXAltoCuadro[0],anchoXAltoCuadro[1])
cuadroPadre9 = pygame.Rect(posicionPadreCuadro9[0],posicionPadreCuadro9[1], anchoXAltoCuadro[0],anchoXAltoCuadro[1])
cuadroPadre10 = pygame.Rect(posicionPadreCuadro10[0],posicionPadreCuadro10[1], anchoXAltoCuadro[0]+100,50)

def jugador(turno):
    if turno % 2 == 0:
        return "O"
    elif turno % 2 == 1:
        return "X"
#Variable que contea los Turnos del Juego
turno = 0
#Control de Bloques clickeados, solo debe de ser 1 vez
bloques_Hijos_Clickeados = {
    "1":[False,""],
    "2":[False,""],
    "3":[False,""],
    "4":[False,""],
    "5":[False,""],
    "6":[False,""],
    "7":[False,""],
    "8":[False,""],
    "9":[False,""],
}
#Funcion decididora si hay ganador
def ganar(bloques_Hijos_Clickeados):
    #SENTIDO HORIZONTAL
    if bloques_Hijos_Clickeados["1"][0] and bloques_Hijos_Clickeados["2"][0] and bloques_Hijos_Clickeados["3"][0]:
        if bloques_Hijos_Clickeados["1"][1] == "X" and bloques_Hijos_Clickeados["2"][1] == "X" and bloques_Hijos_Clickeados["3"][1]  == "X":
            return [True,"X"]
        elif bloques_Hijos_Clickeados["1"][1] == "O" and bloques_Hijos_Clickeados["2"][1] == "O" and bloques_Hijos_Clickeados["3"][1]  == "O":
            return [True,"O"]
    elif bloques_Hijos_Clickeados["4"][0] and bloques_Hijos_Clickeados["5"][0] and bloques_Hijos_Clickeados["6"][0]:
        if bloques_Hijos_Clickeados["4"][1] == "X" and bloques_Hijos_Clickeados["5"][1] == "X" and bloques_Hijos_Clickeados["6"][1]  == "X":
            return [True,"X"]
        elif bloques_Hijos_Clickeados["4"][1] == "O" and bloques_Hijos_Clickeados["5"][1] == "O" and bloques_Hijos_Clickeados["6"][1]  == "O":
            return [True,"O"]
    elif bloques_Hijos_Clickeados["7"][0] and bloques_Hijos_Clickeados["8"][0] and bloques_Hijos_Clickeados["9"][0]:
        if bloques_Hijos_Clickeados["7"][1] == "X" and bloques_Hijos_Clickeados["8"][1] == "X" and bloques_Hijos_Clickeados["9"][1]  == "X":
            return [True,"X"]
        elif bloques_Hijos_Clickeados["7"][1] == "O" and bloques_Hijos_Clickeados["8"][1] == "O" and bloques_Hijos_Clickeados["9"][1]  == "O":
            return [True,"O"]
    #SENTIDO VERTICAL
    if bloques_Hijos_Clickeados["7"][0] and bloques_Hijos_Clickeados["4"][0] and bloques_Hijos_Clickeados["1"][0]:
        if bloques_Hijos_Clickeados["7"][1] == "X" and bloques_Hijos_Clickeados["4"][1] == "X" and bloques_Hijos_Clickeados["1"][1]  == "X":
            return [True,"X"]
        elif bloques_Hijos_Clickeados["7"][1] == "O" and bloques_Hijos_Clickeados["4"][1] == "O" and bloques_Hijos_Clickeados["1"][1]  == "O":
            return [True,"O"]
    elif bloques_Hijos_Clickeados["8"][0] and bloques_Hijos_Clickeados["5"][0] and bloques_Hijos_Clickeados["2"][0]:
        if bloques_Hijos_Clickeados["8"][1] == "X" and bloques_Hijos_Clickeados["5"][1] == "X" and bloques_Hijos_Clickeados["2"][1]  == "X":
            return [True,"X"]
        elif bloques_Hijos_Clickeados["8"][1] == "O" and bloques_Hijos_Clickeados["5"][1] == "O" and bloques_Hijos_Clickeados["2"][1]  == "O":
            return [True,"O"]
    elif bloques_Hijos_Clickeados["9"][0] and bloques_Hijos_Clickeados["6"][0] and bloques_Hijos_Clickeados["3"][0]:
        if bloques_Hijos_Clickeados["9"][1] == "X" and bloques_Hijos_Clickeados["6"][1] == "X" and bloques_Hijos_Clickeados["3"][1]  == "X":
            return [True,"X"]
        elif bloques_Hijos_Clickeados["9"][1] == "O" and bloques_Hijos_Clickeados["6"][1] == "O" and bloques_Hijos_Clickeados["3"][1]  == "O":
            return [True,"O"]
    #SENTIDO X
    if bloques_Hijos_Clickeados["1"][0] and bloques_Hijos_Clickeados["5"][0] and bloques_Hijos_Clickeados["9"][0]:
        if bloques_Hijos_Clickeados["1"][1] == "X" and bloques_Hijos_Clickeados["5"][1] == "X" and bloques_Hijos_Clickeados["9"][1]  == "X":
            return [True,"X"]
        elif bloques_Hijos_Clickeados["1"][1] == "O" and bloques_Hijos_Clickeados["5"][1] == "O" and bloques_Hijos_Clickeados["9"][1]  == "O":
            return [True,"O"]
    elif bloques_Hijos_Clickeados["3"][0] and bloques_Hijos_Clickeados["5"][0] and bloques_Hijos_Clickeados["7"][0]:
        if bloques_Hijos_Clickeados["3"][1] == "X" and bloques_Hijos_Clickeados["5"][1] == "X" and bloques_Hijos_Clickeados["7"][1]  == "X":
            return [True,"X"]
        elif bloques_Hijos_Clickeados["3"][1] == "O" and bloques_Hijos_Clickeados["5"][1] == "O" and bloques_Hijos_Clickeados["7"][1]  == "O":
            return [True,"O"]
    return [False,""]
while True: # El juego entra en un Loop
    screen.fill(blanco)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
                if event.button == 1:
                    # `event.pos` is the mouse position.
                    if cuadroPadre1.collidepoint(event.pos) and bloques_Hijos_Clickeados["1"][0] == False:
                        # CAMBIAR DE LETRA A ESE CUADRO HIJO
                        texto_del_cuadro_surface1 = fuenteTexto.render(jugador(turno), parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_rect = texto_del_cuadro_surface1.get_rect()
                        texto_del_cuadro_rect.center = (posicionHijo(posicionPadreCuadro)) #Posicion del Cuadro
                        bloques_Hijos_Clickeados["1"][0] = True
                        bloques_Hijos_Clickeados["1"][1] = jugador(turno)
                        turno = turno+1
                    elif cuadroPadre2.collidepoint(event.pos) and bloques_Hijos_Clickeados["2"][0] == False:
                        # CAMBIAR DE LETRA A ESE CUADRO HIJO
                        texto_del_cuadro_surface2 = fuenteTexto.render(jugador(turno), parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_rect2 = texto_del_cuadro_surface2.get_rect()
                        texto_del_cuadro_rect2.center = (posicionHijo(posicionPadreCuadro2)) #Posicion del Cuadro
                        bloques_Hijos_Clickeados["2"][0] = True
                        bloques_Hijos_Clickeados["2"][1] = jugador(turno)
                        turno = turno+1
                    elif cuadroPadre3.collidepoint(event.pos) and bloques_Hijos_Clickeados["3"][0] == False:
                        # CAMBIAR DE LETRA A ESE CUADRO HIJO
                        texto_del_cuadro_surface3 = fuenteTexto.render(jugador(turno), parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_rect3 = texto_del_cuadro_surface3.get_rect()
                        texto_del_cuadro_rect3.center = (posicionHijo(posicionPadreCuadro3)) #Posicion del Cuadro
                        bloques_Hijos_Clickeados["3"][0] = True
                        bloques_Hijos_Clickeados["3"][1] = jugador(turno)
                        turno = turno+1
                    elif cuadroPadre4.collidepoint(event.pos) and bloques_Hijos_Clickeados["4"][0] == False:
                        # CAMBIAR DE LETRA A ESE CUADRO HIJO
                        texto_del_cuadro_surface4 = fuenteTexto.render(jugador(turno), parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_rect4 = texto_del_cuadro_surface4.get_rect()
                        texto_del_cuadro_rect4.center = (posicionHijo(posicionPadreCuadro4)) #Posicion del Cuadro
                        bloques_Hijos_Clickeados["4"][0] = True
                        bloques_Hijos_Clickeados["4"][1] = jugador(turno)
                        turno = turno+1
                    elif cuadroPadre5.collidepoint(event.pos) and bloques_Hijos_Clickeados["5"][0] == False:
                        # CAMBIAR DE LETRA A ESE CUADRO HIJO
                        texto_del_cuadro_surface5 = fuenteTexto.render(jugador(turno), parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_rect5 = texto_del_cuadro_surface5.get_rect()
                        texto_del_cuadro_rect5.center = (posicionHijo(posicionPadreCuadro5)) #Posicion del Cuadro
                        bloques_Hijos_Clickeados["5"][0] = True
                        bloques_Hijos_Clickeados["5"][1] = jugador(turno)
                        turno = turno+1
                    elif cuadroPadre6.collidepoint(event.pos) and bloques_Hijos_Clickeados["6"][0] == False:
                        # CAMBIAR DE LETRA A ESE CUADRO HIJO
                        texto_del_cuadro_surface6 = fuenteTexto.render(jugador(turno), parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_rect6 = texto_del_cuadro_surface6.get_rect()
                        texto_del_cuadro_rect6.center = (posicionHijo(posicionPadreCuadro6)) #Posicion del Cuadro
                        bloques_Hijos_Clickeados["6"][0] = True
                        bloques_Hijos_Clickeados["6"][1] = jugador(turno)
                        turno = turno+1
                    elif cuadroPadre7.collidepoint(event.pos) and bloques_Hijos_Clickeados["7"][0] == False:
                        # CAMBIAR DE LETRA A ESE CUADRO HIJO
                        texto_del_cuadro_surface7 = fuenteTexto.render(jugador(turno), parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_rect7 = texto_del_cuadro_surface7.get_rect()
                        texto_del_cuadro_rect7.center = (posicionHijo(posicionPadreCuadro7)) #Posicion del Cuadro
                        bloques_Hijos_Clickeados["7"][0] = True
                        bloques_Hijos_Clickeados["7"][1] = jugador(turno)
                        turno = turno+1
                    elif cuadroPadre8.collidepoint(event.pos) and bloques_Hijos_Clickeados["8"][0] == False:
                        # CAMBIAR DE LETRA A ESE CUADRO HIJO
                        texto_del_cuadro_surface8 = fuenteTexto.render(jugador(turno), parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_rect8 = texto_del_cuadro_surface8.get_rect()
                        texto_del_cuadro_rect8.center = (posicionHijo(posicionPadreCuadro8)) #Posicion del Cuadro
                        bloques_Hijos_Clickeados["8"][0] = True
                        bloques_Hijos_Clickeados["8"][1] = jugador(turno)
                        turno = turno+1
                    elif cuadroPadre9.collidepoint(event.pos) and bloques_Hijos_Clickeados["9"][0] == False:
                        # CAMBIAR DE LETRA A ESE CUADRO HIJO
                        texto_del_cuadro_surface9 = fuenteTexto.render(jugador(turno), parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_rect9 = texto_del_cuadro_surface9.get_rect()
                        texto_del_cuadro_rect9.center = (posicionHijo(posicionPadreCuadro9)) #Posicion del Cuadro
                        bloques_Hijos_Clickeados["9"][0] = True
                        bloques_Hijos_Clickeados["9"][1] = jugador(turno)
                        turno = turno+1
                    elif cuadroPadre10.collidepoint(event.pos):
                        #RESETEAR DICCIONARIO
                        bloques_Hijos_Clickeados = {
                            "1":[False,""],
                            "2":[False,""],
                            "3":[False,""],
                            "4":[False,""],
                            "5":[False,""],
                            "6":[False,""],
                            "7":[False,""],
                            "8":[False,""],
                            "9":[False,""],
                        }
                        #LIMPIAR TABLERO
                        texto_del_cuadro_surface1 = fuenteTexto.render("", parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_surface2 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_surface3 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_surface4 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_surface5 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_surface6 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_surface7 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_surface8 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_surface9 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        #PRIMERA FILA
                        texto_del_cuadro_rect = texto_del_cuadro_surface1.get_rect()
                        texto_del_cuadro_rect.center = (posicionHijo(posicionPadreCuadro)) #Posicion del Cuadro

                        texto_del_cuadro_rect2 = texto_del_cuadro_surface2.get_rect()
                        texto_del_cuadro_rect2.center = (posicionHijo(posicionPadreCuadro2))

                        texto_del_cuadro_rect3 = texto_del_cuadro_surface3.get_rect()
                        texto_del_cuadro_rect3.center = (posicionHijo(posicionPadreCuadro3))

                        #SEGUNDA FILA
                        texto_del_cuadro_rect4 = texto_del_cuadro_surface4.get_rect()
                        texto_del_cuadro_rect4.center = (posicionHijo(posicionPadreCuadro4))

                        texto_del_cuadro_rect5 = texto_del_cuadro_surface5.get_rect()
                        texto_del_cuadro_rect5.center = (posicionHijo(posicionPadreCuadro5))

                        texto_del_cuadro_rect6 = texto_del_cuadro_surface6.get_rect()
                        texto_del_cuadro_rect6.center = (posicionHijo(posicionPadreCuadro6))

                        #TERCERA FILA
                        texto_del_cuadro_rect7 = texto_del_cuadro_surface7.get_rect()
                        texto_del_cuadro_rect7.center = (posicionHijo(posicionPadreCuadro7))

                        texto_del_cuadro_rect8 = texto_del_cuadro_surface8.get_rect()
                        texto_del_cuadro_rect8.center = (posicionHijo(posicionPadreCuadro8))

                        texto_del_cuadro_rect9 = texto_del_cuadro_surface9.get_rect()
                        texto_del_cuadro_rect9.center = (posicionHijo(posicionPadreCuadro9))

                        #RESETEAR TURNO
                        turno = 0
                    if ganar(bloques_Hijos_Clickeados)[0] or turno == 9:
                        turno = turno+1
                        if ganar(bloques_Hijos_Clickeados)[0]:
                            ganador = ganar(bloques_Hijos_Clickeados)[1]
                            cantidad_de_turnos = str(round(turno/2))
                            messagebox.showinfo('Mensaje de Informacion','GANASTE JUGADOR '+ganador+" EN "+cantidad_de_turnos+" TURNOS :D\nJuego desarrollado por: Juan Serrano.")
                        #LIMPIAR TABLERO
                        texto_del_cuadro_surface1 = fuenteTexto.render("", parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_surface2 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_surface3 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_surface4 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_surface5 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_surface6 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_surface7 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_surface8 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        texto_del_cuadro_surface9 = fuenteTexto.render('', parametros_hijos[0],parametros_hijos[1],parametros_hijos[2])
                        #PRIMERA FILA
                        texto_del_cuadro_rect = texto_del_cuadro_surface1.get_rect()
                        texto_del_cuadro_rect.center = (posicionHijo(posicionPadreCuadro)) #Posicion del Cuadro

                        texto_del_cuadro_rect2 = texto_del_cuadro_surface2.get_rect()
                        texto_del_cuadro_rect2.center = (posicionHijo(posicionPadreCuadro2))

                        texto_del_cuadro_rect3 = texto_del_cuadro_surface3.get_rect()
                        texto_del_cuadro_rect3.center = (posicionHijo(posicionPadreCuadro3))

                        #SEGUNDA FILA
                        texto_del_cuadro_rect4 = texto_del_cuadro_surface4.get_rect()
                        texto_del_cuadro_rect4.center = (posicionHijo(posicionPadreCuadro4))

                        texto_del_cuadro_rect5 = texto_del_cuadro_surface5.get_rect()
                        texto_del_cuadro_rect5.center = (posicionHijo(posicionPadreCuadro5))

                        texto_del_cuadro_rect6 = texto_del_cuadro_surface6.get_rect()
                        texto_del_cuadro_rect6.center = (posicionHijo(posicionPadreCuadro6))

                        #TERCERA FILA
                        texto_del_cuadro_rect7 = texto_del_cuadro_surface7.get_rect()
                        texto_del_cuadro_rect7.center = (posicionHijo(posicionPadreCuadro7))

                        texto_del_cuadro_rect8 = texto_del_cuadro_surface8.get_rect()
                        texto_del_cuadro_rect8.center = (posicionHijo(posicionPadreCuadro8))

                        texto_del_cuadro_rect9 = texto_del_cuadro_surface9.get_rect()
                        texto_del_cuadro_rect9.center = (posicionHijo(posicionPadreCuadro9))
                        
                        #RESETEAR DICCIONARIO
                        bloques_Hijos_Clickeados = {
                            "1":[False,""],
                            "2":[False,""],
                            "3":[False,""],
                            "4":[False,""],
                            "5":[False,""],
                            "6":[False,""],
                            "7":[False,""],
                            "8":[False,""],
                            "9":[False,""],
                        }
                        turno = 0
                    # print(bloques_Hijos_Clickeados)
    # DIBUJA EN PANTALLA
    # DIBUJA LOS CUADROS PADRES
    pygame.draw.rect(screen,gris,cuadroPadre1)
    pygame.draw.rect(screen,gris,cuadroPadre2)
    pygame.draw.rect(screen,gris,cuadroPadre3)
    pygame.draw.rect(screen,gris,cuadroPadre4)
    pygame.draw.rect(screen,gris,cuadroPadre5)
    pygame.draw.rect(screen,gris,cuadroPadre6)
    pygame.draw.rect(screen,gris,cuadroPadre7)
    pygame.draw.rect(screen,gris,cuadroPadre8)
    pygame.draw.rect(screen,gris,cuadroPadre9)
    pygame.draw.rect(screen,gris,cuadroPadre10)
    # DIBUJA LOS CUADROS HIJOS CON TEXTO
    screen.blit(texto_del_cuadro_surface1, texto_del_cuadro_rect)
    screen.blit(texto_del_cuadro_surface2, texto_del_cuadro_rect2)
    screen.blit(texto_del_cuadro_surface3, texto_del_cuadro_rect3)
    screen.blit(texto_del_cuadro_surface4, texto_del_cuadro_rect4)
    screen.blit(texto_del_cuadro_surface5, texto_del_cuadro_rect5)
    screen.blit(texto_del_cuadro_surface6, texto_del_cuadro_rect6)
    screen.blit(texto_del_cuadro_surface7, texto_del_cuadro_rect7)
    screen.blit(texto_del_cuadro_surface8, texto_del_cuadro_rect8)
    screen.blit(texto_del_cuadro_surface9, texto_del_cuadro_rect9)
    screen.blit(texto_del_cuadro_surface10, texto_del_cuadro_rect10)

    pygame.display.update()
    fpsClock.tick(FPS)
