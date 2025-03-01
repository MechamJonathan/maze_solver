from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__rootWidget = Tk()
        self.__canvas = Canvas()
        self.__isRunning = False
        self.__rootWidget.protocol("WM_DELETE_WINDOW", self.close)

        self.__rootWidget.title = "Root Widget"
        self.__canvas.pack()

    def redraw(self):
        self.__rootWidget.update_idletasks
        self.__rootWidget.update

    def wait_for_close(self):
        self.__isRunning = True
        while self.__isRunning:
            self.redraw()

    def close(self):
        self.__isRunning = False

