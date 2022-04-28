import pygame as p
class CGame:
    #mask used for color_key transparency
    cursor_mask = (34, 177, 76)

    def __init__(self,screen):
        self.current_Level = 1
        self.screen = screen

        self.game_Map = p.image.load('sprites/map/map_Demo.png').convert()
        self.game_Map = p.transform.scale(self.game_Map, (int(3.6*240),int(3.6*336)))    
        self.game_Map_Pos = [0,0]

        self.game_Icon = p.image.load('sprites/map/map_cursor_1.png').convert()
        self.game_Icon = p.transform.scale(self.game_Icon, (int(3.6*20), int(3.6*20)))
        self.game_Icon.set_colorkey(self.cursor_mask)
        self.game_Icon_Pos = [50,50]
        return

    def game_Event_Loop(self, game_State_Flags):
        key = p.key.get_pressed()
        # Update Cursor Position
        

        # Update Screen Position 
        if key[p.K_ESCAPE]:
            game_State_Flags['in_Game_Screen']   = False
            game_State_Flags['in_Main_Menu']     = True
        if key[p.K_DOWN]:
            print('Icon Pos: ', self.game_Icon_Pos, 'Map Pos: ', self.game_Map_Pos)
            if self.game_Icon_Pos[1] <= 510:
                self.game_Icon_Pos[1] += 10
            
            if self.game_Icon_Pos[1] == 520 and self.game_Map_Pos[1] > -620:
                self.game_Map_Pos[1] -= 10

        if key[p.K_UP]:
            print('Icon Pos: ', self.game_Icon_Pos, 'Map Pos: ', self.game_Map_Pos)
            # move cursor up unless at top of screen
            if self.game_Icon_Pos[1] > -1:
                self.game_Icon_Pos[1] -= 10

            if self.game_Icon_Pos[1] == -10 and self.game_Map_Pos[1] < 0:
                self.game_Map_Pos[1] += 10
            

        if key[p.K_LEFT]:   
            print('Icon Pos: ', self.game_Icon_Pos, 'Map Pos: ', self.game_Map_Pos)
            if self.game_Icon_Pos[0] > 0 :
                self.game_Icon_Pos[0] -= 10

            if self.game_Icon_Pos[0] == 0 and self.game_Map_Pos[0] < 0:
                self.game_Map_Pos[0] += 10

        if key[p.K_RIGHT]:  
            print('Icon Pos: ', self.game_Icon_Pos, 'Map Pos: ', self.game_Map_Pos)
            if self.game_Icon_Pos[0] <= 590:    
                self.game_Icon_Pos[0] += 10
            
            if self.game_Icon_Pos[0] == 600 and self.game_Map_Pos[0] > -190:
                self.game_Map_Pos[0] -= 10
        




        for event in p.event.get():
            if event.type == p.QUIT:
                game_State_Flags['end_Application'] = True
                game_State_Flags['in_Game_Screen']  = False
                break
        return

    def draw_Game(self, *args):  
        # Draw Images on screen
        self.screen.blit( self.game_Map, self.game_Map_Pos)
        self.screen.blit( self.game_Icon, self.game_Icon_Pos)
        return
    
        