import pygame
import random
import math
from pygame import mixer

# Initialize the pygame
pygame.init()
# create the screen tamaño (x,y)
screen = pygame.display.set_mode((800, 600))

# fondo
fondo = pygame.image.load('fondo.png')
# fondo sonido
mixer.music.load('Boss Battle - The Legend of Zelda Ocarina of Time.wav')
#mixer.music.play(-1)
# Title and Icon
pygame.display.set_caption("Gali vs Aliens")
icon = pygame.image.load('Pixel art gali 1.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('Pixel art gali grande.png').convert()
playerImg.set_colorkey((255, 255, 255))

playerImg = pygame.transform.scale(playerImg, (64, 64))

playerX = 368
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(1, 735))
    enemyY.append(50)
    enemyX_change.append(2.5)
    enemyY_change.append(80)

# Bala

# Ready - Todavía no se ve
# Fire - la bala se está moviendo
bulletImg = pygame.image.load('bala.png')
bulletImg.set_colorkey((255, 255, 255))
bulletImg = pygame.transform.scale(bulletImg, (24, 24))
bulletX = 0
bulletY = 480
bulletX_change = 0  # No importa para la bala
bulletY_change = 5
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game over

over_font = pygame.font.Font('freesansbold.ttf', 64)
denuevo_font = pygame.font.Font('freesansbold.ttf', 32)


def game_over_text():
    over_text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (300, 250))
    denuevo_text = font.render("Press space to play again", True, (255, 255, 255))
    screen.blit(denuevo_text, (215, 300))


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, j):
    screen.blit(enemyImg[j], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Controlar la colision, ver la distancia entre dos objetos
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 30:
        return True
    else:
        return False


def isgameover(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 50:
        return True
    else:
        return False


running = True
reinicio = 1

while running:

    if reinicio == 1:


        screen.fill((255, 255, 255))
        # agregar fondo
        screen.blit(fondo, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if keystroke is pressed, check wether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -3
                if event.key == pygame.K_RIGHT:
                    playerX_change = 3
                # Bala
                if event.key == pygame.K_SPACE and bullet_state == 'ready' and enemyY[1] < 2000:
                    fire_bullet(playerX, bulletY)
                    bulletX = playerX

                # Reiniciar el juego cuando está en gameover
                if event.key == pygame.K_SPACE and bullet_state == 'ready' and enemyY[1] >= 2000:
                    print('reinicio')
                    reinicio = 2
                    break

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and playerX_change < 0:
                    playerX_change = 0

                if event.key == pygame.K_RIGHT and playerX_change > 0:
                    playerX_change = 0

        # Se pone esta suma afuera porque cada momento se revisar este for y una vez que se ve que se cumple se sale
        # Boundaries para que no salga de la pantalla
        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        for j in range(num_of_enemies):

            if isgameover(enemyX[j], enemyY[j], playerX, playerY) is True:
                gameover = True
                break
            else:
                gameover = False

        # Game over
        if gameover is True or enemyY[1] >= 2000:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()

        for i in range(num_of_enemies):

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = -enemyX_change[i]
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -enemyX_change[i]
                enemyY[i] += enemyY_change[i]

            # collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)

            if collision is True:
                bulletY = 480
                bullet_state = 'ready'
                score_value += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = 50

            enemy(enemyX[i], enemyY[i], i)

        # Bullet movement, si sale de la pantalla se reinicia la función para poder disparar otra bala
        if bulletY <= -20:
            bullet_state = 'ready'
            bulletY = 480
        if bullet_state == 'fire':
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score(textX, textY)

        pygame.display.update()

    #Reiniciar le juego
    else:


        enemyX = []
        enemyY = []
        enemyX_change = []
        enemyY_change = []
        num_of_enemies = 6
        for i in range(num_of_enemies):

            enemyX.append(random.randint(1, 735))
            enemyY.append(50)
            enemyX_change.append(2.5)
            enemyY_change.append(80)

        score_value = 0

        reinicio = 1






        if gali.jumpCount >= -15:
            neg = 1
            if gali.jumpCount < 0:
                neg = -1
            if i==1:
                gali.y -= neg * (gali.jumpCount ** 2) * 0.2
                gali.jumpCount -= 1
                i = 1
            else:
                i += 1

        else:
            gali.isJump = False
            gali.jumpCount = 15
