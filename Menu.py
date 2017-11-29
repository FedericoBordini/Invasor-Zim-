import pilasengine

pilas = pilasengine.iniciar()

class EscenaMenu(pilasengine.escenas.Escena):

    def iniciar(self):
        # Contenido de la escena principal: menu, fondo, logo del juego
        pilas.fondos.FondoMozaico("imagenes/universo5.jpg")
        self.menu_inicial()
        self.logo_juego()

    @staticmethod
    def logo_juego():
        # importamos logo desde carpeta imagenes
        imagen = pilas.imagenes.cargar("imagenes/invaderzim.png")
        logo = pilas.actores.Actor()
        logo.imagen = imagen
        logo.y = 130
        logo.x = 5

    def menu_inicial(self):
        # creamos opciones para el menu
        opciones = [
            ("Iniciar Invacion", self.iniciar_juego),
            ("Ayuda", self.pantalla_ayuda),
            ("Salir", self.salir_juego)
        ]
        self.menu = self.pilas.actores.Menu(opciones, y=1)

    def iniciar_juego(self):
        #Importamos el codigo del juego desde el archivo juego.py
        import juego

    def pantalla_ayuda(self):
        #Seleccionamos la escena Ayuda.
        self.pilas.escenas.Ayuda()

    def salir_juego(self):
        self.pilas.terminar()

# Vinculamos las escenas
pilas.escenas.vincular(EscenaMenu)

#Se inicia la escena
pilas.escenas.EscenaMenu()

pilas.ejecutar()
