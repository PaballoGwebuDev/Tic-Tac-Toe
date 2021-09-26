#initialize pygame
import pygame as pg
pg.init()

#set screen dimensions in pixels
screen_height = 700
screen_width = 700

screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Tic Tac Toe')

#Variable definitions:
game_board = []
num_grid_lines = 3

for rows in range(num_grid_lines):
    row = [0]*num_grid_lines
    game_board.append(row)

    
#print(game_board)

def draw_grid(n_grid_lines):
    #grid backround
    rgb = (255,255,200)
    screen.fill(rgb)

    #gridlines
    h_grid_line_spacing = (screen_height/n_grid_lines)
    v_grid_line_spacing = (screen_width/n_grid_lines)
    line_width = 10
    line_color = (50,50,50)

    for x in range(1,n_grid_lines):
        #Horizontal lines
        pg.draw.line(screen,line_color,(0,x*h_grid_line_spacing),(screen_width,x*h_grid_line_spacing),line_width)
        #vertical lines
        pg.draw.line(screen,line_color,(x*v_grid_line_spacing,0),(x*v_grid_line_spacing,screen_height),line_width)
        



#Game loop
running = True

while running:
    # event handlers
    draw_grid(num_grid_lines)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.update()

pg.quit()
   


