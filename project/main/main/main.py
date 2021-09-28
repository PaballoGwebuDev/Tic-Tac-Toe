
import math
import numpy

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

winner = 0
game_over = False
turn_count = 0

for rows in range(num_grid_lines):
    row = [0]*num_grid_lines
    game_board.append(row)

    

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
    global turn_count
    global winner
    global game_over

    
    mouse_click = False
    mouse_pos = pg.mouse.get_pos()
    cell_x = mouse_pos[1]//floor_h_spacing #column #board flip
    cell_y = mouse_pos[0]//floor_v_spacing #rows #board flip
    if game_board[cell_x][cell_y] == 0:
        global player
        game_board[cell_x][cell_y] = player
        turn_count += 1
        player *= -1 
 #Check for draw 1st
    if turn_count == (num_grid_lines*num_grid_lines) and winner == 0:
        winner = 3
        game_over = True
        print(game_over)
        print(winner)

    else:
        check_winner()
    populate_cells()
    print(game_over)
    print(winner)


def populate_cells():
    global line_width
    p_one_color =  (255,0,0) #red
    p_two_color =  (0,0,255) #blue

    y_pos = 0 #board flip
    for x in game_board:
        x_pos = 0 #board flip
        for y in x:
            if y == 1:
                line_one = [x_pos*h_spacing + offset, y_pos*v_spacing +offset]
                line_two = [x_pos*h_spacing + (h_spacing - offset),y_pos*v_spacing + (v_spacing - offset)]
                pg.draw.line(screen,p_one_color,(line_one[0],line_one[1]),(line_two[0],line_two[1]),5)
                pg.draw.line(screen,p_one_color,(line_one[0],line_two[1]),(line_two[0],line_one[1]),5)
            if y == -1:
                pg.draw.circle(screen,p_two_color,(x_pos*h_spacing + (h_spacing/2),y_pos*v_spacing + (v_spacing/2)),38,5)
            x_pos += 1 #board flip
        y_pos += 1 #board flip

def search_array(game_board):
    global game_over
    global winner
    for rows in game_board:
        #check rows for winner
        if sum(rows) == num_grid_lines:
            winner = 1
            game_over = True
        if sum(rows) == -1 *num_grid_lines:
            winner = 2
            game_over = True
    #check diagonals for winner
    diagonal = numpy.asarray(game_board)
    if numpy.trace(diagonal) == num_grid_lines:
        winner = 1
        game_over = True
    if numpy.trace(diagonal) == -1*num_grid_lines:
        winner = 2
        game_over = True
    anti_diagonal = numpy.fliplr(diagonal)
    if numpy.trace(anti_diagonal) == num_grid_lines:
        winner = 1
        game_over = True
    if numpy.trace(anti_diagonal) == -1*num_grid_lines:
        winner = 2
        game_over = True
    #print(game_over)
    #print(winner)



def check_winner():
    #global game_over
    #global winner
    
    #check for winner horizontally
    search_array(game_board)
    #check for winner vertically
    search_array(numpy.transpose(game_board))




draw_grid(num_grid_lines)
#Game loop

running = True

while running:
    # event handlers

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if game_over == False:
                if event.type == pg.MOUSEBUTTONDOWN and mouse_click == False:
                    mouse_click = True
                if event.type == pg.MOUSEBUTTONUP and mouse_click == True:
                    fill_player_clicks()




                                 
    pg.display.update()


pg.quit()
   


