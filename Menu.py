# coding: utf-8
import pilasengine

def iniciar_invacion():
    print("iniciar invacion")

def opciones_del_juego():
    print("opciones del juego...")

def salir_del_juego():
    print("Tengo que salir...")


pilas = pilasengine.iniciar()

pilas.actores.Menu(
        [
            ('iniciar invacion', iniciar_invacion),
            ('opciones',opciones_del_juego),
            ('salir', salir_del_juego),
        ])

FondoMenu = pilas.fondos.Fondo()
FondoMenu.imagen = pilas.imagenes.cargar('imagenes/invader_zim.jpg')
texto = pilas.actores.Texto("Invazor Zim")
texto.x = 20
texto.y = 100
texto.color = pilas.colores.Color(0, 255, 0)
texto.escala = 3
fondo.imagen.repetir_vertical = True
fondo.imagen.repetir_horizontal = True
pilas.ejecutar()
