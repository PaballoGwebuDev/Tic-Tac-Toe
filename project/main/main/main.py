
import math
import numpy

#initialize pygame
import pygame as pg
pg.init()

#set screen dimensions
total_screen_height = 650
screen_height = 500
screen_width = 500
num_grid_lines = 3

h_spacing = 0
floor_h_spacing = 0
v_spacing = 0
floor_v_spacing = 0



#Display screen
screen = pg.display.set_mode((screen_width, total_screen_height))
pg.display.set_caption('Tic Tac Toe')

#Variable definitions:
game_board = []

mouse_click = False
mouse_pos = []
player = 1 #designate 1 for player 1 and -1 for player 2
offset = 15

winner = 0
game_over = False
turn_count = 0
button_click = False
ai_oponent = False
ai_game_over = False
ai_turn = False

#Define  colors
p_one_color =  (255,0,0) #red
p_two_color =  (0,0,255) #blue
black = (50,50,50)
white = (255,255,255)
purple = (128,0,128)
rgb = black

#Define fonts
font = pg.font.SysFont('arial',40,True)


#Define functions

#initialise game board array
def populate_game_board(n_grid_lines):
    for rows in range(n_grid_lines):
        row = [0]*n_grid_lines
        game_board.append(row)
               
    #print(game_board)

#populate_game_board(num_grid_lines)


#Draw Grid
def draw_grid(n_grid_lines):
    #grid backround
    global h_spacing
    global floor_h_spacing
    global v_spacing
    global floor_v_spacing

    screen.fill(rgb)
    h_spacing = (screen_height/n_grid_lines)
    floor_h_spacing = math.floor(h_spacing)
    v_spacing = (screen_width/n_grid_lines)
    floor_v_spacing = math.floor(v_spacing)
    #gridlines
    line_width = 7
    line_color = purple

    pg.draw.line(screen,line_color,(0,screen_height),(screen_width,screen_height),line_width)
    for x in range(1,n_grid_lines):
        #Horizontal lines
        pg.draw.line(screen,line_color,(0,x*h_spacing),(screen_width,x*h_spacing),line_width)

        #vertical lines
        pg.draw.line(screen,line_color,(x*v_spacing,0),(x*v_spacing,screen_height),line_width)

 
 #register player clicks and fill game_board
def fill_player_clicks():
    global turn_count
    global winner
    global game_over
    global player
    global ai_turn

    
    mouse_click = False
    mouse_pos = pg.mouse.get_pos()
#make sure game play clicks are only registered in play area

    if mouse_pos[1] <= screen_height and ai_oponent == False:

        cell_x = mouse_pos[1]//floor_h_spacing #column #board flip
        cell_y = mouse_pos[0]//floor_v_spacing #rows #board flip

        if game_board[cell_x][cell_y] == 0:
            game_board[cell_x][cell_y] = player
            turn_count += 1
            player *= -1 
    elif mouse_pos[1] <= screen_height and ai_oponent:
        player = -1
        cell_x = mouse_pos[1]//floor_h_spacing #column #board flip
        cell_y = mouse_pos[0]//floor_v_spacing #rows #board flip

        if game_board[cell_x][cell_y] == 0:
            game_board[cell_x][cell_y] = player
            turn_count += 1
            
     
      

 #Check for draw 1st
    if turn_count == (num_grid_lines*num_grid_lines) and winner == 0:
        winner = 3
        game_over = True
        ai_game_over = True
    else:
        check_winner()
    #print(game_board)
    #draw X and Os in grid
    populate_cells()


#draw X and Os
def populate_cells():
  
    y_pos = 0 #board flip
    for x in game_board:
        x_pos = 0 #board flip
        for y in x:
            if y == 1:
                line_one = [x_pos*h_spacing + offset, y_pos*v_spacing +offset]
                line_two = [x_pos*h_spacing + (h_spacing - offset),y_pos*v_spacing + (v_spacing - offset)]
                pg.draw.line(screen,white,(line_one[0],line_one[1]),(line_two[0],line_two[1]),5)
                pg.draw.line(screen,white,(line_one[0],line_two[1]),(line_two[0],line_one[1]),5)
            if y == -1:
                pg.draw.circle(screen,white,(x_pos*h_spacing + (h_spacing/2),y_pos*v_spacing + (v_spacing/2)),38,5)
            x_pos += 1 #board flip
        y_pos += 1 #board flip

def search_array(game_board):
    global game_over
    global winner
    global num_grid_lines
    for rows in game_board:
        #check rows for winner
        if sum(rows) == num_grid_lines:
            print(sum(rows))
            winner = 1
            game_over = True
            ai_game_over = True
        if sum(rows) == -1 *num_grid_lines:
            winner = 2
            game_over = True
            ai_game_over = True

    #check diagonals for winner
    diagonal = numpy.asarray(game_board)
    if numpy.trace(diagonal) == num_grid_lines:
        winner = 1
        game_over = True
        ai_game_over = True
    if numpy.trace(diagonal) == -1*num_grid_lines:
        winner = 2
        game_over = True
        ai_game_over = True

    anti_diagonal = numpy.fliplr(diagonal)
    if numpy.trace(anti_diagonal) == num_grid_lines:
        winner = 1
        game_over = True
    if numpy.trace(anti_diagonal) == -1*num_grid_lines:
        winner = 2
        game_over = True
        aiai_game_over = True


def check_winner():
    print('min max call')
    #check for winner horizontally
    search_array(game_board)
    #check for winner vertically
    search_array(numpy.transpose(game_board))

#AI Decision tree using the minimax algorithm
def comp_move():

    best_score = -math.inf
    best_move_row = 0
    best_move_col = 0
    global turn_count
    global ai_turn
    #print(game_board)

    for rows in range(num_grid_lines):
        for col in range(num_grid_lines):
            if game_board[rows][col] == 0:
                game_board[rows][col] = 1 #ai goes first
                score = mini_max(game_board,0,False)
                game_board[rows][col] = 0
                if (score > best_score):
                    best_score = score
                    best_move_row = rows
                    best_move_col = col     
    game_board[best_move_row][best_move_col] = 1
    ai_turn = False
    print(game_board)
    populate_cells()
    return
    #ai_turn = False
    #print(game_board)
    #return

def mini_max(game_board,depth,maximizing):
    global winner
    check_winner()
    if winner == 1:
        return 1
    elif winner == 2:
        return -1
    elif winner == 3:
        return 0

    if maximizing:
        best_score = -math.inf
        for rows in range(num_grid_lines):
            for col in range(num_grid_lines):
                if game_board[rows][col] == 0:
                    game_board[rows][col] = 1 #ai goes first
                    score = mini_max(game_board,depth +1,True)
                    game_board[rows][col] = 0
                    if (score > best_score):
                        best_score = score
        return best_score
    else:
        best_score = math.inf
        for rows in range(num_grid_lines):
            for col in range(num_grid_lines):
                if game_board[rows][col] == 0:
                    game_board[rows][col] = -1
                    score = mini_max(game_board,depth +1,False)
                    game_board[rows][col] = 0
                    if (score < best_score):
                        best_score = score
        return best_score


    

def ui_manager(winner):
    if winner == 1 or winner == 2:
        win_text = 'Player ' + str(winner) + " wins!"
    elif winner == 3:
        win_text = "it's a Tie!"
    win_image = font.render(win_text,True,p_two_color)
    screen.blit(win_image,(screen_width//2-100,screen_height+10))


#Define classes
class buttons():

    #define colours for buttons and text
    button_col = (255,255,255)
    hover_col = (218,112,214)
    click_col = (50,150,255)
    text_col = black

    #button dimensions
    width = 180
    height = 50

    #initialize button
    def __init__(self,x,y,text,side):
        self.x = x
        self.y = y
        self.text = text
        self.side = side
  
    #draw button
    def draw_button(self):
        global button_click
        action = False
        pos = pg.mouse.get_pos()

        #create rect that represents button
        button_rect = pg.Rect(self.x, self.y, self.width, self.height)

        #check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1:
                button_click = True
                pg.draw.rect(screen, self.click_col, button_rect)
            elif pg.mouse.get_pressed()[0] == 0 and button_click == True:
                button_click = False
                action = True
            else: 
                pg.draw.rect(screen,self.hover_col,button_rect)
        else:
            pg.draw.rect(screen,self.button_col,button_rect)
    
        #add text to button
        text_image = font.render(self.text, True, self.text_col)
        text_len = text_image.get_width()
        if self.side == 1:
            screen.blit(text_image,(self.x + (self.x/3.5), self.y +2))
        elif self.side == 3:
            screen.blit(text_image,(self.x + (self.x/13.5), self.y +2))
        else:
            screen.blit(text_image,(self.x, self.y))

        
        #screen.blit(text_image,(self.x + int(self.width/2) - int(text_len/2), self.y +5))
        return action

class GameState():
    def __init__(self):
        self.state = 'intro'

    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'main_game':
            self.main_game()
        if self.state == 'ai_scene':
            self.ai_scene()

        


    def intro(self):
        global game_over
        global mouse_click
        global winner
        global game_board
        global player
        global mouse_pos
        global turn_count
        global running
        global num_grid_lines
        global ai_oponent
        global ai_turn

        game_board = []
        turn_count = 0
        game_over = False
        player = 1
        mouse_pos = (0,0)
        winner = 0


        screen.fill(rgb)
        
        # inatantiate intro screen ui objects
        intro_rect = pg.Rect(0,0,screen_width//2,total_screen_height)
        pg.draw.rect(screen,(218,112,214),intro_rect)

        intro_rect_t = pg.Rect(screen_width//2,0,screen_width//2,total_screen_height)
        pg.draw.rect(screen,(72,61,139),intro_rect_t)

        human_image = font.render('VS Human',True,(255,255,255))
        screen.blit(human_image,(10, 30))

        ai_image = font.render('VS AI',True,(255,255,255))
        screen.blit(ai_image,(screen_width//2 + 10, 30))
        

        human_player = buttons(10,100, 'Classic',1)
        human_player.draw_button()

        human_player_t = buttons(10,200, 'Challenge',1)
        human_player_t.draw_button()


        ai_player = buttons(screen_width//2 + 10,400, 'Classic',3)
        ai_player.draw_button()

        ai_player_t = buttons(screen_width//2 + 10,500, 'Challenge',3)
        ai_player_t.draw_button()

        #human_player = buttons(screen_width//2 -100,total_screen_height + 95, 'AI',2)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if human_player.draw_button():
                self.state = 'main_game'
                screen.fill(rgb)
                num_grid_lines = 3
                draw_grid(num_grid_lines)
                populate_game_board(num_grid_lines)

            elif human_player_t.draw_button():
                self.state = 'main_game'
                num_grid_lines = 5
                draw_grid(num_grid_lines)
                populate_game_board(num_grid_lines)
            elif ai_player.draw_button():
                self.state = 'ai_scene'
                ai_oponent = True
                print('intro click sets ai turn to:')
                ai_turn = True
                print(ai_turn)
                turn_count = 1
                screen.fill(rgb)
                draw_grid(num_grid_lines)
                populate_game_board(num_grid_lines)
        pg.display.update()


    def ai_scene(self):
        global ai_game_over
        global mouse_click
        global winner
        global game_board
        global player
        global mouse_pos
        global turn_count
        global running
        global ai_turn
        #ai_mouse_click = False
        
        if ai_turn:
            comp_move()
        else:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if ai_game_over == False:
                    if event.type == pg.MOUSEBUTTONDOWN and mouse_click == False:
                        mouse_click = True
                    if event.type == pg.MOUSEBUTTONUP and mouse_click == True:
                        fill_player_clicks()
                        ai_turn = True
      
        


    def main_game(self):
        global game_over
        global mouse_click
        global winner
        global game_board
        global player
        global mouse_pos
        global turn_count
        global running
        #populate_game_board(num_grid_lines)
        #draw_grid(num_grid_lines)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if game_over == False:
                    if event.type == pg.MOUSEBUTTONDOWN and mouse_click == False:
                        mouse_click = True
                    if event.type == pg.MOUSEBUTTONUP and mouse_click == True:
                        fill_player_clicks()

        #after a game ends
        if game_over == True:
            #announce winner
            ui_manager(winner)
            # call buttons
            instant_replay = buttons((1/10)*screen_width,total_screen_height - 85, 'Replay',1)
            main_menu = buttons((5.5/10)*screen_width,total_screen_height - 85, 'Menu',3)

            #button event handlers
            if instant_replay.draw_button():
                game_board = []
                turn_count = 0
                game_over = False
                player = 1
                mouse_pos = (0,0)
                winner = 0
                populate_game_board(num_grid_lines)
                screen.fill(rgb)
                draw_grid(num_grid_lines)
            elif main_menu.draw_button():
                self.state = 'intro'
                          






populate_game_board(num_grid_lines)
#Game loop
game_state = GameState()
running = True


while running:
    game_state.state_manager()    
    pg.display.update()
pg.quit()
   


