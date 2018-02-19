import table

class Obj:
    def __init__(self, table, width = 100, height = 15, x_posn = 50,
                 y_posn = 50, color = "red", x_speed = 50, y_speed = 50):
        self.width = width
        self.height = height
        self.x_posn = x_posn
        self.color = color
        self.x_start = x_posn
        self.y_start = y_posn
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.table = table
        self.rectangle = self.table.draw_rectangle(self)

    def move_up(self, master):
        self.y_posn = self.y_posn - self.y_speed
        if(self.y_posn <= 0):
            self.y_posn = 0
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2)

    def move_down(self, master):
        self.y_posn = self.y_posn + self.y_speed
        far_bottom = self.table.height - self.height
        if(self.y_posn >= far_bottom):
            self.y_posn = far_bottom
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2)

    def move_right(self, master):
        self.x_posn = self.x_posn + self.x_speed
        if(self.x_posn >= far_right):
            self.x_posn = far_right
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_rectangle(self.rectangle, x1, y1, x2, y2)

    def move_right(self, master):
        self.x_posn = self.x_posn + self.x_speed
        if(self.x_posn >= far_right):
            self.x_posn = far_right
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_rectangle(self.rectangle, x1, y1, x2, y2)

    def start_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start

    def detect_collision(self, ball, sides_sweet_spot = True, topnbottom_sweet_spot = False):
        collision_direction = " "
        collision = False
        feel = 5
        top = self.y_posn
        bottom = self.y_posn + self.height
        left = self.x_posn
        right = self.x_posn + self.width
        v_center = top + (self.height/2)
        h_center = left + (self.width/2)

        if(x_posn <= 3):
            collision = True
            collision_direction = "E"
        if(x_posn >= 997):
            collision = True
            collision_direction = "W"
        

            
        

        
