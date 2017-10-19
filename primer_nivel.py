import pilasengine

pilas = pilasengine.iniciar()

Fondo = pilas.fondos.Fondo()
Fondo.imagen = pilas.imagenes.cargar('imagenes/galaxia1.jpg')
Fondo.escala = [3]
Fondo.x = [400]
Fondo.y = [400]


actor = pilas.actores.Actor()
actor.imagen = "imagenes/nave1.png"
actor.escala = [0.1]
actor.aprender("MoverseComoCoche")
actor.aprender("RotarConMouse")
actor.aprender("Disparar", angulo_salida_disparo=90)


pilas.ejecutar()
