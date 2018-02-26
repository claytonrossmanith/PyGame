from tkinter import*
import table, ball, bat

x_velocity = 10
y_velocity = 0
score_left = 0
score_right = 0
first_serve = True

window = Tk()
window.title("MyPong")

my_table = table.Table(window)

my_ball = ball.Ball(table = my_table, x_speed = x_velocity, y_speed = y_velocity,
                    width = 45, height = 45, color = "yellow", x_start = 500, y_start = 955)

bat_L = bat.Bat(table = my_table, width = 250, height = 68, x_posn = 3, y_posn = 150, color = "yellow")
bat_R = bat.Bat(table = my_table, width = 250, height = 68, x_posn = 750, y_posn = 450, color = "yellow")

self.ballposition=[0,0]
self.ballposition[0]=self.ballstart[0]
self.ballposition[0]=self.ballstart[1]

def game_flow():
    global first_serve
    global score_left
    global score_right

    if(first_serve == True):
        my_ball.stop_ball()
        first_serve = False
    bat_L.detect_collision(my_ball)
    bat_R.detect_collision(my_ball)

 

    if(my_ball.x_posn <= 3):
        my_ball.stop_ball()
        my_ball.start_position()
        bat_L.start_position()
        bat_R.start_position()
        my_table.move_item(bat_L.rectangle, 20, 150, 35, 250)
        my_table.move_item(bat_R.rectangle, 575, 150, 590, 250)
        score_left = score_left + 1
        if(score_left >= 10):
            score_left = "W"
            score_right = "L"
        first_serve = True
        my_table.draw_score(score_left, score_right)
    if(my_ball.x_posn + my_ball.width >= my_table.width - 3):
        my_ball.stop_ball()
        my_ball.start_position()
        bat_L.start_position()
        bat_R.start_position()
        my_table.move_item(bat_L.rectangle, 20, 150, 35, 250)
        my_table.move_item(bat_R.rectangle, 575, 150, 590, 250)
        score_right = score_right + 1
        if(score_right >= 10):
            score_right = "W"
            score_left = "L"
        first_serve = True
        my_table.draw_score(score_left, score_right)

    my_ball.move_next()
    window.after(50, game_flow)
    
 def move_ball(self, d):
    x = self.frogposition[0]
    y = self.frogposition[1]
  if(d == 'Up'):
   y -= 1
  elif(d == 'Down'):
   y += 1
  elif(d == 'Left'):
   x -= 1
  else:
   x += 1
  if(x >= 0 and y >= 0 and x < self.width and y < self.height):
   self.frogposition[0] = x
   self.frogposition[1] = y
   self.movedup = False
   if(d == 'Up' and y < self.highest):
    self.movedup = True
    
def restart_game(master):
        global score_left
        global score_right

        my_ball.start_ball(x_speed = x_velocity, y_speed = 0)
        if(score_left == "W" or score_left == "L"):
            score_left = 0
            score_right = 0
        my_table.draw_score(score_left, score_right) 
        

window.bind("<Up>", ball.move_up)
window.bind("<Left>", ball.move_left)
window.bind("<space>", restart_game)
game_flow()

window.mainloop()
