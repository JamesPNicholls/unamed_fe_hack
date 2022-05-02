import pygame as p
class Cmenu:

    def __init__(self, screen) -> None:   
        p.font.init()     
        self.screen = screen
        self.my_font = p.font.SysFont('Times New Roman', 50)
        self.debug_Options = [  self.my_font.render('1: Map Test', False, (0xff,0xff,0xff)),
                                self.my_font.render('2: Stat Screen Test', False, (0xff,0xff,0xff)),
                                self.my_font.render('3: Combat Test', False, (0xff,0xff,0xff)),
                                self.my_font.render('4: Menu Test', False, (0xff,0xff,0xff)),
                                self.my_font.render('5: AI Test', False, (0xff,0xff,0xff)),
                                self.my_font.render('6: Test', False, (0xff,0xff,0xff))]

        self.menu_Cursor_Pos = [0,100]

        self.menu_Surface   = p.image.load('sprites/misc/menu.png').convert()
        self.menu_Surface   = p.transform.scale(self.menu_Surface, (836,564))
        self.menu_Cursor    = p.image.load('sprites/misc/menu_Pointer.png')

        self.top_Button     = p.image.load('sprites/misc/button_00.png')
        self.bot_Button     = p.image.load('sprites/misc/button_00.png')

        self.top_Button     = p.transform.scale(self.top_Button, [700,250])
        self.bot_Button     = p.transform.scale(self.bot_Button, [700,250])
        return

    def draw_Menu(self, *args):
        self.screen.blit(self.menu_Surface,(0,0))
        for i in range(0,5):
            self.screen.blit(self.debug_Options[i], (200,100+60*i))

       # self.screen.blit(self.top_Button,(10,10))
       # self.screen.blit(self.bot_Button,(10,200))

        self.screen.blit(self.menu_Cursor, self.menu_Cursor_Pos)
        return

    def key_press_handler():
        return

    def menu_Event_Loop(self, game_State_Flags):
        for event in p.event.get():
            if event.type == p.QUIT:
                game_State_Flags['end_Application']      = True
                game_State_Flags['in_Main_Menu']  = False

            if event.type == p.KEYDOWN:
                if event.key == p.K_1:
                    game_State_Flags['in_Main_Menu']  = False
                    game_State_Flags['in_Game_Screen']       = True

                elif event.key == p.K_DOWN:
                    self.menu_Cursor_Pos[1] += 100 

                elif event.key == p.K_UP:
                    self.menu_Cursor_Pos[1] -= 100

        return