class Rectangle:
    # Especial Methods
    def __init__(self,width, height):
        self.width = width
        self.height = height
    def __str__(self):
        obj = f"Rectangle(width={self.width}, height={self.height})"
        return obj
        
    # Class Methods

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2*(self.width + self.height)
    
    def get_diagonal(self):
        return ((self.width)**2 + (self.height)**2)**0.5
    
    def get_picture(self):
        if self.width > 50:
            return "Too big for picture."
        else:
            line = self.width * '*'
            rec_picture = ''
            for i in range(self.height):
                rec_picture += line+'\n'
            return rec_picture

    def get_amount_inside(self, shape):
        current_shape_area = self.get_area()
        argument_shape_area = shape.get_area()
        number_times = int(current_shape_area / argument_shape_area)

        return number_times

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)


    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side

