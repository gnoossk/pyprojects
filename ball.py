class Ball:

    def __init__(self,canvas,x,y,diameter,xVelo,yVelo,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill = color)
        self.xVelo = xVelo
        self.yVelo = yVelo

    def move(self):
        coordinates = self.canvas.coords(self.image)
        if coordinates[2]>= self.canvas.winfo_width() or coordinates [0] < 0:
           self.xVelo = -self.xVelo
        if coordinates [3] >= self.canvas.winfo_height() or coordinates[1]<0:
            self.yVelo = -self.yVelo



        self.canvas.move(self.image,self.xVelo,self.yVelo)
