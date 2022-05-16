from numpy import size, multiply
import pygame as p
import map
import unit

class Cgame:
    #mask used for color_key transparency
    cursor_mask = (156, 39, 176)
    frame_count = 0

    #pixel granularity for the map grid


    # starting postion for enemy units
    enemy_start_pos = { 'u_damas'       : (5,4),
                        'u_brigand_0'   : (7,10),
                        'u_archer_0'    : (2,2),
                        'u_archer_1'    : (8,13),
                        'u_bandit_0'    : (1,3),
                        'u_bandit_1'    : (4,5),
                        'u_bandit_2'    : (6,5),
                        'u_bandit_3'    : (11,7),
                        'u_bandit_4'    : (8,9),
                        'u_bandit_5'    : (9,9),
                        'u_bandit_6'    : (12,13),
                        'u_bandit_7'    : (8,14),
                        'u_bandit_8'    : (7,15),
                        'u_bandit_9'    : (8,18)}
        
    def __init__(self,screen):
        self.current_Level = 1
        self.screen = screen

        # Terrain Display Screen
        self.terrain_disp = p.image.load('sprites/map/terrain_disp.png').convert()
        self.terrain_disp = p.transform.scale(self.terrain_disp, (210,210))
        self.terrain_disp.set_colorkey(self.cursor_mask)
        self.terrain_disp_pos = [11.8, 6.9]

        self.terrain_defn_text_pos = [14, 8.8]
        self.terrain_avod_text_pos = [14, 9.3]
        self.terrain_name_text_pos = [13, 7.9]



        # map object populated with sqaure objects to store the tile data
        self.game_map = map.Cmap()

        # Cursor images
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
        self.enemies = {    'u_damas'       : unit.Cunit(unit.unit_id_val['Damas'],     self.enemy_start_pos['u_damas']),
                            'u_brigand_0'   : unit.Cunit(unit.unit_id_val['Brigand'],   self.enemy_start_pos['u_brigand_0']),
                            'u_archer_0'    : unit.Cunit(unit.unit_id_val['Archer'],    self.enemy_start_pos['u_archer_0']),
                            'u_archer_1'    : unit.Cunit(unit.unit_id_val['Archer'],    self.enemy_start_pos['u_archer_1']),
                            'u_bandit_0'    : unit.Cunit(unit.unit_id_val['Fighter'],   self.enemy_start_pos['u_bandit_0']),
                            'u_bandit_1'    : unit.Cunit(unit.unit_id_val['Fighter'],   self.enemy_start_pos['u_bandit_1']),
                            'u_bandit_2'    : unit.Cunit(unit.unit_id_val['Fighter'],   self.enemy_start_pos['u_bandit_2']),
                            'u_bandit_3'    : unit.Cunit(unit.unit_id_val['Fighter'],   self.enemy_start_pos['u_bandit_3']),
                            'u_bandit_4'    : unit.Cunit(unit.unit_id_val['Fighter'],   self.enemy_start_pos['u_bandit_4']),
                            'u_bandit_5'    : unit.Cunit(unit.unit_id_val['Fighter'],   self.enemy_start_pos['u_bandit_5']),
                            'u_bandit_6'    : unit.Cunit(unit.unit_id_val['Fighter'],   self.enemy_start_pos['u_bandit_6']),
                            'u_bandit_7'    : unit.Cunit(unit.unit_id_val['Fighter'],   self.enemy_start_pos['u_bandit_7']),
                            'u_bandit_8'    : unit.Cunit(unit.unit_id_val['Fighter'],   self.enemy_start_pos['u_bandit_8']),
                            'u_bandit_9'    : unit.Cunit(unit.unit_id_val['Fighter'],   self.enemy_start_pos['u_bandit_9'])}

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
                        self.game_map.update_map_pos('down') 
                        # Need two calls of this for the screen scrolling
                        # No need for the left and right inputs
                    
                    # Checks to see if the cursor is at the edge of visible screen to scroll the map
                    # One of these for up and down
                    if self.game_Icon_Pos[1] == 9 and self.game_map.game_Map_Pos[1] > -11:
                        self.game_map.update_map_pos('down')
                        self.game_map.game_Map_Pos[1] -= 1

                if event.key == p.K_UP:
                    
                    # move cursor up unless at top of screen
                    if self.game_Icon_Pos[1] > 0:
                        self.game_Icon_Pos[1] -= 1
                        self.game_map.update_map_pos('up')

                    if self.game_Icon_Pos[1] == 0 and self.game_map.game_Map_Pos[1] < 0:
                        self.game_map.game_Map_Pos[1] += 1
                        self.game_map.update_map_pos('up')
                    
                if event.key == p.K_LEFT:
                    self.game_map.update_map_pos('left')
                    if self.game_Icon_Pos[0] > 0 :
                        self.game_Icon_Pos[0] -= 1

                if event.key == p.K_RIGHT:
                    self.game_map.update_map_pos('right')
                    if self.game_Icon_Pos[0] <= 13:    
                        self.game_Icon_Pos[0] += 1
                    
                if event.key == p.K_ESCAPE:
                    game_State_Flags['in_Game_Screen'] = False
                    game_State_Flags['in_Main_Menu'] = True

        # print('Icon Pos: ', self.game_Icon_Pos, 'Map Pos: ', self.game_Map_Pos) # debug print
        return
    def get_cursor_pos(self):
        return self.game_Icon_Pos

    def draw_terrain_disp(self):
        # font
        my_font = p.font.SysFont('Times New Roman', 30)
        

        # gets the data to be printed
        avod = self.game_map.map_grid[self.game_map.map_pos[1]][self.game_map.map_pos[0]].bonus_avd
        defn = self.game_map.map_grid[self.game_map.map_pos[1]][self.game_map.map_pos[0]].bonus_def
        name = self.game_map.map_grid[self.game_map.map_pos[1]][self.game_map.map_pos[0]].name
        # debug print
        print('x: ',self.game_map.map_pos[0],' y: ',self.game_map.map_pos[1], ' def: ', defn, ', avd: ', avod, )
       
        # renders the text to be printed
        defn = my_font.render(str(defn), False, (0xf,0xf,0xf))
        avod = my_font.render(str(avod), False, (0xf,0xf,0xf))
        name = my_font.render(name, False, (0x0, 0x0, 0x0))

        # change position of terrain disp to prevent blocking the cursor cursor
        # if self.game_Icon_Pos[0] > map.x_size/2 :
        #     self.terrain_disp_pos[0] = 50
        # else
        #     self.terrain_disp

        # prints images and text
        self.screen.blit(self.terrain_disp, multiply(self.terrain_disp_pos, self.game_map.grid_size))
        self.screen.blit( defn, (770,483))
        self.screen.blit( avod, (770,515))
        self.screen.blit( name, (715,435))
        

    def draw_Game(self, *args):  
        # Draw Images on screen
        # Map
        self.screen.blit( self.game_map.game_Map, multiply(self.game_map.game_Map_Pos, self.game_map.grid_size))

        # Icon
        self.screen.blit( self.game_Icon[1], multiply(self.game_Icon_Pos, self.game_map.grid_size))

        #terrain data
        self.draw_terrain_disp()
        return

 