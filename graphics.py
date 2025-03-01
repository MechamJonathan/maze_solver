from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__rootWidget = Tk()
        self.__rootWidget.title = "Maze Solver"
        self.__canvas = Canvas(self.__rootWidget, bg="white", height=height, width=width)
        self.__canvas.pack(fill = BOTH, expand=1)
        self.__isRunning = False
        self.__rootWidget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__rootWidget.update_idletasks
        self.__rootWidget.update

    def wait_for_close(self):
        self.__isRunning = True
        while self.__isRunning:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__isRunning = False

class Point():
    def __init__(self):
        self.__x = 0
        self.__y = 0

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
        )
