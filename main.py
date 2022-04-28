import pygame
import sys

from pygame.constants import K_LEFT

from menu import CMenu
from game import CGame
class CMain():
    
    def __init__(self) -> None:
        # Enabling pygame  
        pygame.init()

        CMain.screen = pygame.display.set_mode((671,590))
        CMain.clock = pygame.time.Clock()
        CMain.game_State_Flags = {    'in_Main_Menu'          :  True,
                                      'in_Game_Screen_Screen' : False,
                                      'end_Application'       : False}

        #  Instanitating the 'subclasses'
        CMain.C_Game = CGame(CMain.screen)
        CMain.C_Menu = CMenu(CMain.screen)

    
    def update():
            pygame.display.update()
            CMain.clock.tick(60)

    def main(self):
        # Contains all the primary game loops

        while(not CMain.game_State_Flags['end_Application']):
            while CMain.game_State_Flags['in_Main_Menu']:
                CMain.C_Menu.menu_Event_Loop(CMain.game_State_Flags)
                CMain.C_Menu.draw_Menu()
                CMain.update()

            while CMain.game_State_Flags['in_Game_Screen']:
                CMain.C_Game.game_Event_Loop(CMain.game_State_Flags)
                CMain.C_Game.draw_Game()
                CMain.update()

        pygame.quit()
        sys.exit()

C_Main = CMain()
C_Main.main()
