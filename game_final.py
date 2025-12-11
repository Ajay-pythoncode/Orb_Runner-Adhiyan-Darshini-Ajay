import pygame
import random 
import math

from sys import exit
winner=True
score=0
instr_timer=0
game_state='intro'
intro_start_timer=pygame.time.get_ticks()
class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60,60),pygame.SRCALPHA)
        pygame.draw.circle(self.image,(0,225,250),(30,30),15)
        self.rect = self.image.get_rect(center = (200,200))
        self.mask1 = pygame.mask.from_surface(self.image)
        self.vx, self.vy = 0,0
    def mvmt(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.vx = player_speed
            self.rect.x += self.vx
        elif keys[pygame.K_a]:
            self.vx = -player_speed
            self.rect.x += self.vx   
        if keys[pygame.K_w]:
            self.vy = -player_speed
            self.rect.y += self.vy
        elif keys[pygame.K_s]:
            self.vy = player_speed
            self.rect.y += self.vy 
    def boundary(self):
        if self.rect.x < -10:
            self.rect.x = -10
        if self.rect.x > 550:
            self.rect.x = 550
        if self.rect.y < -10:
            self.rect.y = -10
        if self.rect.y > 355:
            self.rect.y = 355
    def update(self):
        self.mvmt()
        self.boundary()
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60,60),pygame.SRCALPHA)
        pygame.draw.circle(self.image,(200,80,225),(30,30),15)
        self.rect = self.image.get_rect(center = (400,200))
        self.mask2 = pygame.mask.from_surface(self.image)
        self.vx,self.vy = 0,0
    def mvmt(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.vx = player_speed
            self.rect.x += self.vx
        elif keys[pygame.K_LEFT]:
            self.vx = -player_speed
            self.rect.x += self.vx   
        if keys[pygame.K_UP]:
            self.vy = -player_speed
            self.rect.y += self.vy
        elif keys[pygame.K_DOWN]:
            self.vy = player_speed
            self.rect.y += self.vy 
    def boundary(self):
        if self.rect.x < -10:
            self.rect.x = -10
        if self.rect.x > 550:
            self.rect.x = 550
        if self.rect.y < -10:
            self.rect.y = -10
        if self.rect.y > 355:
            self.rect.y = 355
    def update(self):
        self.mvmt()
        self.boundary()
class Block(pygame.sprite.Sprite):
    def __init__(self,x_pos,y_pos,width,height):
        super().__init__()
        self.image = pygame.Surface((width,height),pygame.SRCALPHA)
        pygame.draw.rect(self.image,(237, 237, 237),(0,0,width,height))
        self.rect = self.image.get_rect(center = (x_pos,y_pos))
        self.vx, self.vy = 0,0
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.x > 700 or self.rect.x < -100 or self.rect.y > 500 or self.rect.y < -100:
            self.kill()
def display_score():
    global score, instr_timer,intro_timer
    score = pygame.time.get_ticks() - restart_time - intro_timer- instr_timer
    score_surf = txt_font.render(str(score//150),True,"White")
    screen.blit(score_surf,(320,20))   
def initial_screen():
    pulse = (math.sin(pygame.time.get_ticks() * 0.004) + 1) * 2 + 15
    screen.fill((0,0,0))
    text=title_font.render('ORB RUNNER',True,(255,255,255))
    text_rect=text.get_rect()
    text_1=txt_font.render("Press space to start the game",True,(240,240,240))
    text_2 = txt_font.render("Press enter to view instructions",True,(240,240,240))
    text_1_rect=text_1.get_rect()
    text_2_rect = text_2.get_rect()
    pygame.draw.circle(screen, (0,200,255), (250,200), int(pulse))
    pygame.draw.circle(screen, (200,80,255), (350,200), int(pulse))
    pygame.draw.rect(screen, "white", (50, 50, 505, 300),width=3)
    text_rect.center = (300, 100)
    text_1_rect.center=(300,300)
    text_2_rect.center =(300,325)
    screen.blit(text,text_rect)
    screen.blit(text_1,text_1_rect)
    screen.blit(text_2,text_2_rect)
    pygame.display.flip()
def init_surf():
    global bg_surf,txt_surf,obst_surf,txt_font,obst_surf1,title_font,text_font
    bg_surf = pygame.image.load("BG.png").convert()
    title_font = pygame.font.Font('CaviarDreams_Bold.ttf',35)
    txt_font = pygame.font.Font('CaviarDreams_Bold.ttf',20)
    text_font= pygame.font.Font('CaviarDreams_Bold.ttf',25)
    txt_surf = txt_font.render("SCORE:",True,"White")
def obst_player_collision():
    def circle_rect_collision(circle_rect, radius, rect):
        cx, cy = circle_rect.center
        # Find closest point on the rectangle to the circle center
        closest_x = max(rect.left, min(cx, rect.right))
        closest_y = max(rect.top, min(cy, rect.bottom))
        dx = cx - closest_x
        dy = cy - closest_y
        #Check if radius is lesser than shortest distance
        return (dx*dx + dy*dy) < (radius * radius)
    p1 = player1.sprite.rect
    p2 = player2.sprite.rect

    for obst in block_group:
        global winner
        global final_score,score
        # check collision with player 1
        if circle_rect_collision(p1, 15, obst.rect):
            final_score=score
            winner = True
            return False

        # check collision with player 2
        if circle_rect_collision(p2, 15,obst.rect):
            final_score=str(score)
            winner =False
            return False

    return True
def player_player_collision(p1,p2,rad):
    x1,y1 = p1.rect.center
    x2,y2 = p2.rect.center

    dx = x2-x1
    dy= y2-y1
    dist = math.hypot(dx,dy)
    min_dist = rad*2
    if dist == 0:
        dist = 0.01
    if dist<min_dist:
        overlap = min_dist - dist
        nx = dx/dist
        ny = dy/dist

        p1.rect.x -= nx*(overlap/2)
        p1.rect.y -= ny*(overlap/2)
        p2.rect.x += nx*(overlap/2)
        p2.rect.y += ny*(overlap/2)

        v1n = (p1.vx*nx) + (p1.vy*ny)
        v2n = (p2.vx*nx) + (p2.vy*ny)

        p1.vx += (v2n - v1n) * nx *1.2
        p2.vx += (v1n-v2n)*nx*1.2
        p2.vy += (v1n-v2n)*ny*1.2

        lmt = 12
        p1.vx = max(-lmt,min(lmt,p1.vx))
        p1.vy = max(-lmt,min(lmt,p1.vy))
        p2.vx = max(-lmt,min(lmt,p2.vx))
        p2.vy = max(-lmt,min(lmt,p2.vy))
def game_over():
    global winner, instr_timer
    screen.fill((0,0,0))
    pygame.draw.rect(screen, "white", (50, 50, 505, 300),width=3)
    text_1=(title_font.render("GAME OVER",True,(255,255,255)))
    text_1_rect=text_1.get_rect()
    text_1_rect.center=(300,100)
    screen.blit(text_1,text_1_rect)
    text_2=(txt_font.render(f"Score:{score//150}",True,(255,255,255)))
    text_2_rect=text_2.get_rect()
    text_2_rect.center=(300,150)
    text_4=(txt_font.render('Press Space to play again',True,'White'))
    text_4_rect=text_4.get_rect()
    text_4_rect.center=(300,250)
    text_5=(txt_font.render('Press Enter to exit',True,'White'))
    text_5_rext=text_5.get_rect()
    text_5_rext.center=(300,300)
    screen.blit(text_2,text_2_rect)
    screen.blit(text_4,text_4_rect)
    screen.blit(text_5,text_5_rext)
    if winner:
        text_3=(txt_font.render('Player 2 wins the game',True,'White'))
    else:
        text_3=(txt_font.render('Player 1 wins the game',True,'White'))
    text_3_rect=text_3.get_rect()
    text_3_rect.center=(300,200)
    screen.blit(text_3,text_3_rect)
    
    block_group.empty()
    global game_active,speed,player_speed
    game_active = True
    player1.sprite.rect.center = (200, 200)
    player2.sprite.rect.center = (400, 200)
    speed,player_speed = 0,7
def obst_spawn_pattern():
    global speed
    def vertical_sweep(group):
        block = Block(random.choice([225,375]),-15,300,30)
        block.vy = 2 + speed
        group.add(block)
    def cluster(group):
        for i in range(4):
            block = Block(random.randint(45,555),random.randint(-255,0),random.randint(35,80),random.randint(35,80))
            pygame.sprite.spritecollide(block,block_group,True)
            block.vy = 3 + speed
            group.add(block)
    def alt_bar(group):
        block_1 = Block(200,-15,100,30)
        block_2 = Block(450,-185,150,30)
        block_1.vy,block_2.vy, = 1 + speed,1 + speed
        group.add(block_1,block_2)
    def double_gap(group):
        block_1 = Block(200, -25, 150, 40)
        block_2 = Block(400, -25, 150, 40) 
        block_1.vy,block_2.vy = 2 + speed,2 + speed
        group.add(block_1, block_2)
    def side_rain(group):
        for i in range(5):
            block = Block(640, random.randint(50,350), 40, 40)
            block.vx = random.uniform(-2, -4) - speed
            group.add(block)
    def corridor(group):
        block_1 = Block(100, -30, 100, 40)
        block_2 = Block(500, -30, 100, 40)
        block_1.vy,block_2.vy = 2 + speed,2 + speed
        group.add(block_1,block_2)
    def crusher(group):
        left = Block(-40, 200, 60, 150)
        right = Block(640, 200, 60, 150)
        left.vx,right.vx = 2 + speed,-2 - speed
        group.add(left, right)

    spawn = [cluster,cluster,cluster,vertical_sweep,alt_bar,double_gap,side_rain,corridor,crusher]
    random.choice(spawn)(block_group)
def instructions():
    screen.fill((0,0,0))
    pygame.draw.rect(screen, "white", (50, 50, 505, 300),width=3)
    title=title_font.render('INSTRUCTIONS',True,'White')
    title_rect=title.get_rect()
    title_rect.center=(300,100)
    screen.blit(title,title_rect)
    text='-> Welcome to Orb Runner!\n-> Player 1 can use A/D/W/S keys and Player 2 can\n' \
    '     use the arrow keys to move left, right, up, down\n-> Avoid the falling obstacles'
    lines = text.split("\n")
    y = 150  # starting height

    for line in lines:
        surface = txt_font.render(line, True, "white")
        rect = surface.get_rect(midleft=(55, y))
        screen.blit(surface, rect)
        y += 40
    txt=txt_font.render('PRESS SPACE TO START THE GAME',True,'White')
    txt_rect=txt.get_rect()
    txt_rect.center=(300,310)
    screen.blit(txt,txt_rect)
    pygame.display.flip()
    pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((600,400),pygame.FULLSCREEN)
pygame.display.set_caption("Orb Runner")

clock = pygame.time.Clock()
game_active = True
restart_time = 0
speed = 0
player_speed= 7 

player1 = pygame.sprite.GroupSingle()
player2 = pygame.sprite.GroupSingle()
obst_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()
player1.add(Player1())
player2.add(Player2())

init_surf()

speed_inc = pygame.USEREVENT + 1
pattern_spawn = pygame.USEREVENT + 2
pygame.time.set_timer(speed_inc,2500)
pygame.time.set_timer(pattern_spawn,2500)

while True:
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == speed_inc and game_active:
            speed += 0.1
        elif event.type == pattern_spawn and game_active:
            if len(block_group) == 0:
                obst_spawn_pattern()
        if game_state=='intro':
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                intro_timer = pygame.time.get_ticks() - intro_start_timer
                game_state='running'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                intro_timer = pygame.time.get_ticks() - intro_start_timer
                instr_start_time = pygame.time.get_ticks()
                game_state = 'instr'
        elif game_state=='instr':
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                instr_timer = pygame.time.get_ticks() - instr_start_time
                game_state= 'running'
        elif game_state == "game_over":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                intro_timer = 0
                instr_timer = 0
                intro_start_timer = pygame.time.get_ticks()
                restart_time = pygame.time.get_ticks()
                game_state='running'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                pygame.quit()
                exit()
    if game_state=='intro':
        initial_screen()
    elif game_state=='instr':
        instructions()
    elif game_state=='running':
        #Static surfaces
        screen.blit(bg_surf,(0,0))
        screen.blit(txt_surf,(225,20))
        #Mobile surfaces
        player1.draw(screen)
        player2.draw(screen)
        obst_group.draw(screen)
        block_group.draw(screen)

        player_player_collision(player1.sprite,player2.sprite,15)
        player1.sprite.boundary()
        player2.sprite.boundary()

        display_score()

        player1.update()
        player2.update()
        block_group.update()

        if not obst_player_collision():
            game_state='game_over'
    else:
        game_over()
    pygame.display.update()
    clock.tick(60)