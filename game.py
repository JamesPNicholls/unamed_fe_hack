import pygame
class CGame:
    def __init__(self,screen):
        CGame.screen = screen
        CGame.game_Map = pygame.image.load('sprites/map/map_Demo.png').convert()
        return

    def game_Event_Loop(self, game_State_Flags):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_State_Flags['end_Application'] = True
                game_State_Flags['in_Game_Screen']  = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_State_Flags['in_Game_Screen']      = False
                    game_State_Flags['in_Main_Menu'] = True
        return
    def draw_Game(*args):  
        CGame.screen.blit( CGame.game_Map, (0,0))
        return
    
