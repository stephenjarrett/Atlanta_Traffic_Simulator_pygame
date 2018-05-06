#run game with pythonw <gamename>
import pygame
import time
from enemy import Enemy
from vehicle import *
from timer import Timer
import random

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
background_crash = (0, 0, 0)
background_height = 650
background_width = 840
size = (background_width, background_height)
screen = pygame.display.set_mode(size)
fps = 60


#sizes
car_width = 175
car_height = 140
left_start = 161
move_x = 129
move_y = 140
start_y = background_height - car_height/2
lane1_x = left_start + (move_x/2)
lane2_x = lane1_x + move_x
lane3_x = lane1_x + move_x*2
lane4_x = lane1_x + move_x*3
left_border = 190
right_border = 521 + move_x
bottom_border = 533
top_border = 90
enemy_car_start_y = 20
enemy_lane1 = (lane1_x, enemy_car_start_y)
enemy_lane2 = (lane2_x, enemy_car_start_y)
enemy_lane3 = (lane3_x, enemy_car_start_y)
enemy_lane4 = (lane4_x, enemy_car_start_y)
enemy_lanes = (enemy_lane1, enemy_lane2, enemy_lane3, enemy_lane4)

#difficulty parameters
easy_mode = .55
medium_mode = .65
hard_mode = .70
atlanta_mode = 1

background = pygame.image.load('./images/background.png')
clock = pygame.time.Clock()
clock.tick(fps)

pygame.display.set_caption('ATLANTA TRAFFIC SIMULATOR')
car_choice = vehicle_images[0]

#fonts and texts (score text is in outro screen due to embeded var)
font = pygame.font.SysFont("Times New Roman", 30)
large_font = pygame.font.SysFont('Times New Roman', 60, 5)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
awesome_counting_color = (51, 255, 255)
color_list = [white, green, red, blue]
you_lose_text = font.render(('You LOSE!'), 1, awesome_counting_color)
you_lose_text_rect = you_lose_text.get_rect(center=(size[0]/2, size[1]/2 - 25))
player_options_text = font.render(('Press ENTER to play again or ESCAPE to exit'), 1, awesome_counting_color)
player_options_text_rect = player_options_text.get_rect(center=(size[0]/2, size[1]/2 + 25)) 
atlanta_text = large_font.render(('ATLANTA'),1, color_list[0])
atlanta_text_rect = atlanta_text.get_rect(center=(size[0]/2, size[1]/2 - 100))
traffic_text = large_font.render(('TRAFFIC'), 1, color_list[0])
traffic_text_rect = traffic_text.get_rect(center=(size[0]/2, size[1]/2 - 50))
simulator_text = large_font.render(('SIMULATOR'), 1, color_list[0])
simulator_text_rect = simulator_text.get_rect(center=(size[0]/2 -2, size[1]/2))
player_options2_text = font.render(('Press ENTER to continue'), 1, color_list[0])
player_options2_text_rect = player_options2_text.get_rect(center=(size[0]/2 -3, size[1]/2 + 150))
stephen_jarrett_text = font.render(('-Stephen Jarrett'), 1, color_list[0])
stephen_jarrett_text_rect = stephen_jarrett_text.get_rect(center=(size[0]/2, size[1]/2 + 40))
select_car_text = font.render(('Press LEFT ARROW and RIGHT ARROW to select your car'), 1, color_list[0])
select_car_text_rect = select_car_text.get_rect(center=(size[0]/2, size[1]/2 - 150))
press_enter_text = font.render(('Press ENTER when ready'), 1, color_list[0])
press_enter_text_rect = press_enter_text.get_rect(center=(size[0]/2, size[1]/2 + 150))

def intro():
    intro = True
    title_text = True
    pygame.mixer.music.load('./sounds/game_intro.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)
    car_choice_count = 0

    atlanta_text = large_font.render(('ATLANTA'), 1, color_list[0])
    traffic_text = large_font.render(('TRAFFIC'), 1, color_list[0])
    simulator_text = large_font.render(('SIMULATOR'), 1, color_list[0])
    player_options2_text = font.render(('Press ENTER to continue'), 1, color_list[0])
    stephen_jarrett_text = font.render(('-Stephen Jarrett'), 1, color_list[0])

    screen.blit(atlanta_text,atlanta_text_rect)
    screen.blit(traffic_text, traffic_text_rect)
    screen.blit(simulator_text, simulator_text_rect)
    screen.blit(player_options2_text,player_options2_text_rect)
    screen.blit(stephen_jarrett_text,stephen_jarrett_text_rect)
    pygame.display.update()
    
    title_text_count = 0
    color_picker = 0
    while title_text == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
                title_text = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                title_text = False

        #cycle through color list for title    
        if title_text_count % 35000 == 0:
            atlanta_text = large_font.render(('ATLANTA'),1, color_list[color_picker])
            traffic_text = large_font.render(('TRAFFIC'), 1, color_list[color_picker])
            simulator_text = large_font.render(('SIMULATOR'), 1, color_list[color_picker])
            player_options2_text = font.render(('Press ENTER to continue'), 1, color_list[color_picker])
            stephen_jarrett_text = font.render(('-Stephen Jarrett'), 1, color_list[color_picker])
            color_picker += 1
            title_text_count = 0

            screen.fill(black)
            pygame.display.update()
            screen.blit(atlanta_text, atlanta_text_rect)
            screen.blit(traffic_text, traffic_text_rect)
            screen.blit(simulator_text, simulator_text_rect)
            screen.blit(player_options2_text, player_options2_text_rect)
            screen.blit(stephen_jarrett_text, stephen_jarrett_text_rect)
            pygame.display.update()
        title_text_count += 1
        if color_picker >= len(color_list):
            color_picker = 0
        
    
    while intro == True:
        screen.fill(background_crash)
        car_choice = pygame.image.load(vehicle_images[car_choice_count])
        car_choice_rect = car_choice.get_rect(center=(size[0]/2, (size[1]/2)))
        screen.blit(car_choice, car_choice_rect)
        screen.blit(select_car_text,select_car_text_rect)
        screen.blit(press_enter_text, press_enter_text_rect)
        pygame.display.update()
        
        car_picked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
                intro = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                intro = False

            while car_picked == False:
                for event in pygame.event.get():
                    if car_choice_count > len(vehicle_images)-1:
                        car_choice_count = 0
                    elif car_choice_count == -1:
                        car_choice_count = len(vehicle_images)-1
                    
                    screen.fill(background_crash)
                    car_choice = pygame.image.load(vehicle_images[car_choice_count])
                    screen.blit(car_choice, car_choice_rect)
                    screen.blit(select_car_text, select_car_text_rect)
                    screen.blit(press_enter_text, press_enter_text_rect)
                    pygame.display.update()

                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        pygame.quit()
                        quit()
                        intro = False
                        car_picked = True
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                        screen.fill(background_crash)
                        car_choice_count += 1
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                        screen.fill(background_crash)
                        car_choice_count -= 1
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        car_picked == True
                        pygame.mixer.music.fadeout(750)
                        return car_choice_count
           
    pygame.mixer.music.fadeout(1500)

def pick_car(vehicle_images):
    #will add this in later to shrink code in intro fn
    pass

def outro(results_screen, play_again, player_score):
    while results_screen == True and play_again == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    results_screen = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    play_again = False
                    results_screen = False
                    pygame.quit()
                    quit()
            screen.fill(background_crash)

            your_score_text = font.render(
                ('Your score: %.0f' % player_score), 1, awesome_counting_color)
            your_score_text_rect = your_score_text.get_rect(
                center=(size[0]/2, size[1]/2))

            screen.blit(you_lose_text, you_lose_text_rect)
            screen.blit(your_score_text, your_score_text_rect)
            screen.blit(player_options_text, player_options_text_rect)

            pygame.display.update()
    
def main():
    
    play_again = True
    count = 0
    while play_again == True: 
        screen.fill(background_crash)
        pygame.display.update()
        car_choice_count = intro()

        #Calling on timer class for scorekeepeing
        score_timer = Timer()

        #Create player sprite and add to player group for collisions
        player = Vehicle((lane2_x, start_y), car_choice_count)
        player_group = pygame.sprite.Group()
        player_group.add(player)
        
        #load and play music
        pygame.mixer.music.load('./sounds/racing.mp3')
        pygame.mixer.music.play(-1)

        #list to append with RNG
        enemy_list = []

        #creating ranges for random speeds
        easy_speed_start = 7
        easy_speed_end = 9
        medium_speed_start = 9
        medium_speed_end = 12
        hard_speed_start = 11
        hard_speed_end = 14
        atlanta_speed_start = 14
        atlanta_speed_end = 18
        speed_start = easy_speed_start
        speed_end = easy_speed_end
        mode = easy_mode
        spawn_time =28

        lose = False
        #Main gameplay loops
        while not lose and play_again == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play_again = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    play_again = False
                
                #Controls
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.x_speed = -20
                    elif event.key == pygame.K_RIGHT:
                        player.x_speed = 20
                    elif event.key == pygame.K_UP:
                        player.y_speed = -20
                    elif event.key == pygame.K_DOWN:
                        player.y_speed = 20
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        player.x_speed = 0
                    elif event.key == pygame.K_RIGHT:
                        player.x_speed = 0
                    elif event.key == pygame.K_UP:
                        player.y_speed = 0
                    elif event.key == pygame.K_DOWN:
                        player.y_speed = 0

            #restricts where player can go
            player.rect.bottom = min(player.rect.bottom, background_height + 20)
            player.rect.top = max(player.rect.top, -20)
            player.rect.right = min(player.rect.right, right_border)
            player.rect.left = max(player.rect.left, left_border)
            
            screen.fill(background_crash)
            pygame.display.update()
                
            counting_string = 'Score: %.0f' % ((score_timer.get()/1000))

            counting_text = font.render(str(counting_string), 1, awesome_counting_color)
            counting_rect = counting_text.get_rect()
            counting_rect.center = (775,15)

            #uses the timer to determine and apply the game difficulty
            if score_timer.get()/1000 > 20 and score_timer.get()/1000 < 40:
                speed_start = medium_speed_start
                speed_end = medium_speed_end
                mode = medium_mode
                spawn_time = 25
            elif score_timer.get()/1000 > 40 and score_timer.get()/1000 < 80:
                speed_start = hard_speed_start
                speed_end = hard_speed_end
                mode = hard_mode
                spawn_time = 20
            elif score_timer.get()/1000 > 80:
                speed_start = atlanta_speed_start
                speed_end = atlanta_speed_end
                mode = atlanta_mode
                spawn_time = 18
                
            #randomly spawn enemy cars
            if count % spawn_time == 0:
                if random.random() < mode:
                        enemy_list.append(Enemy(enemy_lanes[random.randint(0,1)], random.randrange(speed_start,speed_end)))
                if random.random() < mode:
                        enemy_list.append(Enemy(enemy_lanes[random.randint(2,3)], random.randrange(speed_start,speed_end)))
                
            player.update()
            
            enemy_list_group = pygame.sprite.Group(enemy_list)
            
            crash = pygame.sprite.spritecollide(player, enemy_list_group, True)
            
            #crash occured - stop music and exit lose loop
            if crash:
                player.kill()
                score_timer.pause()
                player.score = int((score_timer.get()/1000))
                # pygame.mixer.music.stop()
                pygame.mixer.music.fadeout(50)
                pygame.mixer.music.load('./sounds/play_again.mp3')
                pygame.mixer.music.play(-1)
                player.rect.x = lane1_x
                player.rect.y = start_y
                lose = True

            screen.blit(background,(0,0))
            screen.blit(counting_text,counting_rect)
            player_group.draw(screen)
            enemy_list_group.draw(screen)

            pygame.display.update()
            clock.tick(fps)

            #kill sprites if they leave the screen
            for enemy in enemy_list:
                enemy.rect.y += enemy.speed
                if enemy.rect.y > 800:
                    enemy.kill()
                    enemy_list.remove(enemy)    
            
            #increment count for better spawn control
            count += 1

        #run outro function
        results_screen = True
        outro(results_screen, play_again, player.score)
        
    pygame.quit()

main()