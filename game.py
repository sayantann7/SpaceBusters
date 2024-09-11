import pygame
import random

pygame.init()
pygame.mixer.init()
screenSize = (800, 600)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("SpaceBusters")
pygame.display.set_icon(pygame.image.load('assets/player.png'))
running = True
game_over = False
pygame.mouse.set_visible(False)  


pixelated_font = pygame.font.Font('assets/mainscreenlowerfont.ttf', 40)
pixelated_font_capital = pygame.font.Font('assets/mainscreenlowerfont.ttf', 90)

images_size = (120,120)

IMG1 = pygame.transform.scale(pygame.image.load('assets/img1.png'), images_size)
IMG2 = pygame.transform.scale(pygame.image.load('assets/img2.png'), images_size)
IMG3 = pygame.transform.scale(pygame.image.load('assets/img3.png'), images_size)
IMG4 = pygame.transform.scale(pygame.image.load('assets/img4.png'), images_size)
IMG5 = pygame.transform.scale(pygame.image.load('assets/img5.png'), images_size)
IMG6 = pygame.transform.scale(pygame.image.load('assets/img6.png'), images_size)
IMG7 = pygame.transform.scale(pygame.image.load('assets/img7.png'), images_size)

# Load and play background music
bullet_sound = pygame.mixer.Sound('assets/bullet.mp3')
bullet_sound.set_volume(0.3)
pygame.mixer.music.load('assets/bgmusic.mp3')  
pygame.mixer.music.play(-1)  
pygame.mixer.music.set_volume(0.3)

def img1(x,y):
    screen.blit(IMG1,(x,y))
def img2(x,y):
    screen.blit(IMG2,(x,y))
def img3(x,y):
    screen.blit(IMG3,(x,y))
def img4(x,y):
    screen.blit(IMG4,(x,y))
def img5(x,y):
    screen.blit(IMG5,(x,y))
def img6(x,y):
    screen.blit(IMG6,(x,y))
def img7(x,y):
    screen.blit(IMG7,(x,y))

num_stars = 20  
star_positions = [(random.randint(0, 800), random.randint(0, 600)) for _ in range(num_stars)]

num_stars_welcome_screen = 18  
star_positions_welcome_screen = [(random.randint(0, 800), random.randint(0, 400)) for _ in range(num_stars_welcome_screen)]

starIMG = pygame.transform.scale(pygame.image.load('assets/star.png'), (10, 10))

def draw_stars():
    for pos in star_positions:
        screen.blit(starIMG, pos)
def draw_stars_welcome_screen():
    for pos in star_positions_welcome_screen:
        screen.blit(starIMG, pos)

font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

score = 0
high_score = 0

playerIMG = pygame.transform.scale(pygame.image.load('assets/player.png'), (64, 64))
playerX = 375
playerY = 500
playerX_change = 0
playerSpeed = 0.2

playerBulletIMG = pygame.transform.scale(pygame.image.load('assets/playerBullet.png'), (50, 50))
playerBulletX = playerX + 7
playerBulletY = playerY - 45
playerBulletChangeY = 0.4
bullet_fired = False  
enemyIMG = pygame.transform.scale(pygame.image.load('assets/enemy.png'), (60, 60))
enemyY = 0
enemyX = random.randint(0, 740)
enemy1change = 0.08

enemy2IMG = pygame.transform.scale(pygame.image.load('assets/enemy.png'), (60, 60))
enemy2Y = 65
enemy2X = random.randint(0, 740)
enemy2change = -0.03

enemyBullet1IMG = pygame.transform.scale(pygame.image.load('assets/enemyBullet.png'), (50, 50))
enemyBullet1X = enemyX+7
enemyBullet1Y = enemyY+45

enemyBullet2IMG = pygame.transform.scale(pygame.image.load('assets/enemyBullet.png'), (50, 50))
enemyBullet2X = enemy2X+7
enemyBullet2Y = enemy2Y+45

enemyBulletChangeY = -0.3

def player(x, y):
    screen.blit(playerIMG, (x, y))

def player_shoot_bullets(x, y):
    screen.blit(playerBulletIMG, (x, y))

def enemy1():
    screen.blit(enemyIMG, (enemyX, enemyY))

def enemy2():
    screen.blit(enemy2IMG, (enemy2X, enemy2Y))

def enemy_bullet_1(x,y):
    screen.blit(enemyBullet1IMG,(x,y))

def enemy_bullet_2(x,y):
    screen.blit(enemyBullet2IMG,(x,y))

def show_score(score):
    score_text = pixelated_font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 560))

def game_over_screen():
    pygame.mixer.music.set_volume(0.0)
    game_over_text = pixelated_font_capital.render("GAME OVER", True, (255, 0, 0))
    final_score_text = pixelated_font.render(f"Final Score: {score}", True, (255, 255, 255))
    file = open("assets/score.txt", "r") 
    score_from_text = int(file.read())
    file.close()

    if score > score_from_text:
        high_score = score
        with open("assets/score.txt", "w") as file2:
            file2.write(str(score))
    else:
        high_score = score_from_text

    high_score_text = pixelated_font.render(f"High Score : {high_score}", True, (255, 255, 255))
    restart_text = pixelated_font.render("Press W to Restart or ESC to Quit", True, (255, 255, 255))

    game_over_rect = game_over_text.get_rect(center=(screenSize[0] / 2, screenSize[1] / 2 - 100))
    final_score_rect = final_score_text.get_rect(center=(screenSize[0] / 2, screenSize[1] / 2))
    high_score_rect = high_score_text.get_rect(center=(screenSize[0] / 2, screenSize[1] / 2 + 50))
    restart_rect = restart_text.get_rect(center=(screenSize[0] / 2, screenSize[1] / 2 + 100))


    screen.blit(game_over_text, game_over_rect)
    screen.blit(final_score_text, final_score_rect)
    screen.blit(high_score_text, high_score_rect)
    screen.blit(restart_text, restart_rect)

def welcome_screen():
    pixel_font = pygame.font.Font('assets/mainscreenfont.ttf', 100)
    pixel_font2 = pygame.font.Font('assets/mainscreenlowerfont.ttf', 40)
    title_text = pixel_font.render("SpaceBusters", True, (255, 255, 255))
    instruction_text = pixel_font2.render("Press W to Start", True, (255, 255, 255))
    

    title_rect = title_text.get_rect(center=(screenSize[0] / 2, screenSize[1] / 2 - 50))
    instruction_rect = instruction_text.get_rect(center=(screenSize[0] / 2, screenSize[1] / 2 + 50))

    while True:
        screen.fill((0, 0, 0))  

        img7(0,450)
        img1(115,450)
        img2(230,450)
        img3(345,450)
        img4(465,450)
        img5(570,450)
        img6(685,450)
        draw_stars_welcome_screen()
        # Display the title and instructions
        screen.blit(title_text, title_rect)
        screen.blit(instruction_text, instruction_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:  
                    return

welcome_screen()
pygame.mixer.music.set_volume(1.0)


while running:
    screen.fill((0, 0, 0))
    draw_stars()

    if game_over:
        game_over_screen()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    # Restart game
                    game_over = False
                    score = 0
                    pygame.mixer.music.set_volume(0.3)
                    playerX = 375
                    playerBulletY = playerY - 45
                if event.key == pygame.K_ESCAPE:
                    running = False
        continue

    if bullet_fired and (playerBulletY <= enemyY + 60 and playerBulletY >= enemyY and playerBulletX >= enemyX and playerBulletX <= enemyX + 60):
        score += 10
        bullet_fired = False
        playerBulletY = playerY - 45
        enemyX = random.randint(0, 740)
        enemyY = 0

    if bullet_fired and (playerBulletY <= enemy2Y + 60 and playerBulletY >= enemy2Y and playerBulletX >= enemy2X and playerBulletX <= enemy2X + 60):
        score += 10
        bullet_fired = False
        playerBulletY = playerY - 45
        enemy2X = random.randint(0, 740)
        enemy2Y = 65

    if (enemyBullet1Y >= playerY-64 and (enemyBullet1X >= playerX and enemyBullet1X <= playerX + 64)) or (enemyBullet2Y >= playerY-64 and (enemyBullet2X >= playerX and enemyBullet2X <= playerX + 64)):
        game_over = True

    enemy_bullet_1(enemyBullet1X, enemyBullet1Y)
    enemyBullet1Y -= enemyBulletChangeY
    if enemyBullet1Y >= 550:  
        enemyBullet1Y = enemyY + 45
        enemyBullet1X = enemyX + 7

    enemy_bullet_2(enemyBullet2X, enemyBullet2Y)
    enemyBullet2Y -= enemyBulletChangeY
    if enemyBullet2Y >= 550: 
        enemyBullet2Y = enemy2Y + 45
        enemyBullet2X = enemy2X + 7

    player(playerX, playerY)
    enemy1()
    enemy2()

    if enemyX >= 740:
        enemy1change = -0.03
    if enemyX <= 0:
        enemy1change = 0.03
    if enemy2X >= 740:
        enemy2change = -0.03
    if enemy2X <= 0:
        enemy2change = 0.03
    enemyX += enemy1change
    enemy2X += enemy2change

    if bullet_fired:
        player_shoot_bullets(playerBulletX, playerBulletY)
        playerBulletY -= playerBulletChangeY
        if playerBulletY < -50:  
            bullet_fired = False
            playerBulletY = playerY - 45
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and not bullet_fired:  
                bullet_fired = True
                bullet_sound.play()
                playerBulletX = playerX + 7 
                playerBulletY = playerY - 45
            if event.key == pygame.K_LEFT:
                playerX_change = -playerSpeed
            if event.key == pygame.K_RIGHT:
                playerX_change = playerSpeed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    show_score(score)
    pygame.display.update()

pygame.quit()