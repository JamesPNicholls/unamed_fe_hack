import pygame
import sys
from menu import CMenu
from game import Cgame
class Cmain():
    
    def __init__(self) -> None:
        # Enabling pygame  
        pygame.init()

        Cmain.screen = pygame.display.set_mode((671+55*3,564))
        Cmain.clock = pygame.time.Clock()
        Cmain.game_State_Flags = {    'in_Main_Menu'          :  True,
                                      'in_Game_Screen_Screen' : False,
                                      'end_Application'       : False}

        #  Instanitating the 'subclasses'
        Cmain.C_Game = Cgame(Cmain.screen)
        Cmain.C_Menu = CMenu(Cmain.screen)

    
    def update():
            pygame.display.update()
            Cmain.clock.tick(32)

    def main(self):
        # Contains all the primary game loops

        while(not Cmain.game_State_Flags['end_Application']):
            while Cmain.game_State_Flags['in_Main_Menu']:
                Cmain.C_Menu.menu_Event_Loop(Cmain.game_State_Flags)
                Cmain.C_Menu.draw_Menu()
                Cmain.update()

            while Cmain.game_State_Flags['in_Game_Screen']:
                Cmain.C_Game.game_Event_Loop(Cmain.game_State_Flags)
                Cmain.C_Game.draw_Game()
                Cmain.update()

        pygame.quit()
        sys.exit()

C_Main = Cmain()
C_Main.main()
