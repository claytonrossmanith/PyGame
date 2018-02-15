import tkinter
import objects,ball,table

#initialise global variables
score=0

#order a window from the tkinter window factory
window=Tk()
window.title("our game")

my_table=table.Table(window,net_colour="green")
#order objects from the object factory
obj_1=obj.Obj(table=my_table,width=100,height=15,x_posn=65,y_posn=175,colour="red")
obj_2=obj.Obj(table=my_table,width=100,height=15,x_posn=100,y_posn=195,colour="red")

####functions:
def game_flow():
    global score

    #detect if the ball hits the objects:
    obj_1.detect_collision(my_ball)
    obj_2.detect_collision(my_ball)

    #detect if ball hits the top wall
    if(my_ball.y_posn>=600):
        my_ball.stop_ball()
        my_ball.start_position()
        if(score=1):
            score="You Win"
        my_table.draw_score(score)

        #add restart_ball function here
def restart_ball(master):
    global score
    my_ball.start_ball(x_speed=x_velocity,y_speed=0)
    if(score="Game Over"):
        score=score
    my_table.draw_score(score)

window.bind("<Up>",ball.move_up)
window.bind("<Right>",ball.move_right)

game_flow()
window.mainloop()
        
