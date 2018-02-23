import table

class Obj:
    def __init__(self, table, width = 15, height = 100, x_posn = 50,
                 y_posn = 50, color = "green", x_speed = 23, y_speed = 23):

        self.width = width
        self.height = height
        self.x_posn = x_posn
        self.y_posn = y_posn
        self.color = color
        self.x_start = x_posn
        self.y_start = y_posn
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.table = table
        self.rectangle = self.table.draw_rectangle(self)

    def start_objects(self, x_speed, y_speed):
        self.x_speed = x_speed if random.randint(0, 1) else x_speed
        self.y_speed = y_speed if random.randint(0, 1) else y_speed
        self,start_position()
        

    def start_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start

    def detect_collision(self, ball, topnbottom_sweet_spot=True, side_sweet_spot=False):
        collision_direction = ""
        collision = False
        feel = 5
        top = self.y_posn
        bottom = self.y_posn + self.height
        left = self.x_posn
        right = self.x_posn + self.width
        v_center = top + (self.height/2)
        h_center = left + (self.width/2)
        top_b = ball.y_posn
        bottom_b = ball.y_posn + ball.height
        left_b = ball.x_posn
        right_b = ball.x_posn + ball.width
        r = (right_b - left_b)/2
        v_center_b = top_b + r
        h_center_b = left_b + r
        if((bottom_b > top) and (top_b < bottom) and (right_b > left) and (left_b < right)):
            collision = True
            print("collision")

        if((bottom_b > top) and (top_b < bottom) and (right_b > left) and (left_b < right)):
            collision = True
        if(collision):
            if((top_b > top-r) and (bottom_b < bottom + r) and (right_b > right) and (left_b <=right)):
                collision_direction = "E"
                ball.x_speed = abs(ball.x_speed)

            elif((left_b > left-r) and (right_b < right+r) and (bottom_b > bottom) and (top_b <= bottom)):
                collision_direction = "S"
                ball.y_speed = abs(ball.y_speed)

            elif((left_b > left-r) and (right_b < right+r) and (top_b < top) and (bottom_b >= top)):
                collision_direction = "N"
                ball.y_speed = -abs(ball.y_speed)
            elif((top_b > top-r) and (bottom_b < bottom+r) and (left_b < left) and (right_b >= left)):
                collision_direction = "W"
                ball.x_speed = -abs(ball.x_speed)
            else:
                collision_direction = "miss"
            if((sides_sweet_spot == True) and (collision_direction == "W" or collision_direction == "E")):
                adjustment = (-(v_center - v_center_b))/(self.width/2)
                ball.x_speed = feel * adjustment
            if((topnbottom_sweet_spot == True) and (collision_direction == "N" or collision_direction == "S")):
                adjustment = (-(h_center - h_center_b))/(self.width/2)
                ball.x_speed = feel * adjustment
            return (collision, collision_direction)
