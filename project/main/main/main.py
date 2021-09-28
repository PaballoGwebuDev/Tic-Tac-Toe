
import math
#initialize pygame
import pygame as pg
pg.init()

#set screen dimensions in pixels
screen_height = 600
screen_width = 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Tic Tac Toe')

#Variable definitions:
game_board = []
num_grid_lines = 3
mouse_click = False
mouse_pos = []
h_spacing = (screen_height/num_grid_lines)
floor_h_spacing = math.floor(h_spacing)
v_spacing = (screen_width/num_grid_lines)
floor_v_spacing = math.floor(v_spacing)
player = 1 #designate 1 for player 1 and -1 for player 2
offset = 15

for rows in range(num_grid_lines):
    row = [0]*num_grid_lines
    game_board.append(row)
print(game_board)
    

#Draw Grid
def draw_grid(n_grid_lines):
    #grid backround
    rgb = (255,255,255)
    screen.fill(rgb)

    #gridlines
    line_width = 10
    line_color = (50,50,50)



    for x in range(1,n_grid_lines):
        #Horizontal lines
        pg.draw.line(screen,line_color,(0,x*h_spacing),(screen_width,x*h_spacing),line_width)

        #vertical lines
        pg.draw.line(screen,line_color,(x*v_spacing,0),(x*v_spacing,screen_height),line_width)
        
def fill_player_clicks():
            mouse_click = False
            mouse_pos = pg.mouse.get_pos()
            cell_x = mouse_pos[0]//floor_h_spacing #column
            cell_y = mouse_pos[1]//floor_v_spacing #rows
            if game_board[cell_x][cell_y] == 0:
                global player
                game_board[cell_x][cell_y] = player
                player *= -1 

def populate_cells():
    global line_width
    p_one_color =  (255,0,0) #red
    p_two_color =  (0,0,255) #blue

    x_pos = 0
    for x in game_board:
        y_pos = 0
        for y in x:
            if y == 1:
                line_one = [x_pos*h_spacing + offset, y_pos*v_spacing +offset]
                line_two = [x_pos*h_spacing + (h_spacing - offset),y_pos*v_spacing + (v_spacing - offset)]
                pg.draw.line(screen,p_one_color,(line_one[0],line_one[1]),(line_two[0],line_two[1]),5)
                pg.draw.line(screen,p_one_color,(line_one[0],line_two[1]),(line_two[0],line_one[1]),5)
            if y == -1:
                pg.draw.circle(screen,p_two_color,(x_pos*h_spacing + (h_spacing/2),y_pos*v_spacing + (v_spacing/2)),38,5)
            y_pos += 1
        x_pos += 1


              



 
draw_grid(num_grid_lines)
#Game loop

running = True

while running:
    # event handlers
    #draw_grid(num_grid_lines)
    populate_cells()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN and mouse_click == False:
            mouse_click = True
        if event.type == pg.MOUSEBUTTONUP and mouse_click == True:
            fill_player_clicks()
                                 
    pg.display.update()
print(game_board)
pg.quit()
   


