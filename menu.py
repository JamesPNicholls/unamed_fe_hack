import pygame
class CMenu:

    def __init__(self, screen) -> None:
        CMenu.screen = screen

        CMenu.menu_Cursor_Pos = [0,100]

        CMenu.menu_Surface   = pygame.image.load('sprites/misc/menu.png').convert()
        CMenu.menu_Cursor    = pygame.image.load('sprites/misc/menu_Pointer.png')

        CMenu.top_Button     = pygame.image.load('sprites/misc/button_00.png')
        CMenu.bot_Button     = pygame.image.load('sprites/misc/button_00.png')

        CMenu.top_Button     = pygame.transform.scale(CMenu.top_Button, [700,250])
        CMenu.bot_Button     = pygame.transform.scale(CMenu.bot_Button, [700,250])
        return

    def draw_Menu(*args):
        CMenu.screen.blit(CMenu.menu_Surface,(0,0))

        CMenu.screen.blit(CMenu.top_Button,(10,10))
        CMenu.screen.blit(CMenu.bot_Button,(10,200))

        CMenu.screen.blit(CMenu.menu_Cursor, CMenu.menu_Cursor_Pos)
        return

    def menu_Event_Loop(self, game_State_Flags):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_State_Flags['end_Application']      = True
                game_State_Flags['in_Main_Menu']  = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_State_Flags['in_Main_Menu']  = False
                    game_State_Flags['in_Game_Screen']       = True

                elif event.key == pygame.K_DOWN:
                    CMenu.menu_Cursor_Pos[1] += 100 

                elif event.key == pygame.K_UP:
                    CMenu.menu_Cursor_Pos[1] -= 100

        return