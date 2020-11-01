# -*- coding: utf-8 -*-
from tkinter import Tk, Frame, BOTH


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    root.geometry("1250x1150+2000+100")
    app = Example(root)
    app.mainloop()


if __name__ == '__main__':
    main()