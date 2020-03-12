import tkinter as tk

class Application(tk.Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.pack()

        master.geometry("300x300")
        master.title("tkinter class test")

        self.canvas = tk.Canvas(master, width=300, height=300)
        self.canvas.pack()

        self.canvas.create_polygon(10,10,10,60,50,35,tag="id1")

        master.bind("<space>",self.move)

    def move(self,event):
        self.canvas.move("id1",5,5)


def main():
    win = tk.Tk()
    app = Application(master = win)
    app.mainloop()


if __name__ == "__main__":
    main()