def imagenes():
# Cargar las imágenes
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

luna = pygame.image.load('luna.png').convert()
luna.set_colorkey((255, 255, 255))

estrellaPequena = pygame.image.load('estrella pequeña.png').convert()

postes = pygame.image.load('poste.png').convert()
postes.set_colorkey((255, 255, 255))



# Animación de caminar
        if self.walkCount + 1 >= 48:
            self.walkCount = 0
        if self.left:

            win.blit(walkLeft[self.walkCount // 8], (self.x, self.y))
            self.walkCount += 1
        elif right:
            win.blit(walkRight[self.walkCount // 8], (self.x, self.y))
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