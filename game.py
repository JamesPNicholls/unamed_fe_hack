from numpy import size, multiply
import pygame as p
import map
import unit

class Cgame:
    #mask used for color_key transparency
    cursor_mask = (156, 39, 176)
    frame_count = 0
    grid_size = 55
        
    def __init__(self,screen):
        self.current_Level = 1
        self.screen = screen

        self.game_Map = p.image.load('sprites/map/map_Demo.png').convert()
        self.game_Map = p.transform.scale(self.game_Map, (int(3.5*240),int(3.5*336)))    
        self.game_Map_Pos = [0,0]
        self.game_Map_Grid = map.Cmap()


        self.game_Icon = [p.image.load('sprites/map/map_cursor_0.png').convert(), p.image.load('sprites/map/map_cursor_1.png').convert(), p.image.load('sprites/map/map_cursor_2.png').convert()]
        for i in range(size(self.game_Icon)):
            self.game_Icon[i] = p.transform.scale(self.game_Icon[i], (int(3.6*20), int(3.6*20)))
            self.game_Icon[i].set_colorkey(self.cursor_mask)
        self.game_Icon_Pos = [0,0]

        # dict containing the individual unit objects, uses the unit_name class to pass unit_ID
        # allied unit start_pos arguemnt are set to false because their start postion is found in
        # in base_stats.json

        #__init__(self, unit_id, start_pos )
        self.allies = {     'u_roy'     : unit.Cunit(unit.unit_id_val['Roy'],       False),
                            'u_marcus'  : unit.Cunit(unit.unit_id_val['Marcus'],    False),
                            'u_alan'    : unit.Cunit(unit.unit_id_val['Alen'],      False),
                            'u_lance'   : unit.Cunit(unit.unit_id_val['Lance'],     False),
                            'u_wolt'    : unit.Cunit(unit.unit_id_val['Wolt'],      False),
                            'u_bors'    : unit.Cunit(unit.unit_id_val['Bors'],      False)}
        #__init__(self, unit_id, start_pos )
        self.enemies = {    'u_damas'       : unit.Cunit(unit.unit_id_val['Damas'],     [5,5]),
                            'u_brigand_0'   : unit.Cunit(unit.unit_id_val['Brigand'],   [1,1]),
                            'u_archer_0'    : unit.Cunit(unit.unit_id_val['Archer'],    [1,1]),
                            'u_archer_1'    : unit.Cunit(unit.unit_id_val['Archer'],    [1,1]),
                            'u_bandit_0'    : unit.Cunit(unit.unit_id_val['Fighter'],   [1,1]),
                            'u_bandit_1'    : unit.Cunit(unit.unit_id_val['Fighter'],   [1,1]),
                            'u_bandit_2'    : unit.Cunit(unit.unit_id_val['Fighter'],   [1,1]),
                            'u_bandit_3'    : unit.Cunit(unit.unit_id_val['Fighter'],   [1,1]),
                            'u_bandit_4'    : unit.Cunit(unit.unit_id_val['Fighter'],   [1,1]),
                            'u_bandit_5'    : unit.Cunit(unit.unit_id_val['Fighter'],   [1,1]),
                            'u_bandit_6'    : unit.Cunit(unit.unit_id_val['Fighter'],   [1,1]),
                            'u_bandit_7'    : unit.Cunit(unit.unit_id_val['Fighter'],   [1,1]),
                            'u_bandit_8'    : unit.Cunit(unit.unit_id_val['Fighter'],   [1,1]),
                            'u_bandit_9'    : unit.Cunit(unit.unit_id_val['Fighter'],   [1,1])}


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
                    
                    if self.game_Icon_Pos[1] < 9:
                        self.game_Icon_Pos[1] += 1
                    
                    # Checks to see if the cursor is at the edge of visible screen to scroll the map
                    # One of these for each direction
                    if self.game_Icon_Pos[1] == 9 and self.game_Map_Pos[1] > -11:
                        self.game_Map_Pos[1] -= 1

                if event.key == p.K_UP:
                    # move cursor up unless at top of screen
                    if self.game_Icon_Pos[1] > 0:
                        self.game_Icon_Pos[1] -= 1

                    if self.game_Icon_Pos[1] == 0 and self.game_Map_Pos[1] < 0:
                        self.game_Map_Pos[1] += 1
                    
                if event.key == p.K_LEFT:
                    if self.game_Icon_Pos[0] > 0 :
                        self.game_Icon_Pos[0] -= 1

                if event.key == p.K_RIGHT:
                    if self.game_Icon_Pos[0] <= 13:    
                        self.game_Icon_Pos[0] += 1
                    
                if event.key == p.K_ESCAPE:
                    game_State_Flags['in_Game_Screen'] = False
                    game_State_Flags['in_Main_Menu'] = True

        # print('Icon Pos: ', self.game_Icon_Pos, 'Map Pos: ', self.game_Map_Pos) # debug print
        return
    def get_cursor_pos(self):
        return self.game_Icon_Pos


    def draw_Game(self, *args):  
        # Draw Images on screen
        self.screen.blit( self.game_Map, multiply(self.game_Map_Pos, self.grid_size))
        self.screen.blit( self.game_Icon[1], multiply(self.game_Icon_Pos,self.grid_size))
        
        my_font = p.font.SysFont('Times New Roman', 50)
        defn = self.game_Map_Grid.map_grid[self.game_Icon_Pos[0]][self.game_Icon_Pos[0]].bonus_def
        avod = self.game_Map_Grid.map_grid[self.game_Icon_Pos[0]][self.game_Icon_Pos[0]].bonus_avd
        defn = my_font.render(defn, False, (0xff,0xff,0xff))
        avod = my_font.render(avod, False, (0xff,0xff,0xff))

        self.screen.blit( defn, (10,10))
        self.screen.blit( avod, [20,20])
        return

