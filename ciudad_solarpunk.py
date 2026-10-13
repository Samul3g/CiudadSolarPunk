import turtle
import os
import math
import random
import time


'''Sección de paleta de colores, se definen los valores RGB a usar en edificios, techos y puertas'''

color_ventana= (160, 210, 230)

color_edificios = [
    (235, 230, 215), # Piedra Caliza
    (145, 155, 160), # Gris Concreto
    (190, 110, 90),  # Ladrillo
    (70, 80, 90),    # Pizarra
    (235, 230, 215), # Crema Caliza
    (145, 155, 160), # Gris Hormigón
    (190, 110, 90),  # Ladrillo Rojo
    (70, 80, 90),    # Pizarra Oscura
    (210, 180, 140), # Arena Desértica
    (105, 105, 105), # Grafito Industrial
    (245, 245, 220), # Beige Tradicional
    (85, 107, 47),   # Verde Olivo Seco
    (255, 250, 240), # Blanco Floral
    (112, 128, 144), # Gris Pizarra Claro
    (188, 143, 143), # Adobe Rosáceo
    (222, 184, 135), # Madera Clara
    (47, 79, 79),    # Gris Pizarra Oscuro
    (255, 248, 220), # Crema Cálido
    (139, 69, 19),   # Marrón Revestimiento
    (200, 200, 200), # Plata Mate
    (176, 196, 222), # Azul Acero Pálido
    (160, 82, 45),   # Siena Tostado
    (240, 230, 140), # Caqui
    (176, 143, 124), # Terracota Suave
    (119, 136, 153), # Gris Humo
    (211, 211, 211), # Gris Perla
    (250, 235, 215), # Blanco Antiguo
    (128, 128, 0),   # Oliva Oscuro
    (102, 102, 102), # Granito
    (218, 165, 32),  # Ocre Dorado
    (255, 228, 196)  # Galleta
]

color_techos = [
    (140, 60, 50),   # Teja
    (45, 45, 50),    # Carbón
    (90, 105, 85),   # Musgo
    (140, 60, 50),   # Teja de Barro
    (45, 45, 50),    # Zinc / Carbón
    (90, 105, 85),   # Techo Verde / Musgo
    (120, 130, 140), # Plomo Mate
    (180, 100, 50),  # Terracota Brillante
    (70, 40, 30),    # Chocolate Profundo
    (110, 127, 128), # Cobre Oxidado
    (60, 60, 60),    # Asfalto Moderno
    (139, 0, 0),     # Rojo Sangre Teja
    (119, 136, 153), # Pizarra Azulada
    (107, 142, 35),  # Verde Oliva Denso
    (192, 192, 192), # Galvanizado
    (165, 42, 42),   # Barro Cocido
    (46, 139, 87),   # Cobre Envejecido
    (25, 25, 112),   # Azul Medianoche
    (218, 165, 32),  # Paja Seca
    (0, 0, 0),       # Negro Obsidiana
    (85, 85, 85),    # Gris Bitumen
    (101, 67, 33),   # Marrón Corteza
    (128, 0, 0),     # Granate Techo
    (112, 128, 144), # Acero Mate
    (85, 107, 47),   # Liquen Oscuro
    (139, 69, 19),   # Arcilla Tostada
    (47, 79, 79),    # Pizarra Marina
]

color_puertas = [
    (110, 70, 45),   # Madera
    (35, 65, 100),   # Azul Real
    (110, 70, 45),   # Madera Roble
    (35, 65, 100),   # Azul Naval
    (20, 80, 45),    # Verde Bosque
    (150, 40, 30),   # Bermellón Intenso
    (240, 200, 60),  # Amarillo Mostaza
    (50, 50, 50),    # Negro Carbón
    (210, 210, 210), # Aluminio Pulido
    (90, 50, 40),    # Caoba Oscuro
    (135, 150, 160), # Acero Azulado
    (128, 0, 0),     # Granate Elegante
    (0, 128, 128),   # Teal
    (255, 127, 80),  # Coral Vivo
    (245, 222, 179), # Madera Trigo
    (72, 61, 139),   # Pizarra Oscuro
    (105, 105, 105), # Gris Dim
    (184, 115, 51),  # Cobre Pulido
    (255, 255, 255), # Blanco Puro
    (85, 107, 47),   # Verde Olivo Oscuro
    (123, 63, 0),    # Chocolate Tradicional
    (25, 25, 25),    # Negro Mate
    (65, 105, 225),  # Azul Real Brillante
    (34, 139, 34),   # Verde Hierba
    (178, 34, 34),   # Rojo Ladrillo
    (218, 165, 32),  # Bronce Antiguo
    (255, 215, 0),   # Oro Satinado
    (47, 79, 79),    # Gris Carbón profundo
]

# Variables globales

## Matriz de rotación de cosenos
cosenos = [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]

## Distancia focal utilizada para la perspectiva
distancia_focal = 750 

## Posición (x, y, z) dentro del mundo.

#           x, y, z
posición = [0, 0, 0]


def desactivar_pluma():
    """
    Desactiva la pluma para mover la tortuga sin que se vea la raya
    """
    turtle.penup()

def activar_pluma():
    """
    Activa la pluma para mover la tortuga y que la raya se vea
    """
    turtle.pendown()

def virar(angulo):
    """
    Función para virar la tortuga de acuerdo al eje Z

    E: Recibe la cantidad de grados a virar
    S: Modifica la matriz de cosenos
    """

    cos_angulo = math.cos(math.radians(angulo))
    sen_angulo = math.sin(math.radians(angulo))

    a = cosenos[0][0] * cos_angulo + cosenos[1][0] * sen_angulo
    b = cosenos[0][1] * cos_angulo + cosenos[1][1] * sen_angulo
    c = cosenos[0][2] * cos_angulo + cosenos[1][2] * sen_angulo
    d = cosenos[1][0] * cos_angulo - cosenos[0][0] * sen_angulo
    e = cosenos[1][1] * cos_angulo - cosenos[0][1] * sen_angulo
    f = cosenos[1][2] * cos_angulo - cosenos[0][2] * sen_angulo

    cosenos[0][0] = a
    cosenos[0][1] = b
    cosenos[0][2] = c
    cosenos[1][0] = d
    cosenos[1][1] = e
    cosenos[1][2] = f


def cabecear(angulo):
    """
    Función para virar la tortuga de acuerdo al eje -X

    E: Recibe la cantidad de grados a cabecear
    S: Modifica la matriz de cosenos
    """

    cos_angulo = math.cos(math.radians(angulo))
    sen_angulo = math.sin(math.radians(angulo))

    a = cosenos[0][0] * cos_angulo - cosenos[2][0] * sen_angulo
    b = cosenos[0][1] * cos_angulo - cosenos[2][1] * sen_angulo
    c = cosenos[0][2] * cos_angulo - cosenos[2][2] * sen_angulo
    d = cosenos[2][0] * cos_angulo + cosenos[0][0] * sen_angulo
    e = cosenos[2][1] * cos_angulo + cosenos[0][1] * sen_angulo
    f = cosenos[2][2] * cos_angulo + cosenos[0][2] * sen_angulo

    cosenos[0][0] = a
    cosenos[0][1] = b
    cosenos[0][2] = c
    cosenos[2][0] = d
    cosenos[2][1] = e
    cosenos[2][2] = f

def rolar(angulo):
    """
    Función para virar la tortuga de acuerdo al eje Y

    E: Recibe la cantidad de grados a rolar
    S: Modifica la matriz de cosenos
    """

    cos_angulo = math.cos(math.radians(angulo))
    sen_angulo = math.sin(math.radians(angulo))

    a = cosenos[1][0] * cos_angulo + cosenos[2][0] * sen_angulo
    b = cosenos[1][1] * cos_angulo + cosenos[2][1] * sen_angulo
    c = cosenos[1][2] * cos_angulo + cosenos[2][2] * sen_angulo
    d = cosenos[2][0] * cos_angulo - cosenos[1][0] * sen_angulo
    e = cosenos[2][1] * cos_angulo - cosenos[1][1] * sen_angulo
    f = cosenos[2][2] * cos_angulo - cosenos[1][2] * sen_angulo

    cosenos[1][0] = a    
    cosenos[1][1] = b
    cosenos[1][2] = c
    cosenos[2][0] = d
    cosenos[2][1] = e
    cosenos[2][2] = f

def andar(distancia):
    """
    Avanza la tortuga de acuerdo a la distancia indicada, la distancia está
    indicada en unidades de avance de la tortuga
    
    E: Ingresa la cantidad de unidades a caminar por la tortuga
    S: Mueve la tortuga y actualiza la posición global
    """

    global posición

    nuevo_x = posición[0] + distancia * cosenos[0][0]
    nuevo_y = posición[1] + distancia * cosenos[0][1]
    nuevo_z = posición[2] + distancia * cosenos[0][2]

    posición = [nuevo_x, nuevo_y, nuevo_z]

    graficar(nuevo_x, nuevo_y, nuevo_z)

def graficar(x, y, z):
    """
    Recibe las coordenadas (x, y, z) del punto al que se debe mover la
    tortuga, al mismo tiempo que reliza la proyección 3D a 2D mediante el
    uso de la distancia focal.

    E: posición en el eje x
       posición en el eje y
       posición en el eje z

    S: La tortuga en una nueva posición
    """
    
    nuevo_x = (distancia_focal * x) / (distancia_focal - z)
    nuevo_y = (distancia_focal * y) / (distancia_focal - z)

    turtle.goto(nuevo_x, nuevo_y)


def teletransportar(x, y, z):
    """
    Mueve la tortuga a una posición (x, y, z) realizando la proyección
    3D->2D con la distancia focal
    """
    
    nuevo_x = (distancia_focal * x) / (distancia_focal - z)
    nuevo_y = (distancia_focal * y) / (distancia_focal - z)

    turtle.penup()
    turtle.teleport(nuevo_x, nuevo_y)
    turtle.pendown()



### Ejes de la triada
def ejes_triada(distancia):

    global posición

    x = posición[0]
    y = posición[1]
    z = posición[2]

    turtle.pencolor("red")
    graficar(x + distancia*cosenos[0][0], y + distancia* cosenos[0][1], z + distancia*cosenos[0][2] )
    teletransportar(*posición)
    

    turtle.pencolor("blue")
    graficar(x + distancia*cosenos[1][0], y + distancia* cosenos[1][1], z + distancia*cosenos[1][2] )
    teletransportar(*posición)

    turtle.pencolor("green")
    graficar(x + distancia*cosenos[2][0], y + distancia* cosenos[2][1], z + distancia*cosenos[2][2] )
    teletransportar(*posición)

    turtle.pencolor("black")

# Funciones de movimiento


def dibujar(lista):

    """ E: Una lista con coordenadas [x, y, z]
    R: Toma una lista con 3 valores tipo int
    S: Actualiza la posición global y dibuja una línea hasta ese punto"""
    
    if type(lista)!= list: 
        return "Error01"

    if len(lista) != 3:
        return "Error02"

    if es_num(lista) == False:
        return "Error03"
    else:
        return dibujar_aux(lista)

def dibujar_aux(lista):

    global posición
    posición = [lista[0], lista[1], lista[2]] 
    graficar(lista[0], lista[1], lista[2])

def viajar(lista):

    """ E: Una lista con coordenadas [x, y, z]
    R: Toma una lista con 3 valores tipo int
    S: Teletransporta la posición global y la tortuga a dicho punto"""
    
    if type(lista)!= list: 
        return "Error04"

    if len(lista) != 3:
        return "Error05"

    if es_num(lista) == False:
        return "Error06"
    else:
        return viajar_aux(lista)

def viajar_aux(lista):

    global posición
    posición = [lista[0], lista[1], lista[2]] 
    teletransportar(lista[0], lista[1], lista[2])

def es_num(lista):

    '''E: Lista
    R: Solo toma valores tipo lista
    S: True si la lista contiene solo int, False si la lista contiene otro tipo de valor '''

    if type(lista)!= list:
        return "Error 07"

    else:
        return es_int_aux(lista)

def es_int_aux(lista):

    if lista == []:
        return True
        
    if type(lista[0]) != int and type(lista[0]) != float:
        return False

    else:
        return es_int_aux(lista[1:])




# --- Funciones de Formas Geométricas ---

def cuadro(altura, ancho):

    """E: Int de altura y ancho
    R: Toma valores solo tipo int y float
    S: Calcula los vértices de un cuadro sin dibujarlo, retorna la lista de puntos """

    if (type(altura) != int and type(altura) != float) or (type(ancho) != int and type(ancho) != float):
        return "Error 08"

    else: 
        return cuadro_aux(altura, ancho)

def cuadro_aux(altura, ancho):

    desactivar_pluma()
    puntoA = posición
    virar(90)
    andar(altura)
    puntoB = posición
    virar(-90)
    andar(ancho)
    puntoC = posición
    virar(-90)
    andar(altura)
    puntoD = posición
    virar(-90)
    andar(ancho)
    virar(180)
    activar_pluma()
    return [puntoA, puntoB, puntoC, puntoD]


def dibujar_cuadro(altura, ancho):

    """E: Int de altura y ancho
    R: Toma valores solo tipo int o float
    S: Dibuja un cuadro en la posición actual y retorna sus vértices."""

    if (type(altura) != int and type(altura) != float) or (type(ancho) != int and type(ancho) != float):
        return "Error 09"

    else: 
        return dibujar_cuadro_aux(altura, ancho)

def dibujar_cuadro_aux(altura, ancho):

    puntoA = posición
    virar(90)
    andar(altura)
    puntoB = posición
    virar(-90)
    andar(ancho)
    puntoC = posición
    virar(-90)
    andar(altura)
    puntoD = posición
    virar(-90)
    andar(ancho)
    return [puntoA, puntoB, puntoC, puntoD]

def triangulo(altura, ancho):

    """E: Int de altura y ancho
    R: Toma valores solo tipo int o float
    S: Calcula los puntos de un triángulo sin dibujarlo, retorna los vértices."""
    
    if (type(altura) != int and type(altura) != float) or (type(ancho) != int and type(ancho) != float):
        return "Error 10"

    else: 
        return triangulo_aux(altura, ancho)


def triangulo_aux(altura, ancho):

    desactivar_pluma()
    puntoA = posición
    andar(ancho)
    puntoB = posición
    andar(-(ancho/2))
    virar(-90); andar(-altura)
    puntoC = posición
    virar(90)
    activar_pluma()
    return [puntoA, puntoB, puntoC]

def dibujar_triangulo(altura, ancho):

    """E: Int de altura y ancho
    R: Toma valores solo tipo int o float
    S: Dibuja un triángulo y retorna sus vértices."""
    
    if (type(altura) != int and type(altura) != float) or (type(ancho) != int and type(ancho) != float):
        return "Error 10"

    else: 
        return dibujar_triangulo_aux(altura, ancho)

def dibujar_triangulo_aux(altura, ancho):

    puntoA = posición
    andar(ancho)
    puntoB = posición
    andar(-(ancho/2))
    virar(-90)
    desactivar_pluma()
    andar(-altura)
    puntoC = posición
    activar_pluma()
    dibujar(puntoA)
    viajar(puntoC)
    dibujar(puntoB)
    dibujar(puntoA)
    virar(90)
    return [puntoA, puntoB, puntoC]


# --- Modelado de Edificios ---

def edificio1(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo, color_apoyo):

    '''E: Altura int, Ancho int, color de ventana RGB, color de edificio RGB, color de puerta RGB,
    color de techo RGB, color de apoyo RGB
    R: Solo acepta valores tipo int o float
    en Ancho y Altura y solor de tipo RGB para turtle en las demas entradas
    S: El edificio 1 con medidas y colores acordes a los parametros dados'''

    if type(altura) != int or type(ancho) != int: 
        return "Error 11"

    if (type(color_ventana) != tuple or type(color_edificio) != tuple or type(color_puerta) != tuple or
    type(color_techo) != tuple or type(color_apoyo) != tuple) :
        return "Error 12"

    if (len(color_ventana) != 3 or len(color_edificio) != 3 or len(color_puerta) != 3 or
    len(color_techo) != 3 or len(color_apoyo) != 3):
        return "Error 13"

    else:
        return edificio1_aux(altura,ancho, color_ventana, color_edificio, color_puerta, 
        color_techo, color_apoyo)

    

def edificio1_aux(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo, color_apoyo):

    ini=posición

    turtle.fillcolor(color_edificio)
    turtle.begin_fill()
    cuerpo = dibujar_cuadro(altura, ancho)
    turtle.end_fill()
    viajar(cuerpo[0])
    virar(-90)
    andar(altura*0.7)
    virar(-90)
    desactivar_pluma()
    andar(ancho*0.1)
    activar_pluma()

    ventana1 = cuadro(altura*0.2, ancho*0.2)
    
    viajar(ventana1[1])
    dibujar(ventana1[2])
    viajar(ventana1[3])
    dibujar(ventana1[0])
    andar(ancho*0.03)
    turtle.fillcolor(color_ventana)
    turtle.begin_fill()
    dibujar_cuadro(altura*0.2, ancho*0.14)
    turtle.end_fill()
    


    viajar(ventana1[3])
    virar(-180)
    desactivar_pluma()
    andar(ancho*0.4)
    activar_pluma()

    ventana2 = cuadro(altura*0.2, ancho*0.2)
    viajar(ventana2[1])
    dibujar(ventana2[2])
    viajar(ventana2[3])
    dibujar(ventana2[0])
    andar(ancho*0.03)
    turtle.begin_fill()
    dibujar_cuadro(altura*0.2, ancho*0.14)
    turtle.end_fill()


    viajar(cuerpo[0])
    desactivar_pluma()
    virar(180)
    andar(ancho*0.5)
    activar_pluma()
    turtle.fillcolor(color_puerta)
    turtle.begin_fill()
    dibujar_cuadro(altura*0.3, ancho*0.1)
    desactivar_pluma()
    andar(ancho*0.1)
    virar(180); activar_pluma()
    dibujar_cuadro(altura*0.3, ancho*0.1)
    turtle.end_fill()

    viajar(cuerpo[1])
    virar(180)
    andar(ancho*-0.1)
    turtle.fillcolor(color_apoyo)
    turtle.begin_fill()
    techito = dibujar_cuadro(altura*0.1, ancho*1.2)
    turtle.end_fill()
    viajar(techito[1])
    virar(180)
    andar(ancho*0.1)
    turtle.fillcolor(color_techo)
    turtle.begin_fill()
    dibujar_triangulo(altura*0.5, ancho)
    turtle.end_fill()

    return ini


def edificio2(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo, color_apoyo):

    '''E: Altura int, Ancho int, color de ventana RGB, color de edificio RGB, color de puerta RGB,
    color de techo RGB, color de apoyo RGB
    R: Solo acepta valores tipo int o float
    en Ancho y Altura y solor de tipo RGB para turtle en las demas entradas
    S: El edificio 2 con medidas y colores acordes a los parametros dados'''

    if type(altura) != int or type(ancho) != int: 
        return "Error 14"

    if (type(color_ventana) != tuple or type(color_edificio) != tuple or type(color_puerta) != tuple or
    type(color_techo) != tuple or type(color_apoyo) != tuple):
        return "Error 15"

    if (len(color_ventana) != 3 or len(color_edificio) != 3 or len(color_puerta) != 3 or
    len(color_techo) != 3 or len(color_apoyo) != 3):
        return "Error 16"

    else:
        return edificio2_aux(altura,ancho, color_ventana, color_edificio, color_puerta, 
        color_techo, color_apoyo)
        
def edificio2_aux(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo, color_apoyo):

    ini=posición


    turtle.fillcolor(color_edificio)
    turtle.begin_fill()
    cuerpo = dibujar_cuadro(altura, ancho*1.8)
    turtle.end_fill()
    desactivar_pluma()
    virar(180)
    andar(ancho*0.4)
    activar_pluma()
    turtle.fillcolor(color_puerta)
    turtle.begin_fill()
    dibujar_cuadro(altura*0.3, ancho*0.5)
    virar(180); desactivar_pluma()
    andar(ancho*0.5)
    activar_pluma()

    dibujar_cuadro(altura*0.3, ancho*0.5)
    turtle.end_fill()
    
    viajar(cuerpo[0])
    desactivar_pluma()
    virar(-90)
    andar(altura*0.4)
    virar(-90)
    andar(ancho*0.2)
    activar_pluma()

    turtle.fillcolor(color_apoyo)
    turtle.begin_fill()
    ventanal1 = dibujar_cuadro(altura*0.05, ancho*1.4)
    turtle.end_fill()
    viajar(ventanal1[1])
    desactivar_pluma()
    virar(180); andar(ancho*0.075)
    turtle.fillcolor(color_ventana)
    turtle.begin_fill()
    activar_pluma()
    dibujar_cuadro(altura*0.2, ancho*0.25)
    virar(180); andar(ancho*0.5)
    dibujar_cuadro(altura*0.2, ancho*0.25)
    virar(180); andar(ancho*0.5)
    dibujar_cuadro(altura*0.2, ancho*0.25)
    turtle.end_fill()
    

    viajar(cuerpo[0])
    desactivar_pluma()
    virar(-90)
    andar(altura*0.65)
    virar(-90)
    andar(ancho*0.2)
    activar_pluma()
    
    turtle.fillcolor(color_apoyo)
    turtle.begin_fill()
    ventanal1 = dibujar_cuadro(altura*0.05, ancho*1.4)
    turtle.end_fill()
    viajar(ventanal1[1])
    desactivar_pluma()
    virar(180); andar(ancho*0.075)
    turtle.fillcolor(color_ventana)
    turtle.begin_fill()
    activar_pluma()
    dibujar_cuadro(altura*0.2, ancho*0.25)
    virar(180); andar(ancho*0.5)
    dibujar_cuadro(altura*0.2, ancho*0.25)
    virar(180); andar(ancho*0.5)
    dibujar_cuadro(altura*0.2, ancho*0.25)
    turtle.end_fill()

    viajar(cuerpo[2])
    desactivar_pluma()
    andar(ancho*-0.1)
    activar_pluma()
    virar(-90)
    turtle.fillcolor(color_techo)
    turtle.begin_fill()
    dibujar_cuadro(ancho*2, altura*0.1)
    turtle.end_fill()
    virar(90)

    return ini

def edificio3(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo, color_apoyo):

    '''E: Altura int, Ancho int, color de ventana RGB, color de edificio RGB, color de puerta RGB,
    color de techo RGB, color de apoyo RGB
    R: Solo acepta valores tipo int o float
    en Ancho y Altura y solor de tipo RGB para turtle en las demas entradas
    S: El edificio 3 con medidas y colores acordes a los parametros dados'''

    if type(altura) != int or type(ancho) != int: 
        return "Error 17"

    if (type(color_ventana) != tuple or type(color_edificio) != tuple or type(color_puerta) != tuple or
    type(color_techo) != tuple or type(color_apoyo) != tuple):
        return "Error 18"

    if (len(color_ventana) != 3 or len(color_edificio) != 3 or len(color_puerta) != 3 or
    len(color_techo) != 3 or len(color_apoyo) != 3):
        return "Error 19"

    else:
        return edificio3_aux(altura,ancho, color_ventana, color_edificio, color_puerta, 
        color_techo, color_apoyo)


def edificio3_aux(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo, color_apoyo):

    ini=posición
    turtle.fillcolor(color_edificio)
    turtle.begin_fill()
    cuerpo= dibujar_cuadro(altura, ancho)
    turtle.end_fill()
    viajar(cuerpo[1])


    virar(180)
    turtle.fillcolor(color_techo)
    turtle.begin_fill()
    techito= cuadro(altura*0.2, ancho)
    viajar(techito[1])
    dibujar(techito[2])


    
    viajar(cuerpo[2])
    andar(ancho*-0.2)
    borde1= triangulo(altura*0.2, ancho*0.4)
    dibujar(borde1[2])
    dibujar(borde1[1])
    dibujar(borde1[0])

    viajar(cuerpo[1])
    andar(ancho*-0.2)
    borde2= triangulo(altura*0.2, ancho*0.4)
    desactivar_pluma()
    dibujar(borde2[1])
    activar_pluma()
    dibujar(borde2[0])
    dibujar(borde2[2])

    turtle.end_fill()



    viajar(cuerpo[0])
    andar(ancho*0.1)
    virar(-90)
    desactivar_pluma()
    andar(altura*-0.2)
    activar_pluma()
    virar(-90)
    turtle.fillcolor(color_apoyo)
    turtle.begin_fill()
    maseta1_1=triangulo(altura*0.2, ancho*0.05)
    viajar(maseta1_1[2])
    dibujar(maseta1_1[1])
    dibujar(maseta1_1[0])
    viajar(maseta1_1[2])
    virar(180)
    maseta1_2=cuadro(altura*0.2, ancho*0.25)
    viajar(maseta1_2[1])
    dibujar(maseta1_2[2])
    virar(180)
    turtle.end_fill()
    maseta1_3=triangulo(altura*0.2, ancho*0.05)
    dibujar(maseta1_3[0])



    viajar(cuerpo[3])
    virar(180)
    andar(ancho*-0.3)
    virar(-90)
    desactivar_pluma()
    andar(altura*-0.2)
    activar_pluma()
    virar(-90)
    turtle.begin_fill()
    maseta2_1=triangulo(altura*0.2, ancho*0.05)
    viajar(maseta2_1[2])
    dibujar(maseta2_1[1])
    dibujar(maseta2_1[0])
    viajar(maseta2_1[2])
    virar(180)
    maseta2_2=cuadro(altura*0.2, ancho*0.25)
    viajar(maseta2_2[1])
    dibujar(maseta2_2[2])
    virar(180)
    turtle.end_fill()
    maseta2_3=triangulo(altura*0.2, ancho*0.05)
    dibujar(maseta2_3[0])
    dibujar(maseta2_3[1])

    viajar(cuerpo[0])
    virar(180)
    andar(ancho*0.5)
    turtle.fillcolor(color_puerta)
    turtle.begin_fill()
    dibujar_cuadro(altura*0.4, ancho*0.1)
    andar(ancho*0.1)
    virar(180)
    dibujar_cuadro(altura*0.4, ancho*0.1)
    turtle.end_fill()

    viajar(maseta1_1[1])
    virar(-90)
    desactivar_pluma()
    andar(altura*0.2)

    virar(-90)
    andar(ancho*0.05)

    turtle.fillcolor(color_techo)
    turtle.begin_fill()
    borde3=triangulo(altura*0.1, ancho*0.1)
    dibujar(borde3[0])
    dibujar(borde3[1])
    andar(ancho*-0.05)
    techo=cuadro(altura*0.1, ancho*0.75)
    dibujar(techo[3])
    viajar(techo[1])
    dibujar(techo[2])
    dibujar(techo[1])


    viajar(techo[3])
    andar(ancho*-0.05)
    borde3=triangulo(altura*0.1, ancho*0.1)
    dibujar(borde3[1])
    dibujar(borde3[0])
    turtle.end_fill()


    viajar(cuerpo[0])


    turtle.fillcolor(color_ventana)
    virar(90)
    andar(altura*0.55)
    virar(-90)
    desactivar_pluma()
    andar(ancho*0.2)
    activar_pluma()
    turtle.begin_fill()
    dibujar_cuadro(altura*0.125,ancho*0.125 )
    virar(-90)
    desactivar_pluma()
    andar(altura*0.15)
    activar_pluma()
    virar(-90)
    dibujar_cuadro(altura*0.125,ancho*0.125 )
    virar(-90)
    desactivar_pluma()
    andar(altura*0.15)
    activar_pluma()
    virar(-90)
    dibujar_cuadro(altura*0.125,ancho*0.125 )
    turtle.end_fill()


    viajar(cuerpo[3])
    virar(-90)
    andar(altura*0.55)
    virar(-90)
    desactivar_pluma()
    andar(ancho*-0.3)
    activar_pluma()
    turtle.begin_fill()
    dibujar_cuadro(altura*0.125,ancho*0.125 )
    virar(-90)
    desactivar_pluma()
    andar(altura*0.15)
    activar_pluma()
    virar(-90)
    dibujar_cuadro(altura*0.125,ancho*0.125 )
    virar(-90)
    desactivar_pluma()
    andar(altura*0.15)
    activar_pluma()
    virar(-90)
    dibujar_cuadro(altura*0.125,ancho*0.125 )
    virar(180)
    turtle.end_fill()

    return ini


def edificio4(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo):

    '''E: Altura int, Ancho int, color de ventana RGB, color de edificio RGB, color de puerta RGB,
    color de techo RGB, color de apoyo RGB
    R: Solo acepta valores tipo int o float
    en Ancho y Altura y solor de tipo RGB para turtle en las demas entradas
    S: El edificio 4 con medidas y colores acordes a los parametros dados'''

    if type(altura) != int or type(ancho) != int: 
        return "Error 20"

    if (type(color_ventana) != tuple or type(color_edificio) != tuple or type(color_puerta) != tuple or
    type(color_techo) != tuple):
        return "Error 21"

    if (len(color_ventana) != 3 or len(color_edificio) != 3 or len(color_puerta) != 3 or
    len(color_techo) != 3):
        return "Error 22"

    else:
        return edificio4_aux(altura,ancho, color_ventana, color_edificio, color_puerta, 
        color_techo)


def edificio4_aux(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo):

    ini=posición

    turtle.fillcolor(color_edificio)
    turtle.begin_fill()
    cuerpo = cuadro(altura, ancho)
    viajar(cuerpo[3])
    dibujar(cuerpo[2])
    viajar(cuerpo[1])
    viajar(cuerpo[1])
    virar(90); andar(altura*-0.256)

    viajar(cuerpo[0])
    virar(-90)
    desactivar_pluma()
    andar(ancho*-0.4)
    activar_pluma()
    
    cuerpo2 = cuadro(altura*0.7, ancho*0.55)
    turtle.end_fill()

    dibujar(cuerpo2[1])
    viajar(cuerpo2[2])
    dibujar(cuerpo2[3])
    viajar(cuerpo2[1])
    virar(90)
    andar(altura*0.17)
    virar(180)

    turtle.begin_fill()
    techito = triangulo(ancho*0.55, altura*0.35)
    turtle.end_fill()
    dibujar(techito[0])
    viajar(cuerpo[2])
    andar(altura*0.25)
    virar(180)


    turtle.fillcolor(color_edificio)
    turtle.begin_fill()
    techo = triangulo(ancho, altura*0.5)
    dibujar(techo[1])
    dibujar(techo[0])
    turtle.end_fill()


    viajar(cuerpo2[0])
    desactivar_pluma()
    virar(-90)
    andar(ancho*0.125)
    activar_pluma()
    turtle.fillcolor(color_techo)
    turtle.begin_fill()
    garaje = cuadro(altura*0.4, ancho*0.3)
    turtle.end_fill()
    dibujar(garaje[1])
    dibujar(garaje[2]) 
    dibujar(garaje[3])
    
    garaje_dib(garaje[0], altura, 7, ancho)

    viajar(cuerpo[3])
    virar(180)
    desactivar_pluma()
    andar(ancho*0.1)
    virar(90)
    andar(altura*-0.1)
    virar(-90)
    activar_pluma()
    virar(-90)
    turtle.fillcolor(color_ventana)
    turtle.begin_fill()
    dibujar_cuadro(ancho*0.2, altura*0.7)
    turtle.end_fill()
    desactivar_pluma()
    andar(altura*0.1)
    virar(90)
    andar(ancho*-0.45)
    activar_pluma()
    turtle.fillcolor(color_puerta)
    turtle.begin_fill()
    puerta = dibujar_cuadro( altura*0.25, ancho*0.2)
    turtle.end_fill()
    andar(ancho*-0.09)
    virar(-90)
    andar(altura*0.25)
    viajar(puerta[0])
    virar(90)
    desactivar_pluma()
    andar(ancho*0.04)
    virar(-90)
    andar(altura*0.1)
    virar(90)
    activar_pluma()
    virar(-90)
    turtle.fillcolor(color_ventana)
    turtle.begin_fill()
    dibujar_cuadro(ancho*0.2, altura*0.7)
    turtle.end_fill()

    virar(90)

    return ini
    
def garaje_dib(garaje, altura, contador, ancho):

    '''E: Garaje lista de 3 elementos de cordenadas, Altura y Ancho int o float, Contador int
    R: Garaje debe ser una lista de 3 números, los demás valores deben ser numéricos
    S: Valida los datos y llama a la función auxiliar para dibujar'''

    if type(garaje) != list:
        return "Error 23"

    if len(garaje) != 3:
        return "Error 24"

    if es_num(garaje) == False:
        return "Error 25"

    if ((type(altura) != int and type(altura) != float) or
    (type(contador) != int) or (type(ancho) != int and type(ancho) != float)) :
        return "Error 26"

    else:
        return garaje_dib_aux(garaje, altura, contador, ancho)


def garaje_dib_aux(garaje, altura, contador, ancho):

    if contador == 0:
        return 

    viajar(garaje)
    virar(90)
    andar(altura * (0.05 * contador))
    virar(-90)
    
    desactivar_pluma()
    andar(ancho * 0.05)
    activar_pluma()
    
    andar(ancho * 0.2)
    
    return garaje_dib_aux(garaje, altura, contador - 1, ancho)

def edificio5(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo, color_techito):

    '''E: Altura int, Ancho int, color de ventana RGB, color de edificio RGB, color de puerta RGB,
    color de techo RGB, color de apoyo RGB
    R: Solo acepta valores tipo int o float
    en Ancho y Altura y solor de tipo RGB para turtle en las demas entradas
    S: El edificio 5 con medidas y colores acordes a los parametros dados'''

    if type(altura) != int or type(ancho) != int: 
        return "Error 27"

    if (type(color_ventana) != tuple or type(color_edificio) != tuple or type(color_puerta) != tuple or
    type(color_techo) != tuple or type(color_techito) != tuple):
        return "Error 28"

    if (len(color_ventana) != 3 or len(color_edificio) != 3 or len(color_puerta) != 3 or
    len(color_techo) != 3 or len(color_techito) != 3):
        return "Error 29"

    else:
        return edificio5_aux(altura,ancho, color_ventana, color_edificio, color_puerta, 
        color_techo, color_techito)





def edificio5_aux(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo, color_techito):
    ini=posición

    turtle.fillcolor(color_edificio)
    turtle.begin_fill()
    cuerpo= dibujar_cuadro(altura*1.3, ancho*2)
    turtle.end_fill()
    viajar(cuerpo[1])
    andar(ancho*0.05)
    virar(180)

    turtle.fillcolor(color_techito)
    turtle.begin_fill()
    tejado= dibujar_cuadro(altura*0.1, ancho*2.1)
    turtle.end_fill()
    viajar(tejado[1])
    virar(180)
    andar(ancho*0.05)
    turtle.fillcolor(color_techo)
    turtle.begin_fill()
    dibujar_triangulo(altura*0.5, ancho*2)
    turtle.end_fill()

    viajar(cuerpo[1])
    virar(-90)
    andar(altura*0.3)
    virar(90)
    desactivar_pluma()
    andar(ancho*0.05)
    activar_pluma()
    andar(ancho*1.9)
    virar(180)
    andar(ancho*1.85)
    virar(180)
    turtle.fillcolor(color_ventana)
    turtle.begin_fill()
    dibujar_cuadro(altura*0.2, ancho*1.8)
    turtle.end_fill()

    viajar(cuerpo[1])
    virar(90)
    andar(altura*0.6)
    virar(90)
    desactivar_pluma()
    andar(ancho*0.1)
    activar_pluma()
    turtle.fillcolor(color_ventana)
    turtle.begin_fill()
    ventanal1=dibujar_cuadro(altura*0.2, ancho*1.8)
    turtle.end_fill()
    viajar(ventanal1[0])
    virar(-180)
    andar(ancho*0.15)
    turtle.fillcolor(color_techito)
    turtle.begin_fill()
    dibujar_cuadro(altura*0.2, ancho*0.025)
    turtle.end_fill()
    ventana1(ancho, altura, 9, color_techito)
    viajar(cuerpo[1])
    virar(90)
    andar(altura*0.9)
    virar(90)
    desactivar_pluma()
    andar(ancho*0.1)
    activar_pluma()
    turtle.fillcolor(color_ventana)
    turtle.begin_fill()
    ventanal2=dibujar_cuadro(altura*0.2, ancho*1.8)
    turtle.end_fill()    
    viajar(ventanal2[0])
    virar(-180)
    andar(ancho*0.15)
    turtle.fillcolor(color_techito)
    turtle.begin_fill()
    dibujar_cuadro(altura*0.2, ancho*0.025)
    turtle.end_fill()
    ventana1(ancho, altura, 9,color_techito)

    viajar(cuerpo[0])
    virar(180)
    andar(ancho)
    turtle.fillcolor(color_puerta)
    turtle.begin_fill()
    dibujar_cuadro(altura*0.3, ancho*0.2)
    andar(ancho*0.2)
    virar(180)
    dibujar_cuadro(altura*0.3, ancho*0.2)
    turtle.end_fill()

    virar(180)




    return ini

def edificio6(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo):

    '''E: Altura int, Ancho int, color de ventana RGB, color de edificio RGB, color de puerta RGB,
    color de techo RGB, color de apoyo RGB
    R: Solo acepta valores tipo int o float
    en Ancho y Altura y solor de tipo RGB para turtle en las demas entradas
    S: El edificio 6 con medidas y colores acordes a los parametros dados'''

    if type(altura) != int or type(ancho) != int: 
        return "Error 30"

    if (type(color_ventana) != tuple or type(color_edificio) != tuple or type(color_puerta) != tuple or
    type(color_techo) != tuple):
        return "Error 31"

    if (len(color_ventana) != 3 or len(color_edificio) != 3 or len(color_puerta) != 3 or
    len(color_techo) != 3):
        return "Error 32"

    else:
        return edificio6_aux(altura,ancho, color_ventana, color_edificio, color_puerta, 
        color_techo)



def edificio6_aux(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo):

    ini = posición


    turtle.fillcolor(color_edificio)
    turtle.begin_fill()
    cuerpo= cuadro(altura*2,ancho*0.5)
    turtle.end_fill()
    dibujar(cuerpo[1])
    viajar(cuerpo[3])
    dibujar(cuerpo[2])
    viajar(cuerpo[1])
    virar(-90)
    andar(altura*-0.25)
    turtle.fillcolor(color_edificio)
    turtle.begin_fill()
    techo=triangulo(ancho*0.5, altura*0.5)
    turtle.end_fill()
    viajar(techo[0])
    dibujar(techo[2])

    ventanal(ancho, altura, 6, 0.3, techo[0], color_ventana)

    viajar(cuerpo[0])
    desactivar_pluma()
    virar(90)
    andar(ancho*0.125)
    activar_pluma()
    virar(90)

    turtle.fillcolor(color_puerta)
    turtle.begin_fill()
    dibujar_cuadro(ancho*0.075, altura*0.25)
    virar(90)
    andar(ancho*0.075)
    virar(90)
    dibujar_cuadro(ancho*0.075, altura*0.25)
    virar(90)
    turtle.end_fill()

    return ini


def edificio7(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo):

    '''E: Altura int, Ancho int, color de ventana RGB, color de edificio RGB, color de puerta RGB,
    color de techo RGB, color de apoyo RGB
    R: Solo acepta valores tipo int o float
    en Ancho y Altura y solor de tipo RGB para turtle en las demas entradas
    S: El edificio 7 con medidas y colores acordes a los parametros dados'''

    if type(altura) != int or type(ancho) != int: 
        return "Error 33"

    if (type(color_ventana) != tuple or type(color_edificio) != tuple or type(color_puerta) != tuple or
    type(color_techo) != tuple):
        return "Error 34"

    if (len(color_ventana) != 3 or len(color_edificio) != 3 or len(color_puerta) != 3 or
    len(color_techo) != 3):
        return "Error 35"

    else:
        return edificio7_aux(altura,ancho, color_ventana, color_edificio, color_puerta, 
        color_techo)

def edificio7_aux(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo):

    ini = posición

    turtle.fillcolor(color_edificio)
    turtle.begin_fill()
    cuerpo= dibujar_cuadro(altura*1.3, ancho*0.5 )
    turtle.end_fill()
    virar(180)
    andar(ancho*-0.25)
    sub_edificio(altura, ancho, color_ventana, color_edificio, color_puerta, color_techo)
    viajar(cuerpo[3])
    virar(90)
    turtle.begin_fill()
    sub_edificio(altura, ancho, color_ventana, color_edificio, color_puerta, color_techo)
    turtle.end_fill()
    viajar(cuerpo[0])
    virar(90)
    andar(ancho*0.1)

    turtle.fillcolor(color_puerta)
    turtle.begin_fill()
    puerta= dibujar_cuadro(altura*0.3, ancho*0.3)
    turtle.end_fill()
    andar(ancho*-0.025)
    virar(90)
    andar(altura*-0.3)
    virar(90)
    andar(ancho*0.125)
    virar(90)
    andar(altura*-0.3)
    virar(90)
    andar(ancho*-0.125)
    virar(90)
    andar(altura*-0.3)

    viajar(puerta[1])
    virar(-90)
    andar(ancho*0.03)
    virar(180)
    turtle.fillcolor(color_techo)
    turtle.begin_fill()
    trapecio1= triangulo(altura*0.08, ancho*0.05)
    dibujar(trapecio1[0])
    andar(ancho*0.025)
    trapecio2= cuadro(altura*0.08, ancho*0.3)
    viajar(trapecio2[1])
    dibujar(trapecio2[2])
    viajar(trapecio2[3])
    andar(ancho*-0.025)
    trapecio3= triangulo(altura*0.08, ancho*0.05)
    dibujar(trapecio3[1])
    dibujar(trapecio3[0])
    viajar(trapecio2[1])
    turtle.end_fill()

    turtle.fillcolor(color_ventana)
    turtle.begin_fill()
    dibujar_cuadro(altura*0.8, ancho*0.3)
    turtle.end_fill()
    virar(180)
    




    return ini



def edificio8(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo):

    '''E: Altura int, Ancho int, color de ventana RGB, color de edificio RGB, color de puerta RGB,
    color de techo RGB, color de apoyo RGB
    R: Solo acepta valores tipo int o float
    en Ancho y Altura y solor de tipo RGB para turtle en las demas entradas
    S: El edificio 8 con medidas y colores acordes a los parametros dados'''

    if type(altura) != int or type(ancho) != int: 
        return "Error 36"

    if (type(color_ventana) != tuple or type(color_edificio) != tuple or type(color_puerta) != tuple or
    type(color_techo) != tuple):
        return "Error 37"

    if (len(color_ventana) != 3 or len(color_edificio) != 3 or len(color_puerta) != 3 or
    len(color_techo) != 3):
        return "Error 38"

    else:
        return edificio8_aux(altura,ancho, color_ventana, color_edificio, color_puerta, 
        color_techo)

def edificio8_aux(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo):

    ini = posición
    turtle.fillcolor(color_edificio)
    turtle.begin_fill()
    cuerpo = dibujar_cuadro(altura*2, ancho*0.5)
    turtle.end_fill()

    turtle.fillcolor(color_ventana)

    viajar(cuerpo[1])
    virar(90)
    andar(altura*0.25)
    turtle.begin_fill()
    ventana4(altura, ancho)
    turtle.end_fill()

    viajar(cuerpo[1])
    virar(90)
    andar(altura*0.5)
    turtle.begin_fill()
    ventana4(altura, ancho)
    turtle.end_fill()
    viajar(cuerpo[1])
    virar(90)
    andar(altura*0.75)
    turtle.begin_fill()
    ventana4(altura, ancho)
    turtle.end_fill()
    viajar(cuerpo[1])
    virar(90)
    andar(altura*1)
    turtle.begin_fill()
    ventana4(altura, ancho)
    turtle.end_fill()
    viajar(cuerpo[1])
    virar(90)
    andar(altura*1.25)
    turtle.begin_fill()
    ventana4(altura, ancho)
    turtle.end_fill()
    viajar(cuerpo[1])
    virar(90)
    andar(altura*1.50)
    turtle.begin_fill()
    ventana4(altura, ancho)
    turtle.end_fill()
    viajar(cuerpo[0])
    virar(180)
    andar(ancho*0.25)
    turtle.end_fill()

    turtle.fillcolor(color_puerta)
    turtle.begin_fill()
    dibujar_cuadro(altura*0.325, ancho*0.125)
    turtle.end_fill()
    virar(180)
    andar(ancho*-0.125)
    turtle.begin_fill()
    dibujar_cuadro(altura*0.325, ancho*0.125)
    turtle.end_fill()
    virar(180)

    return ini



def crear_edificio1(altura, ancho, separacion, color_ventana, color_edificio, color_puerta, color_techo, 
    color_apoyo):

    '''E: Altura, Ancho, Separacion (num), Colores (tuplas RGB)
    R: Valores numéricos para medidas y tuplas de 3 para colores
    S: Genera el espaciado del edificio 1'''

    if ((type(altura) != int and type(altura) != float) or (type(ancho) != int and type(ancho) != float) or
    (type(separacion) != int and type(separacion) != float)):
        return "Error 39"

    if ((type(color_ventana) != tuple or type(color_edificio) != tuple or type(color_puerta) != tuple or
    type(color_techo) != tuple or type(color_apoyo) != tuple)):
        return "Error 40"

    if (len(color_ventana) != 3 or len(color_edificio) != 3 or len(color_puerta) != 3 or
    len(color_techo) != 3 or len(color_apoyo) != 3):
        return "Error 41"

    return crear_edificio1_aux(altura,ancho, separacion, color_ventana, color_edificio, color_puerta,
    color_techo, color_apoyo)

def crear_edificio1_aux(altura,ancho, separacion, color_ventana, color_edificio, color_puerta, color_techo,
    color_apoyo):
    
    edi1 = edificio1(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo, color_apoyo)
    
    viajar(edi1)
    
    distancia = ancho*1.2 + separacion
    desactivar_pluma()
    andar(distancia)
    activar_pluma()
    return edi1


def crear_edificio2(altura, ancho, separacion, color_ventana, color_edificio, color_puerta, color_techo, 
    color_apoyo):

    '''E: Altura, Ancho, Separacion (num), Colores (tuplas RGB)
    R: Valores numéricos para medidas y tuplas de 3 para colores
    S: Genera el espaciado del edificio 2'''

    if ((type(altura) != int and type(altura) != float) or (type(ancho) != int and type(ancho) != float) or
    (type(separacion) != int and type(separacion) != float)):
        return "Error 42"

    if ((type(color_ventana) != tuple or type(color_edificio) != tuple or type(color_puerta) != tuple or
    type(color_techo) != tuple or type(color_apoyo) != tuple)):
        return "Error 43"

    if (len(color_ventana) != 3 or len(color_edificio) != 3 or len(color_puerta) != 3 or
    len(color_techo) != 3 or len(color_apoyo) != 3):
        return "Error 44"

    return crear_edificio2_aux(altura,ancho, separacion, color_ventana, color_edificio, color_puerta,
    color_techo, color_apoyo)

def crear_edificio2_aux(altura,ancho, separacion, color_ventana, color_edificio, color_puerta, color_techo, 
    color_apoyo):

    desactivar_pluma()
    andar(ancho*0.1)
    activar_pluma()
    edi2 = edificio2(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo, color_apoyo)

    viajar(edi2)
    
    distancia = ancho*2 + separacion*1.8
    desactivar_pluma()
    andar(distancia)
    activar_pluma()
    return edi2

def crear_edificio3(altura, ancho, separacion, color_ventana, color_edificio, color_puerta, color_techo, 
    color_apoyo):

    '''E: Altura, Ancho, Separacion (num), Colores (tuplas RGB)
    R: Valores numéricos para medidas y tuplas de 3 para colores
    S: Genera el espaciado del edificio 3'''

    if ((type(altura) != int and type(altura) != float) or (type(ancho) != int and type(ancho) != float) or
    (type(separacion) != int and type(separacion) != float)):
        return "Error 45"

    if ((type(color_ventana) != tuple or type(color_edificio) != tuple or type(color_puerta) != tuple or
    type(color_techo) != tuple or type(color_apoyo) != tuple)):
        return "Error 46"

    if (len(color_ventana) != 3 or len(color_edificio) != 3 or len(color_puerta) != 3 or
    len(color_techo) != 3 or len(color_apoyo) != 3):
        return "Error 47"

    return crear_edificio3_aux(altura,ancho, separacion, color_ventana, color_edificio, color_puerta,
    color_techo, color_apoyo)


def crear_edificio3_aux(altura,ancho, separacion, color_ventana, color_edificio, color_puerta, color_techo, 
    color_apoyo):

    desactivar_pluma()
    andar(ancho*0.3)
    activar_pluma()
    edi3= edificio3(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo, color_apoyo)
    viajar(edi3)


    distancia =  ancho*1.5 + separacion 
    desactivar_pluma()
    andar(distancia)
    activar_pluma()  
    return edi3
  
def crear_edificio4(altura, ancho, separacion, color_ventana, color_edificio, color_puerta, color_techo):

    '''E: Altura, Ancho, Separacion (num), Colores (tuplas RGB)
    R: Valores numéricos para medidas y tuplas de 3 para colores
    S: Genera el espaciado del edificio 4'''

    if ((type(altura) != int and type(altura) != float) or (type(ancho) != int and type(ancho) != float) or
    (type(separacion) != int and type(separacion) != float)):
        return "Error 48"

    if ((type(color_ventana) != tuple or type(color_edificio) != tuple or type(color_puerta) != tuple or
    type(color_techo) != tuple)):
        return "Error 49"

    if (len(color_ventana) != 3 or len(color_edificio) != 3 or len(color_puerta) != 3 or
    len(color_techo) != 3):
        return "Error 50"

    return crear_edificio4_aux(altura,ancho, separacion, color_ventana, color_edificio, color_puerta,
    color_techo)


def crear_edificio4_aux(altura,ancho, separacion, color_ventana, color_edificio, color_puerta, color_techo):

    desactivar_pluma()
    andar(ancho*0.5)
    activar_pluma()
    
    edi4= edificio4(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo)
    viajar(edi4)

    distancia =  ancho*1.125 + separacion 
    desactivar_pluma()
    andar(distancia)
    activar_pluma() 
    return edi4

def crear_edificio5(altura, ancho, separacion, color_ventana, color_edificio, color_puerta, color_techo, 
    color_apoyo):

    '''E: Altura, Ancho, Separacion (num), Colores (tuplas RGB)
    R: Valores numéricos para medidas y tuplas de 3 para colores
    S: Genera el espaciado del edificio 5'''

    if ((type(altura) != int and type(altura) != float) or (type(ancho) != int and type(ancho) != float) or
    (type(separacion) != int and type(separacion) != float)):
        return "Error 51"

    if ((type(color_ventana) != tuple or type(color_edificio) != tuple or type(color_puerta) != tuple or
    type(color_techo) != tuple or type(color_apoyo) != tuple)):
        return "Error 52"

    if (len(color_ventana) != 3 or len(color_edificio) != 3 or len(color_puerta) != 3 or
    len(color_techo) != 3 or len(color_apoyo) != 3):
        return "Error 53"

    return crear_edificio5_aux(altura,ancho, separacion, color_ventana, color_edificio, color_puerta,
    color_techo, color_apoyo)

    
def crear_edificio5_aux(altura,ancho, separacion, color_ventana, color_edificio, color_puerta, color_techo, 
    color_techito):

    
    edi5= edificio5(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo, color_techito)
    viajar(edi5)

    distancia =  ancho*2.1 + separacion
    desactivar_pluma()
    andar(distancia)
    activar_pluma() 
    return edi5  


def crear_edificio6(altura, ancho, separacion, color_ventana, color_edificio, color_puerta, color_techo):

    '''E: Altura, Ancho, Separacion (num), Colores (tuplas RGB)
    R: Valores numéricos para medidas y tuplas de 3 para colores
    S: Genera el espaciado del edificio 6'''

    if ((type(altura) != int and type(altura) != float) or (type(ancho) != int and type(ancho) != float) or
    (type(separacion) != int and type(separacion) != float)):
        return "Error 54"

    if ((type(color_ventana) != tuple or type(color_edificio) != tuple or type(color_puerta) != tuple or
    type(color_techo) != tuple)):
        return "Error 55"

    if (len(color_ventana) != 3 or len(color_edificio) != 3 or len(color_puerta) != 3 or
    len(color_techo) != 3):
        return "Error 56"

    return crear_edificio6_aux(altura,ancho, separacion, color_ventana, color_edificio, color_puerta,
    color_techo)

def crear_edificio6_aux(altura,ancho, separacion, color_ventana, color_edificio, color_puerta, color_techo):
    
    edi6= edificio6(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo)
    viajar(edi6)

    distancia =  ancho*0.5 + separacion
    desactivar_pluma()
    andar(distancia)
    activar_pluma() 
    return edi6 


def crear_edificio7(altura, ancho, separacion, color_ventana, color_edificio, color_puerta, color_techo):

    '''E: Altura, Ancho, Separacion (num), Colores (tuplas RGB)
    R: Valores numéricos para medidas y tuplas de 3 para colores
    S: Genera el espaciado del edificio 7'''

    if ((type(altura) != int and type(altura) != float) or (type(ancho) != int and type(ancho) != float) or
    (type(separacion) != int and type(separacion) != float)):
        return "Error 57"

    if ((type(color_ventana) != tuple or type(color_edificio) != tuple or type(color_puerta) != tuple or
    type(color_techo) != tuple)):
        return "Error 58"

    if (len(color_ventana) != 3 or len(color_edificio) != 3 or len(color_puerta) != 3 or
    len(color_techo) != 3):
        return "Error 59"

    return crear_edificio7_aux(altura,ancho, separacion, color_ventana, color_edificio, color_puerta,
    color_techo)

def crear_edificio7_aux(altura,ancho, separacion, color_ventana, color_edificio, color_puerta, color_techo):

    desactivar_pluma()
    andar(ancho*0.4)
    activar_pluma()
    edi7= edificio7(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo)
    viajar(edi7)

    distancia =  ancho + separacion
    desactivar_pluma()
    andar(distancia)
    activar_pluma()
    return edi7


def crear_edificio8(altura, ancho, separacion, color_ventana, color_edificio, color_puerta, color_techo):

    '''E: Altura, Ancho, Separacion (num), Colores (tuplas RGB)
    R: Valores numéricos para medidas y tuplas de 3 para colores
    S: Genera el espaciado del edificio 8'''

    if ((type(altura) != int and type(altura) != float) or (type(ancho) != int and type(ancho) != float) or
    (type(separacion) != int and type(separacion) != float)):
        return "Error 60"

    if ((type(color_ventana) != tuple or type(color_edificio) != tuple or type(color_puerta) != tuple or
    type(color_techo) != tuple)):
        return "Error 61"

    if (len(color_ventana) != 3 or len(color_edificio) != 3 or len(color_puerta) != 3 or
    len(color_techo) != 3):
        return "Error 62"

    return crear_edificio8_aux(altura,ancho, separacion, color_ventana, color_edificio, color_puerta,
    color_techo)
 

def crear_edificio8_aux(altura,ancho, separacion, color_ventana, color_edificio, color_puerta, color_techo):

    edi8= edificio8(altura,ancho, color_ventana, color_edificio, color_puerta, color_techo)
    viajar(edi8)

    distancia =  ancho*0.5 + separacion
    desactivar_pluma()
    andar(distancia)
    activar_pluma()
    return edi8

def calle(ancho):

    """Dibuja la calle central
    E: Ancho de los edificios
    R: Valor solo tipo int o floar
    S: Calle central"""
    
    if (type(ancho) != int and type(ancho) != float):
        return "Error 63"

    return calle_aux(ancho, 1, 10, 20)    
    


def calle_aux(ancho, separacion, contador, tamaño):


    if contador==0:
        turtle.pensize(1)
        return []

    if tamaño > 1:
        turtle.pensize(tamaño)
    else:
        turtle.pensize(1)

    puntoA=posición
        
    andar(100)

    puntoB=posición
    
    desactivar_pluma()
    andar(250)
    activar_pluma()

    puntoC= posición
    andar(100)
    puntoD= posición
    
    desactivar_pluma()
    andar(250)
    activar_pluma()
    return calle_aux(ancho, separacion, contador-1, tamaño-3) + [puntoA, puntoB, puntoC, puntoB]

def ventana1(ancho, altura, contador, color_edificio):
    
    '''E: Ancho num, Altura num, Contador int, Color RGB
    R: Solo valores numéricos y tupla de 3 para el color
    S: Valida datos y llama a la auxiliar para dibujar líneas ventana 1'''
    
    if (type(ancho) != int and type(ancho) != float) or (type(altura) != int and type(altura) != float):
        return "Error 64"
        
    if (type(contador) != int):
        return "Error 65"
    
    if (type(color_edificio) != tuple) or (len(color_edificio) != 3):
        return "Error 66"
    
    else:
        return ventana1_aux(ancho, altura, contador, color_edificio)
    
def ventana1_aux(ancho, altura, contador, color_edificio):
    
    if contador == 0:
        return 
    virar(180)
    andar(ancho * 0.175)
    turtle.fillcolor(color_edificio)
    turtle.begin_fill()
    dibujar_cuadro(altura * 0.2, ancho * 0.025)
    turtle.end_fill()
    return ventana1_aux(ancho, altura, contador - 1, color_edificio)

def ventana2(ancho, altura, contador, color_ventana):

    '''E: Ancho num, Altura num, Contador int, Color RGB
    R: Solo valores numéricos y tupla de 3 para el color
    S: Valida datos y llama a la auxiliar para dibujar ventana 2'''

    if (type(ancho) != int and type(ancho) != float) or (type(altura) != int and type(altura) != float):
        return "Error 67"
    
    if (type(contador) != int):
        return "Error 68"

    if (type(color_ventana) != tuple) or (len(color_ventana) != 3):
        return "Error 69"

    else:
        return ventana2_aux(ancho, altura, contador, color_ventana)

def ventana2_aux(ancho, altura, contador, color_ventana):

    if contador == 0:
        return
    desactivar_pluma()
    virar(90)
    andar(ancho * 0.05)
    activar_pluma()
    turtle.fillcolor(color_ventana)
    turtle.begin_fill()

    if abs(ancho) > abs(altura):
        dibujar_cuadro(ancho * 0.075, altura * 0.1)
        turtle.end_fill()
        andar(altura * -0.1)
        virar(90)
        desactivar_pluma()
        andar(altura * 0.1)
        activar_pluma()
        desactivar_pluma()
    else: 
        dibujar_cuadro(ancho * 0.075, ancho * 0.075)
        turtle.end_fill()
        andar(ancho * -0.075)
        virar(90)
        desactivar_pluma()
        andar(ancho * 0.1)
        activar_pluma()
        desactivar_pluma()
        

    return ventana2_aux(ancho, altura, contador - 1, color_ventana)

def ventana3(ancho, altura):

    '''E: Ancho num, Altura num
    R: Solo valores numéricos
    S: Valida datos y llama a la auxiliar para dibujar ventana 3'''

    if (type(ancho) != int and type(ancho) != float) or (type(altura) != int and type(altura) != float):
        return "Error 70"

    else:
        return ventana3_aux(ancho, altura)

def ventana3_aux(ancho, altura):

    virar(90)
    desactivar_pluma()
    andar(ancho * 0.025)
    activar_pluma()
    virar(-90)
    dibujar_cuadro(ancho * 0.2, altura * 0.1)
    andar(altura * -0.1)
    virar(-90)
    andar(ancho * 0.1125)
    virar(90)
    dibujar_cuadro(ancho * 0.025, altura * 0.1)

def ventana4(altura, ancho):

    '''E: Altura num, Ancho num
    R: Solo valores numéricos
    S: Valida datos y llama a la auxiliar para dibujar ventana 4'''

    if (type(altura) != int and type(altura) != float) or (type(ancho) != int and type(ancho) != float):
        return "Error 71"

    else:
        return ventana4_aux(altura, ancho)

def ventana4_aux(altura, ancho):

    virar(90)
    desactivar_pluma()
    andar(ancho * 0.025)
    activar_pluma()
    dibujar_cuadro(ancho * 0.2, altura * 0.1)
    virar(180)
    desactivar_pluma()
    andar(ancho * 0.125)
    activar_pluma()
    dibujar_cuadro(ancho * 0.2, altura * 0.2)
    virar(180)
    desactivar_pluma()
    andar(ancho * 0.225)
    activar_pluma()
    dibujar_cuadro(ancho * 0.2, altura * 0.1)

def ventanal(ancho, altura, contador, mult, techo, color_ventana):

    '''E: Ancho num, Altura num, Contador int, Multiplicador num, Techo lista [x,y,z], Color RGB
    R: Validar tipos de datos y lista de posición
    S: Valida datos y llama a la auxiliar dibujar el ventanal'''

    if (type(ancho) != int and type(ancho) != float) or (type(altura) != int and type(altura) != float) or (type(mult) != int and type(mult) != float):
        return "Error 72"
    
    if (type(contador) != int):
        return "Error 73"

    if (type(techo) != list) or (len(techo) != 3) or (es_num(techo) == False):
        return "Error 74"

    if (type(color_ventana) != tuple) or (len(color_ventana) != 3):
        return "Error 75"

    else:
        return ventanal_aux(ancho, altura, contador, mult, techo, color_ventana)

def ventanal_aux(ancho, altura, contador, mult, techo, color_ventana):

    if contador == 0:
        return
    else:
        viajar(techo)
        andar(altura * mult)
        ventana2(ancho, altura, 4, color_ventana)
        return ventanal_aux(ancho, altura, contador - 1, mult + 0.3, techo, color_ventana)


    

def sub_edificio(altura, ancho, color_ventana, color_edificio, color_puerta, color_techo):

    '''E: Altura num, Ancho num, Colores RGB
    R: Solo valores numéricos y tuplas de 3 para colores
    S: Valida datos y llama a la auxiliar para dibujar sección del subedificio'''

    if (type(altura) != int and type(altura) != float) or (type(ancho) != int and type(ancho) != float):
        return "Error 76"

    if (type(color_ventana) != tuple) or (type(color_edificio) != tuple) or (type(color_puerta) != tuple) or (type(color_techo) != tuple):
        return "Error 77"
    
    if (len(color_ventana) != 3) or (len(color_edificio) != 3) or (len(color_puerta) != 3) or (len(color_techo) != 3):
        return "Error 78"

    else:
        return sub_edificio_aux(altura, ancho, color_ventana, color_edificio, color_puerta, color_techo)

def sub_edificio_aux(altura, ancho, color_ventana, color_edificio, color_puerta, color_techo):

    turtle.fillcolor(color_edificio)
    turtle.begin_fill()
    cuerpo = dibujar_cuadro(altura * 0.7, ancho * 0.25)
    turtle.end_fill()
    
    viajar(cuerpo[1])
    virar(90)
    andar(altura * 0.05)
    
    turtle.fillcolor(color_ventana)
    turtle.begin_fill()
    ventana3(ancho, altura * 1.5)
    turtle.end_fill()
    
    viajar(cuerpo[1])
    andar(altura * 0.25)
    turtle.begin_fill()
    ventana3(ancho, altura * 1.5)
    turtle.end_fill()   
    
    viajar(cuerpo[1])
    andar(altura * 0.45)
    turtle.begin_fill()
    ventana3(ancho, altura * 1.5)
    turtle.end_fill()



def acera(ancho, separacion):

    '''E: Ancho num, Separacion num
    R: Solo valores numéricos (int o float)
    S: Valida datos y dibuja la acera izquierda'''

    if (type(ancho) != int and type(ancho) != float):
        return "Error 79"
    
    if (type(separacion) != int and type(separacion) != float):
        return "Error 80"
    
    else:
        return acera_aux(ancho, separacion, 5)

def acera_aux(ancho, separacion, escala):

    puntoA = posición
    andar(14000)
    puntoB = posición
    viajar(puntoA)
    viajar([posición[0] + escala * 20, posición[1], posición[2]])
    puntoC = posición

    viajar(puntoA)
    viajar([posición[0], posición[1] - escala * 10, posición[2]])
    
    puntoG = posición
    viajar(puntoC)

    andar(14000)
 
    puntoD = posición

    viajar(puntoC)

    viajar([posición[0], posición[1] - escala * 10, posición[2]])

    puntoE = posición
    andar(14000)
    puntoF = posición

    viajar(puntoA)
    dibujar(puntoC)
    viajar(puntoA)
    dibujar(puntoG)
    
    viajar(puntoC)
    dibujar(puntoE)

def acera_inv(ancho, separacion):
    
    '''E: Ancho num, Separacion num
    R: Solo valores numéricos (int o float)
    S: Valida datos y dibuja la acera derecha'''    
    if (type(ancho) != int and type(ancho) != float):
        return "Error 81"
        
    if (type(separacion) != int and type(separacion) != float):
        return "Error 82"
        
    else:
        return acera_inv_aux(ancho*-1, separacion, 5)
    
def acera_inv_aux(ancho, separacion, escala):

    puntoA = posición
    andar(-14000)
    puntoB = posición
    viajar(puntoA)
    viajar([posición[0] + escala * -20, posición[1], posición[2]])
    puntoC = posición

    viajar(puntoA)
    viajar([posición[0], posición[1] - escala * 10, posición[2]])
    
    puntoG = posición
    viajar(puntoC)

    andar(-14000)
 
    puntoD = posición

    viajar(puntoC)

    viajar([posición[0], posición[1] - escala * 10, posición[2]])

    puntoE = posición
    andar(-14000)
    puntoF = posición

    viajar(puntoA)
    dibujar(puntoC)
    viajar(puntoA)
    dibujar(puntoG)
    
    viajar(puntoC)
    dibujar(puntoE)

    viajar(puntoG)
    dibujar(puntoE)
   
    





def crear_ciudad(altura, ancho, separacion,edificios, color_edificios, color_puertas, color_ventanas, color_techos):
                
                
    '''E: Altura (int), Ancho (int), Separacion (int), Cantidad de edificios (int),
    Listas de colores (list), Color ventanas (tuple)
    R: Los parámetros de medida deben ser números; los colores deben ser listas o tuplas según corresponda
    S: Valida la entrada e inicia la construcción de la ciudad en ambos sentidos'''

    if (type(altura) != int or type(ancho) != int != float or type(separacion) != int  
    or type(edificios) != int):
        return "Error 83"

    if (type(color_edificios) != list) or (type(color_puertas) != list) or (type(color_techos) != list):
        return "Error 84"

    if (type(color_ventanas) != tuple) or (len(color_ventanas) != 3):
        return "Error 85"

    else:


        cabecear(89)

        ini=posición
        viajar([posición[0]+edificios, posición[1], posición[2]])

        
        acera(ancho, separacion)
        
        viajar(ini)
        
        viajar([posición[0]+5*140, posición[1], posición[2]])
        calle(ancho)

        
        
        viajar(ini)
        
        crear_ciudad_aux(altura, ancho, separacion,edificios, random.randint(1, 8),
        color_edificios, color_puertas, color_ventanas, color_techos, random.randint(0, 28),
        random.randint(0, 27), random.randint(0, 26), random.randint(0, 26))
        
        viajar(ini)
        viajar([posición[0]*-1, posición[1]-600, posición[2]])
        ini2= posición
        virar(-89*2)

        andar(-400)
        crear_ciudad_aux(-altura, -ancho, -separacion,edificios, random.randint(1, 8), 
        color_edificios, color_puertas, color_ventanas, color_techos, random.randint(0, 28), 
        random.randint(0, 27), random.randint(0, 26), random.randint(0, 26))
        

        viajar(ini2)
        acera_inv(ancho, separacion)
                
                
                    
                
                    
                
                
                    
                
                    
                
                
                
                
def crear_ciudad_aux(altura, ancho, separacion,edificios, edificio, color_edificios, color_puertas,
color_ventanas, color_techos, color_edificio, color_puerta, color_techo, color_apoyo):
   
    if edificios <= 0:
        return 0
    else:
  
        if edificio == 1:
        
            crear_edificio1(altura,ancho, separacion, color_ventanas, 
            color_edificios[color_edificio], color_puertas[color_puerta], 
            color_techos[color_techo], color_techos[color_apoyo])
            
            return crear_ciudad_aux(altura, ancho, separacion,edificios-1, random.randint(1, 8), 
                color_edificios, color_puertas, color_ventanas, color_techos, random.randint(0, 28),
                random.randint(0, 27), random.randint(0, 26), random.randint(0, 26))
                
        if edificio == 2:
        
            crear_edificio2(altura,ancho, separacion, color_ventanas,
            color_edificios[color_edificio], color_puertas[color_puerta],
            color_techos[color_techo], color_techos[color_apoyo])
            
            return crear_ciudad_aux(altura, ancho, separacion,edificios-2, random.randint(1, 8), 
                color_edificios, color_puertas, color_ventanas, color_techos, random.randint(0, 28),
                random.randint(0, 27), random.randint(0, 26), random.randint(0, 26))
                
        if edificio == 3:
        
            crear_edificio3(altura,ancho, separacion, color_ventanas, color_edificios[color_edificio], 
            color_puertas[color_puerta], color_techos[color_techo], color_techos[color_apoyo])
            
            return crear_ciudad_aux(altura, ancho, separacion,edificios-1, random.randint(1, 8), 
                color_edificios, color_puertas, color_ventanas, color_techos, random.randint(0, 28),
                random.randint(0, 27), random.randint(0, 26), random.randint(0, 26))
                
        if edificio == 4:
        
            crear_edificio4(altura,ancho, separacion, color_ventanas, color_edificios[color_edificio],
            color_puertas[color_puerta], color_techos[color_techo])
            
            return crear_ciudad_aux(altura, ancho, separacion,edificios-1, random.randint(1, 8), 
                color_edificios, color_puertas, color_ventanas, color_techos, random.randint(0, 28),
                random.randint(0, 27), random.randint(0, 26), random.randint(0, 26))
                
        if edificio == 5:
        
            crear_edificio5(altura,ancho, separacion, color_ventanas, color_edificios[color_edificio],
            color_puertas[color_puerta], color_techos[color_techo], color_techos[color_apoyo])
            
            return crear_ciudad_aux(altura, ancho, separacion,edificios-1, random.randint(1, 8), 
                color_edificios, color_puertas, color_ventanas, color_techos, random.randint(0, 28),
                random.randint(0, 27), random.randint(0, 26), random.randint(0, 26))
                
        if edificio == 6:
        
            crear_edificio6(altura,ancho, separacion, color_ventanas, color_edificios[color_edificio],
            color_puertas[color_puerta], color_techos[color_techo])
            
            return crear_ciudad_aux(altura, ancho, separacion,edificios-0.5, random.randint(1, 8), 
                color_edificios, color_puertas, color_ventanas, color_techos, random.randint(0, 28),
                random.randint(0, 27), random.randint(0, 26), random.randint(0, 26))
                
        if edificio == 7:
        
            crear_edificio7(altura,ancho, separacion, color_ventanas, color_edificios[color_edificio],
            color_puertas[color_puerta], color_techos[color_techo])
            
            return crear_ciudad_aux(altura, ancho, separacion,edificios-1, random.randint(1, 8), 
                color_edificios, color_puertas, color_ventanas, color_techos, random.randint(0, 28),
                random.randint(0, 27), random.randint(0, 26), random.randint(0, 26))
                
        if edificio == 8:
        
            crear_edificio8(altura,ancho, separacion, color_ventanas, color_edificios[color_edificio],
            color_puertas[color_puerta], color_techos[color_techo])
            
            return crear_ciudad_aux(altura, ancho, separacion,edificios-0.5, random.randint(1, 8), 
                color_edificios, color_puertas, color_ventanas, color_techos, random.randint(0, 28),
                random.randint(0, 27), random.randint(0, 26), random.randint(0, 26))
                


    





# --- Ejecución Principal ---

def bucle(color_edificios, color_puertas, color_ventana, color_techos, velocidad, contador, 
    alto, ancho, cantidad, separacion):

    '''E: Listas de colores, Tupla color ventana, Velocidad (int), Contador (int), Medidas (int)
    R: Contador entre 1 y 899. Medidas deben ser Int y mayores a cero.
    S: Valida la entrada del usuario e inicia el ciclo de dibujo de la ciudad'''

    if type(contador) != int or contador <= 0 or contador > 900:
        return "Error 86"

    if ((type(alto) != int or alto <= 0) or (type(ancho) != int or ancho <= 0) or 
       (type(cantidad) != int or cantidad <= 0) or (type(separacion) != int or separacion <= 0)):
        return "Error 87"

    if type(velocidad) != int or velocidad < 0:
        return "Error 88"

    if type(color_edificios) != list or type(color_puertas) != list or type(color_techos) != list:
        return "Error 89"
    
    if type(color_ventana) != tuple or len(color_ventana) != 3:
        return "Error 90"

    else:
        return bucle_aux(color_edificios, color_puertas, color_ventana, color_techos, 
        velocidad, contador, alto, ancho, cantidad, separacion)


def bucle_aux (color_edificios, color_puertas, color_ventana, color_techos, velocidad, contador, 
    alto, ancho, cantidad, separacion):



    if contador == 0:
        return "Animación Finalizada"

    turtle.clear()
    turtle.speed(0)
    viajar([-900,-500,0])
    virar(270)
    crear_ciudad(alto, ancho, separacion,cantidad, color_edificios, color_puertas, color_ventana, 
    color_techos)

    screen.update()
    time.sleep(1*velocidad)


    global cosenos, distancia_focal
    cosenos = [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]
    
    
    distancia_focal = 750 

    return bucle_aux (color_edificios, color_puertas, color_ventana, color_techos, velocidad*0.8, 
    contador-1, alto, ancho, cantidad, separacion)




def terminal():


    introduccion()

    print("")
    
    alto= input_num("Alto de los edificios: "
    ,"Por favor ingrese un numero entero mayor a 0")
    print("")
    
    ancho= input_num("Ancho de los edificios: "
    ,"Por favor ingrese un numero entero mayor a 0")
    print("")
    
    separacion= input_num("Separación de los edificios: "
    ,"Por favor ingrese un numero entero mayor a 0")
    print("")
    
    cantidad= input_num("Cantidad de edificios por generación: "
    ,"Por favor ingrese un numero entero mayor a 0")
    print("")
    
    velocidad= input_num_velocidad("Velocidad de la generación: "
    ,"Por favor ingrese un numero entero mayor o igual a 0")
    print("")
    
    generaciones= input_num_generaciones("Cantidad de generaciónes: "
    ,"Por favor ingrese un numero entero mayor a 0 y menor a 999")
    print("")
    


    global screen
    screen = turtle.Screen()
    screen.tracer(0)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.colormode(255)

    return bucle (color_edificios, color_puertas, color_ventana, color_techos,int(velocidad),
    int(generaciones), int(alto), int(ancho), int(cantidad), int(separacion))


def introduccion():
    print("Alto: Debe ser un entero mayor a 0, define la altura de los edificio")
    print("(Se recomienda un numero mayor a 200)")
    print("")
    print("Ancho: Debe ser un entero mayor a 0, define el ancho de los edificio")
    print("(Se recomienda un numero mayor a 200)")
    print("")
    print("Separacion: Indica la distancia entre edificios, debe ser mayor a 0")
    print("")
    print("Cantidad: Define cuantos edificios se generan a cada lado de la calle por cada generación,")
    print(" debe ser mayor a 0")
    print("")
    print("Velocidad: Define cada cuantos segundos se genera una nueva calle,") 
    print("este tiempo se va haciendo mas corto con cada generación")
    print("(Se recomienda un numero menor a 5, si no se siente muy lento)")
    print("")
    print("Generaciones: Define cuantas calles se van a generar antes de frenar el programa,") 
    print("el maximo son 900 calles")
    print("")
    input("Precione Enter para seguir: ")
    print("\033[2J\033[H")


    

def input_num_generaciones(frase, requisito):

    '''E: Dos strings (frase de petición y mensaje de error)
    R: Ambos parámetros deben ser strings
    S: Valida los datos de la termianl como numeros enteros, si no lo son solicita nuevos datos'''

    if type(frase) != str or type(requisito) != str:
        return "Error 91"
    
    else:
        return input_num_generaciones_aux(frase, requisito)

def input_num_generaciones_aux(frase, requesito):

    valor= input(frase)
    
    if valor == "" or string_es_num(valor) != True or int(valor) <= 0:        
        print("")
        print(requesito)
        print("")
        return input_num_generaciones_aux(frase, requesito)
        
    else: 

        return valor



def input_num_velocidad(frase, requisito):

    '''E: Dos strings (frase de petición y mensaje de error)
    R: Ambos parámetros deben ser strings
    S: Valida los datos de la termianl como numeros enteros, si no lo son solicita nuevos datos'''

    if type(frase) != str or type(requisito) != str:
        return "Error 91"
    
    else:
        return input_num_velocidad_aux(frase, requisito)

def input_num_velocidad_aux(frase, requesito):

    valor= input(frase)
    
    if valor == "" or string_es_num(valor) != True or int(valor) <= 0:
        print("")
        print(requesito)
        print("")
        return input_num_velocidad_aux(frase, requesito)
        
    else: 

        return valor



def input_num(frase, requisito):

    '''E: Dos strings (frase de petición y mensaje de error)
    R: Ambos parámetros deben ser strings
    S: Valida los datos de la termianl como numeros enteros, si no lo son solicita nuevos datos'''

    if type(frase) != str or type(requisito) != str:
        return "Error 91"
    
    else:
        return input_num_aux(frase, requisito)

def input_num_aux(frase, requesito):

    valor= input(frase)
    
    if valor == "" or string_es_num(valor) != True or int(valor) <= 0:
        print("")
        print(requesito)
        print("")
        return input_num_aux(frase, requesito)
        
    else: 

        return valor

def string_es_num(texto):

    '''E: UN string
    R: Debe recibir un string 
    S: Valida que el dato sea string y verifica que sea un numero'''
    
    if type(texto) != str:
        return "Error 92"
    
    else:
        return string_es_num_aux(texto)

def string_es_num_aux(texto):

    if texto == "":
        return True
        
    if comparar_listas(texto[0], ["0","1","2","3","4","5","6","7","8","9"]) == False:
        return False

    else:
        return string_es_num_aux(texto[1:])

def comparar_listas(elemento, lista):

    '''E: Un elemento de cualquier tipo y una lista
    R: El segundo parámetro debe ser una lista
    S: Valida la entrada y llama a la auxiliar para buscar el elemento'''

    if type(lista) != list:
        return "Error 93"
    
    else:
        return comparar_listas_aux(elemento, lista)

def comparar_listas_aux(elemento, lista):

    if lista == []:
        return False

    if elemento == lista[0]:
        return True

    else: 
        return comparar_listas_aux(elemento, lista[1:])
    
    

print(terminal())

turtle.exitonclick() 
