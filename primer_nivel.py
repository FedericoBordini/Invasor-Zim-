# -*- coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()

puntaje = pilas.actores.Puntaje(-280, 200, color=pilas.colores.blanco)


class  Enemigo (pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = "imagenes/did.png"
        self.escala = [0.1]
        self.aprender( pilas.habilidades.PuedeExplotarConHumo )
        self.x = pilas.azar(-250, 250)
        self.y = 550
        self.velocidad = pilas.azar(10, 30) / 7.0

    def actualizar(self):
        self.y -= self.velocidad

        # Elimina el objeto cuando sale de la pantalla.
        if self.y < -300:
            self.eliminar()

fondo = pilas.fondos.Galaxia(dy=-5)

enemigos = pilas.actores.Grupo()

def crear_enemigo():
    actor = Enemigo(pilas)
    enemigos.agregar(actor)

pilas.tareas.siempre(0.5, crear_enemigo)
