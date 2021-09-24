import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()

menu_Flag = {'menu' : True, 'game' : False, 'main' : True}
menu_Surface = pygame.image.load('sprites/misc/menu.png')
game_Surface = pygame.image.load('sprites/b_screen/b_background.png')
def main_menu():
    while menu_Flag['main']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                game()

        screen.blit(menu_Surface,(0,0))
        pygame.display.update()
        clock.tick(60)

def game():
    menu_Flag['game'] = True
    while menu_Flag['game']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                menu_Flag['game'] = False

        screen.blit(game_Surface,(0,0))
        pygame.display.update()
        clock.tick(60)

def draw_Cursor():
    while menu_Flag['main']:
        

main_menu()