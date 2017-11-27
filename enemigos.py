# coding=utf-8
# from pilasengine.actores.actor import pilasengine
import pilasengine

pilas = pilasengine.iniciar()

class Enemigos (pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = "imagenes/papas.jpg"
        self.escala = [0.5]
        self.aprender(pilas.habilidades.PuedeExplotar)
        self.x = pilas.azar(-200, 200)
        self.y = 300
        self.velocidad = pilas.azar(10, 60) / 10.0

    def actualizar(self):
        self.y -= self.velocidad

        # Elimina el objeto cuando sale de la pantalla.
        if self.y < -300:
            self.eliminar()
