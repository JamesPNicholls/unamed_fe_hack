from numpy import size
import pygame as p
class Cgame:
    #mask used for color_key transparency
    cursor_mask = (156, 39, 176)
    frame_count = 0
        
    def __init__(self,screen):
        self.current_Level = 1
        self.screen = screen

        self.game_Map = p.image.load('sprites/map/map_Demo.png').convert()
        self.game_Map = p.transform.scale(self.game_Map, (int(3.5*240),int(3.5*336)))    
        self.game_Map_Pos = [0,0]

        self.game_Icon = [p.image.load('sprites/map/map_cursor_0.png').convert(), p.image.load('sprites/map/map_cursor_1.png').convert(), p.image.load('sprites/map/map_cursor_2.png').convert()]
        for i in range(size(self.game_Icon)):
            self.game_Icon[i] = p.transform.scale(self.game_Icon[i], (int(3.6*20), int(3.6*20)))
            self.game_Icon[i].set_colorkey(self.cursor_mask)
        self.game_Icon_Pos = [0,0]
        return

    def game_Event_Loop(self, game_State_Flags):
        p.key.set_repeat(50)

        for event in p.event.get():
            # Check for quit flag
            if event.type == p.QUIT:
                game_State_Flags['end_Application'] = True
                game_State_Flags['in_Game_Screen']  = False
                break
        
            # Update Cursor Position based on Button Press   
            if event.type == p.KEYDOWN:
                if event.key == p.K_DOWN:
                    
                    if self.game_Icon_Pos[1] < 495:
                        self.game_Icon_Pos[1] += 55
                    
                    # Checks to see if the cursor is at the edge of visible screen to scroll the map
                    # One of these for each direction
                    if self.game_Icon_Pos[1] == 495 and self.game_Map_Pos[1] > -551:
                        self.game_Map_Pos[1] -= 55

                if event.key == p.K_UP:
                    # move cursor up unless at top of screen
                    if self.game_Icon_Pos[1] > 0:
                        self.game_Icon_Pos[1] -= 55

                    if self.game_Icon_Pos[1] == 0 and self.game_Map_Pos[1] < 0:
                        self.game_Map_Pos[1] += 55
                    

                if event.key == p.K_LEFT:   

                    if self.game_Icon_Pos[0] > 0 :
                        self.game_Icon_Pos[0] -= 55



                if event.key == p.K_RIGHT:
                    if self.game_Icon_Pos[0] <= 550+55*3:    
                        self.game_Icon_Pos[0] += 55
                    

        print('Icon Pos: ', self.game_Icon_Pos, 'Map Pos: ', self.game_Map_Pos) # debug print
        return

    def draw_Cursor():
        # want to add the pulsing icon here 
        return 


    def draw_Game(self, *args):  
        # Draw Images on screen
        self.screen.blit( self.game_Map, self.game_Map_Pos)
        self.screen.blit( self.game_Icon[1], self.game_Icon_Pos)
        
        return
        