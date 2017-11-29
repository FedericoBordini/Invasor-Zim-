 # -*- coding: utf-8
import pilasengine

from fondo import Fondo
from nave import NaveZim
from enemigos import Enemigos


pilas = pilasengine.iniciar()

puntaje = pilas.actores.Puntaje(280, 200, color=pilas.colores.blanco)

# Crear el Fondo Personalizado----------------------------------
fondo = Fondo(pilas)
fondo.dy = -5
#---------------------------------------------------------------
# Crear Enemigos (Asteroides)-----------------------------------
enemigos = pilas.actores.Grupo()

def crear_enemigo():
    actor = Enemigos(pilas)
    enemigos.agregar(actor)

pilas.tareas.siempre(0.65, crear_enemigo)
#----------------------------------------------------------------

# Crear NAVE------------------------------------------------------
nave = NaveZim(pilas)
nave.aprender(pilas.habilidades.LimitadoABordesDePantalla)
nave.escala = 0.2
nave.definir_enemigos(enemigos, puntaje.aumentar)
#-----------------------------------------------------------------

def perder(nave, enemigos):

    pilas.colisiones.agregar(nave, enemigos, nave.eliminar)
    pilas.camara.vibrar()
    pilas.camara.vibrar(intensidad=3.5, tiempo=2)
    texto1 = pilas.actores.Texto("PERDISTE")
    texto1.y = 380 ;
    texto1.x = -220 ;
    texto1.escala = 1.2 ;
    texto1.color = "negro"

pilas.colisiones.agregar(nave, enemigos, perder)

pilas.actores.vincular(NaveZim)
pilas.actores.vincular(Enemigos)

pilas.ejecutar()
