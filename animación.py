import pygame
import random
import math
from pygame import mixer
import os

# No sé cómo, pero hace que el sonido sea justo en el momento en vez de tener un atraso
pygame.mixer.pre_init(44100, -16, 1, 512)
# SIEMPRE SE TIENE QUE PONER ESTO AL COMIENZO
pygame.init()

# Sonido del ladrido
ladridoSonido = mixer.Sound('Ladrido.ogg')
ladridoSonido.set_volume(0.1)
# Múscia de fondo
cancion = mixer.music
cancion.load('Motion Picture Soundtrack.mp3')
cancion.set_volume(0.5)
# cancion.play(-1)

# Ventana
screenwidth = 1200
screenheight = 600
win = pygame.display.set_mode((screenwidth, screenheight))
icon = pygame.image.load('Pixel art gali 1.png')
pygame.display.set_icon(icon)

# Nombre de la ventana
pygame.display.set_caption("Super Gali")

# Cargar las imágenes

barraImg = pygame.image.load('barra de vida.png').convert()
barraImg.set_colorkey((255, 255, 255))

derecha1 = pygame.image.load('derecha 1.png').convert()
derecha1.set_colorkey((255, 255, 255))
derecha1 = pygame.transform.scale(derecha1, (64, 64))

derecha2 = pygame.image.load('derecha 2.png').convert()
derecha2.set_colorkey((255, 255, 255))
derecha2 = pygame.transform.scale(derecha2, (64, 64))

derecha3 = pygame.image.load('derecha 3.png').convert()
derecha3.set_colorkey((255, 255, 255))
derecha3 = pygame.transform.scale(derecha3, (64, 64))

derecha4 = pygame.image.load('derecha 4.png').convert()
derecha4.set_colorkey((255, 255, 255))
derecha4 = pygame.transform.scale(derecha4, (64, 64))

derecha5 = pygame.image.load('derecha 5.png').convert()
derecha5.set_colorkey((255, 255, 255))
derecha5 = pygame.transform.scale(derecha5, (64, 64))

derecha6 = pygame.image.load('derecha 6.png').convert()
derecha6.set_colorkey((255, 255, 255))
derecha6 = pygame.transform.scale(derecha6, (64, 64))

# moverse izquierda
izquierda1 = pygame.image.load('izquierda 1.png').convert()
izquierda1.set_colorkey((255, 255, 255))
izquierda1 = pygame.transform.scale(izquierda1, (64, 64))

izquierda2 = pygame.image.load('izquierda 2.png').convert()
izquierda2.set_colorkey((255, 255, 255))
izquierda2 = pygame.transform.scale(izquierda2, (64, 64))

izquierda3 = pygame.image.load('izquierda 3.png').convert()
izquierda3.set_colorkey((255, 255, 255))
izquierda3 = pygame.transform.scale(izquierda3, (64, 64))

izquierda4 = pygame.image.load('izquierda 4.png').convert()
izquierda4.set_colorkey((255, 255, 255))
izquierda4 = pygame.transform.scale(izquierda4, (64, 64))

izquierda5 = pygame.image.load('izquierda 5.png').convert()
izquierda5.set_colorkey((255, 255, 255))
izquierda5 = pygame.transform.scale(izquierda5, (64, 64))

izquierda6 = pygame.image.load('izquierda 6.png').convert()
izquierda6.set_colorkey((255, 255, 255))
izquierda6 = pygame.transform.scale(izquierda6, (64, 64))

izquierdaparado = pygame.image.load('izquierda parado.png').convert()
izquierdaparado.set_colorkey((255, 255, 255))
izquierdaparado = pygame.transform.scale(izquierdaparado, (64, 64))

derechaparado = pygame.image.load('derecha parado.png').convert()
derechaparado.set_colorkey((255, 255, 255))
derechaparado = pygame.transform.scale(derechaparado, (64, 64))

izquierdaparadomirando = pygame.image.load('izquierda parado MIRANDO.png').convert()
izquierdaparadomirando.set_colorkey((0, 255, 0))
izquierdaparadomirando = pygame.transform.scale(izquierdaparadomirando, (65, 65))

derechaparadomirando = pygame.image.load('derecha parado MIRANDO.png').convert()
derechaparadomirando.set_colorkey((255, 255, 255))
derechaparadomirando = pygame.transform.scale(derechaparadomirando, (64, 64))

izquierdaHerido = pygame.image.load('izquierda herido.png').convert()
izquierdaHerido.set_colorkey((0, 0, 128))
izquierdaHerido = pygame.transform.scale(izquierdaHerido, (64, 64))

derechaHerido = pygame.image.load('derecha herido.png').convert()
derechaHerido.set_colorkey((255, 255, 255))
derechaHerido = pygame.transform.scale(derechaHerido, (64, 64))

enemigoImg = pygame.image.load('enemigo.png').convert()
enemigoImg.set_colorkey((255, 255, 255))
enemigoImg = pygame.transform.scale(enemigoImg, (32, 32))

enemigoHeridoImg = pygame.image.load('enemigo herido.png').convert()
enemigoHeridoImg.set_colorkey((255, 255, 255))
enemigoHeridoImg = pygame.transform.scale(enemigoHeridoImg, (32, 32))

luna = pygame.image.load('luna.png').convert()
luna.set_colorkey((255, 255, 255))

ladridoImg = pygame.image.load('ladrido.png').convert()
ladridoImg.set_colorkey((255, 255, 255))
ladridoImg = pygame.transform.scale(ladridoImg, (50, 50))

ladridoizquierdoImg = pygame.image.load('ladrido izquierdo.png').convert()
ladridoizquierdoImg.set_colorkey((255, 255, 255))
ladridoizquierdoImg = pygame.transform.scale(ladridoizquierdoImg, (50, 50))

estrellaPequena = pygame.image.load('estrella pequeña.png').convert()

estrellaMediana = pygame.image.load('estrella mediana.png').convert()

poste = pygame.image.load('poste.png').convert()
poste.set_colorkey((255, 255, 255))

walkRight = [derecha1, derecha2, derecha3, derecha4, derecha5, derecha6]
walkLeft = [izquierda1, izquierda2, izquierda3, izquierda4, izquierda5, izquierda6]
character = [izquierdaparado, derechaparado, izquierdaparadomirando, derechaparadomirando, izquierdaHerido,
             derechaHerido]
# Imágenes de ladridos
ladridosImg = [ladridoizquierdoImg, ladridoImg]
# char = character[1]

fondo = pygame.image.load('noche 0.png')

clock = pygame.time.Clock()


class player(object):
    global ladrido
    global ladridos

    def __init__(self, x, y, width, height, character, walkLeft, walkRight):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.boundary_extra = 5
        self.left = False
        self.right = False
        self.walkCount = 0
        self.isJump = False
        self.jumpCount = 20
        self.paradopormuchotiempo = 0
        self.char = character[1]
        self.character = character
        self.walkLeft = walkLeft
        self.walkRight = walkRight
        self.ladridoono = False
        self.ladridodenuevo = True
        self.dibujarladrido = False
        self.contadorFramesLadrido = 0
        self.ladridoADibujar = ''
        self.hitbox = (self.x, self.y + 20, 64, 45)
        self.health = 100
        self.visible = True
        self.tocado = False
        self.retroceder = False
        self.FC = 0

    def draw(self, win):
        if self.visible:

            # Animación de caminar
            if self.walkCount + 1 >= 48:
                self.walkCount = 0
            if self.left:
                win.blit(self.walkLeft[self.walkCount // 8], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(self.walkRight[self.walkCount // 8], (self.x, self.y))
                self.walkCount += 1
            # Gali parado
            else:
                win.blit(self.char, (self.x, self.y))
                self.paradopormuchotiempo += 1
                if self.paradopormuchotiempo >= 300:
                    if self.char == self.character[0]:
                        self.char = self.character[2]
                    elif self.char == self.character[1]:
                        self.char = self.character[3]

            # Esto se usa para probar el hitbox
            self.hitbox = (self.x, self.y + 20, 64, 45)
            #pygame.draw.rect(win, (255, 0, 0), (self.hitbox), 2)

            #Esta es la barra de vida (de color rojo)
            pygame.draw.rect(win, (255, 0, 0), (12, 60, 396 - (100 - self.health) * 3.96, 13))

    def hit(self):
        if self.tocado is False:

            if self.health > 0:
                self.health -= 10
                self.tocado = True
                self.retroceder = True
                self.FC = 0

            if self.health <= 0:
                self.visible = False

    def contadorGolpe(self):
        if self.retroceder:
            if self.FC == 10:
                self.retroceder = False
        self.FC += 1

        # self.golpeado = False
        # self.barra = pygame.draw.rect(win, (255, 0, 0), (12,60,500,23), 2)
        # self.barra.fill((255,0,0))
        # self.barra.fill((255,0,0))
        # self.barra = pygame.fill((255,0,0), rect=self.barra, special_flags=0)


class ladrido(object):
    global ladridoSonido
    global ladridosImg
    global gali

    def __init__(self):
        self.ladridosImg = ladridosImg
        self.ladridoono = False
        self.ladridodenuevo = True
        self.dibujarladrido = False
        self.contadorFramesLadrido = 0
        self.ladridoADibujar = ''
        self.x = gali.x + 60
        self.y = gali.y
        self.sonido = ladridoSonido
        # Esto se usa para probar el hitbox
        self.hitbox = (self.x, self.y + 20, 64, 45)

    def draw(self, win):

        self.y = gali.y

        # poner ladrido
        if self.ladridoono:
            ladridoSonido.play()
            self.dibujarladrido = True

            self.ladridoono = False

        if self.dibujarladrido:
            if gali.char == character[1] or gali.char == character[3]:
                self.x = gali.x + 60
                self.ladridoADibujar = ladridosImg[1]
                win.blit(self.ladridoADibujar, (self.x, self.y + 20))

            elif gali.char == character[0] or gali.char == character[2]:
                self.x = gali.x - 40
                self.ladridoADibujar = ladridosImg[0]
                win.blit(self.ladridoADibujar, (self.x, self.y + 20))
            self.contadorFramesLadrido += 1
            if self.contadorFramesLadrido >= 10:
                self.dibujarladrido = False
                self.contadorFramesLadrido = 0

        # Esto se usa para probar el hitbox
        self.hitbox = (self.x, self.y + 20, 50, 50)
        #pygame.draw.rect(win, (255, 0, 0), (self.hitbox), 2)


class enemy(object):
    global camaraFinal
    walkRight = [enemigoImg]
    walkLeft = [enemigoImg]
    herido = [enemigoHeridoImg]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = -2
        self.isJump = False
        self.jumpCount = 30
        self.yinicial = self.y
        self.framesParaSalto = 10
        self.hitbox = (self.x - camaraFinal.cameraX, self.y, 64, 45)
        self.hitx = False
        self.hity = False
        self.tocado = False
        self.contadorretroceso = 5
        self.vida = 3
        self.restarvida = True
        self.extraSalto = 0
        self.atacado = False

    def draw(self, win):


        self.move()
        if self.contadorretroceso >= 10 or self.atacado is False:
            if self.vida > 0:
                if self.walkCount + 1 >= 3:
                    self.walkCount = 0

                if self.vel > 0:
                    win.blit(self.walkRight[self.walkCount // 3], (self.x - camaraFinal.cameraX, self.y))
                    self.walkCount += 1

                else:
                    win.blit(self.walkRight[self.walkCount // 3], (self.x - camaraFinal.cameraX, self.y))
                    self.walkCount += 1

                self.hitbox = (self.x - camaraFinal.cameraX, self.y, 32, 32)
                #pygame.draw.rect(win, (255, 0, 0), (self.hitbox), 2)

            if self.vida <= 0:
                self.hitbox = (0, 0, 64, 45)



        #Se ponga rojo cuando lo atacan
        if self.contadorretroceso < 10 and self.atacado is True:
            if self.walkCount + 1 >= 3:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.herido[self.walkCount // 3], (self.x - camaraFinal.cameraX, self.y))
                self.walkCount += 1

            else:
                win.blit(self.herido[self.walkCount // 3], (self.x - camaraFinal.cameraX, self.y))
                self.walkCount += 1
            if self.contadorretroceso==9:
                self.atacado = False



            self.hitbox = (self.x - camaraFinal.cameraX, self.y, 32, 32)




    def move(self):
        if self.tocado:
            self.contadorretroceso=0
            if self.restarvida and self.atacado:
                self.vida -= 1
                self.restarvida = False
            else:
                self.restarvida = False
        if self.contadorretroceso>=10:
            self.restarvida = True
            if self.path[1] > self.path[0]:
                if self.vel > 0:
                    if self.x + self.vel < self.path[1]:
                        self.x += self.vel

                    else:
                        self.vel = self.vel * -1
                        self.walkCount = 0
                else:
                    if self.x - self.vel > self.path[0]:
                        self.x += self.vel

                    else:
                        self.vel = self.vel * -1
                        self.walkCount = 0
            else:
                if self.vel > 0:
                    if self.x + self.vel < self.path[0]:
                        self.x += self.vel

                    else:
                        self.vel = self.vel * -1
                        self.walkCount = 0
                else:
                    if self.x - self.vel > self.path[1]:
                        self.x += self.vel

                    # Sacar esta parte evita que se devuelvan.
                    #else:
                    #    self.vel = self.vel * -1
                    #    self.walkCount = 0
        #Esta es la parte que lo hace retroceder cuando es atacado
        if self.contadorretroceso<10:
            if gali.char == gali.character[1] or gali.char == gali.character[3]:
                self.x += 20
                self.tocado = False
                self.contadorretroceso += 1
                self.restarvida = False
            elif gali.char == gali.character[0] or gali.char == gali.character[2]:
                self.x -= 5
                self.tocado = False
                self.contadorretroceso += 1
                self.restarvida = False

            #self.extraSalto = random.randint(-20,20)


        # Salto
        if self.isJump is False and self.framesParaSalto == 0:
            self.isJump = True
            self.framesParaSalto = 10
        if self.isJump:
            if self.jumpCount > 0:
                self.y += (self.jumpCount ** 2) * (-0.015)
                self.jumpCount -= 1
            if self.jumpCount <= 0:
                self.y -= (self.jumpCount ** 2) * (-0.015)
                self.jumpCount -= 1
                if self.y >= self.yinicial:
                    self.y = self.yinicial
                    self.isJump = False
                    self.jumpCount = 30 + self.extraSalto
        else:
            self.framesParaSalto -= 1

    def hit(self):
        print(self.vida)
        self.tocado = True


# Permite poner cosas en el mapa. Tendrán la misma distancia entre dos.
class adorno(object):
    global camaraFinal

    def __init__(self, numeroDePostes, diseño):
        self.numeroDePostes = numeroDePostes
        self.diseño = diseño

    def draw(self, win):
        for p in range(self.numeroDePostes):
            win.blit(self.diseño, (87.295 + 996.41 * p - camaraFinal.cameraX, 376))


class estrellas(object):
    global camaraFinal

    def __init__(self, Img, numEstrellas):
        self.numEstrellas = numEstrellas
        self.estrellasImg = Img
        self.estrellasX = []
        self.estrellasY = []
        # 0 si no aparece, 1 si aparece
        self.aparecerEstrella = []
        for i in range(self.numEstrellas):
            self.aparecerEstrella.append(0)

        for i in range(self.numEstrellas):
            self.estrellasX.append(random.randint(1, 3200))
            self.estrellasY.append(random.randint(0, 540))

        self.sumatoriaparaestrellas = 0

    def draw(self, win, x):
        if x > 568 or camaraFinal.cameraX >= 332:
            for i in range(self.numEstrellas):
                if self.sumatoriaparaestrellas // 2000 == i:
                    self.aparecerEstrella[i] = 1
                    if i < (self.numEstrellas):
                        self.aparecerEstrella[i + 1] = 1
                    if i < self.numEstrellas - 1:
                        self.aparecerEstrella[i + 2] = 1
                    if i < self.numEstrellas - 2:
                        self.aparecerEstrella[i + 3] = 1

                if self.aparecerEstrella[i] == 1:
                    win.blit(self.estrellasImg, (self.estrellasX[i] - camaraFinal.cameraX, self.estrellasY[i]))
                else:
                    self.sumatoriaparaestrellas += 1


class camara(object):
    global gali

    def __init__(self):
        self.cambioEscenario = False
        self.cameraX = 0
        self.cam = 0
        self.velocidadCam = gali.vel
        self.distanciaCamara = 2000

    def draw(self, win):
        # Cambio de escenario
        if self.cambioEscenario is True:
            gali.x -= 0
            self.cam = self.velocidadCam

        else:
            self.cambioEscenario = False
            self.cam = 0
        self.cameraX += self.cam


# adorno(Número de adornos, imagen del adorno)
postes = adorno(6, poste)

# player(x , y , width, height, LISTA de imagenes para cuando está parado, Lista de imagenes para camina a la izquierda, lista para cuando camina a la derecha)
gali = player(50, 500, 64, 64, character, walkLeft, walkRight)

# estrellas(imagenestrella, numero de estrellas)
estrellapequeña = estrellas(estrellaPequena, 1000)
estrellamediana = estrellas(estrellaMediana, 200)

# camara
camaraFinal = camara()

ladridoFinal = ladrido()
# enemigo blob ( x, y, width, height, end)
blobs = []
for i in range(3):
    blobs.append(enemy(1200 + 1200 * i, 532, 32, 32, 0))

blob = enemy(50, 532, 32, 32, 50)


def redrawGameWindow():
    # dibujar fondo
    win.blit(fondo, (0 - camaraFinal.cameraX, 0))

    # Dibujar estrellas
    estrellapequeña.draw(win, gali.x)
    estrellamediana.draw(win, gali.x)

    # Aparecer postes a la misma distancia
    postes.draw(win)

    # Dibujar luna
    win.blit(luna, (2100 - camaraFinal.cameraX, 100))

    # Dibuja la barra de vida
    win.blit(barraImg, (10, 0))

    for i in range(3):
        blobs[i].draw(win)

    # Dibujar a gali
    if gali.retroceder is False:
        gali.draw(win)

    # Se pone rojo cuando lo golpean
    if gali.retroceder is True:
        if gali.char == gali.character[0] or gali.char == gali.character[2]:
            win.blit(gali.character[4], (gali.x, gali.y))

        if gali.char == gali.character[1] or gali.char == gali.character[3]:
            win.blit(gali.character[5], (gali.x, gali.y))
        # Dibuja la barra de vida
        pygame.draw.rect(win, (255, 0, 0), (12, 60, 396 - (100 - gali.health) * 3.96, 13))

    ladridoFinal.draw(win)

    # Movimiento de cámara
    camaraFinal.draw(win)

    pygame.display.update()


# mainloop
run = True
while run:
    # "Reloj" en ms frames per second
    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if not gali.retroceder:
        if keys[pygame.K_LEFT] and gali.x > gali.boundary_extra:
            camaraFinal.cambioEscenario = False
            gali.paradopormuchotiempo = 0
            gali.char = gali.character[0]
            gali.x -= gali.vel
            gali.left = True
            gali.right = False
        if keys[pygame.K_RIGHT] and gali.x < screenwidth - gali.width - gali.boundary_extra:
            gali.paradopormuchotiempo = 0
            gali.char = gali.character[1]
            # Hasta dónde la cámara sigue al personaje
            if gali.x < 236 or camaraFinal.cameraX > camaraFinal.distanciaCamara:
                camaraFinal.cambioEscenario = False
                gali.left = False
                gali.x += gali.vel
            elif gali.x >= 236 and camaraFinal.cameraX <= camaraFinal.distanciaCamara:
                camaraFinal.cambioEscenario = True
            gali.left = False
            gali.right = True

        # if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
        if not keys[pygame.K_RIGHT]:
            camaraFinal.cambioEscenario = False
            gali.right = False
            if gali.left is False:
                gali.walkCount = 0

        # if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
        if not keys[pygame.K_LEFT]:
            gali.left = False
            if gali.right is False:
                gali.walkCount = 0

        if keys[pygame.K_e] and ladridoFinal.ladridodenuevo is True:
            ladridoFinal.ladridoono = True
            ladridoFinal.ladridodenuevo = False

        if not gali.isJump:

            if keys[pygame.K_SPACE]:
                gali.paradopormuchotiempo = 0
                gali.isJump = True
                gali.right = False
                gali.left = False
                gali.walkCount = 0
                i = 0
        else:
            if gali.jumpCount >= -20:
                neg = 1
                if gali.jumpCount < 0:
                    neg = -1

                gali.y -= neg * (gali.jumpCount ** 2) * 0.06
                gali.jumpCount -= 1
                i = 1

            else:
                gali.isJump = False
                gali.jumpCount = 20

    # Retrocede si lo golpean
    else:
        if gali.char == gali.character[0] or gali.char == gali.character[2]:
            if gali.x + 15 < 1200:
                gali.x += 15
            else:
                gali.x = 1200

        if gali.char == gali.character[1] or gali.char == gali.character[3]:
            if gali.x - 15 > 0:
                gali.x -= 15
            else:
                gali.x = 0

    if event.type == pygame.KEYUP and event.key == pygame.K_e:
        ladridoFinal.ladridodenuevo = True

    # En este for van todos los ataques hacia y del enemigo
    for i in range(len(blobs)):

        # cuando el enemigo es atacado por ladrido
        if ((ladridoFinal.hitbox[0] - blobs[i].hitbox[0]) <= blobs[i].hitbox[2] and ladridoFinal.hitbox[2] >= (
                blobs[i].hitbox[0] - ladridoFinal.hitbox[0])) and ladridoFinal.dibujarladrido:
            if ((ladridoFinal.hitbox[1] - blobs[i].hitbox[1]) <= blobs[i].hitbox[3] and ladridoFinal.hitbox[3] >= (
                    blobs[i].hitbox[1] - ladridoFinal.hitbox[1])):
                blobs[i].atacado = True
                blobs[i].hit()

        #Eliminar a enemigo si se queda sin vidas:





        # para cuando el enemigo ataca a gali
        if ((gali.hitbox[0] - blobs[i].hitbox[0]) <= blobs[i].hitbox[2] and gali.hitbox[2] >= (
                blobs[i].hitbox[0] - gali.hitbox[0])):
            if ((gali.hitbox[1] - blobs[i].hitbox[1]) <= blobs[i].hitbox[3] and gali.hitbox[3] >= (
                    blobs[i].hitbox[1] - gali.hitbox[1])):
                if gali.tocado is False:
                    gali.hit()
                    blobs[i].tocado = True



                else:
                    pass

            else:
                gali.tocado = False



    gali.contadorGolpe()

    redrawGameWindow()

pygame.QUIT
