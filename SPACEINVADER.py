import tkinter
from tkinter import Tk, Button, Canvas,PhotoImage


class Visuel:
    def __init__(self,fenetre):
        self.image=PhotoImage(file="Image_Espace.gif")

        Quitter=Button(fenetre, text='Quitter', fg='red',command=fenetre.destroy)
        Quitter.pack()
        self.canvas()

    def canvas(self):
        canvas0 = Canvas(fenetre, width = 800, height = 700, bg = 'blue')
        canvas0.pack()
        canvas0.create_image(0, 0,anchor='nw', image = self.image)
        
        

fenetre=Tk()
fenetre.geometry('1000x800')
fenetre.title('nom')
Visuel(fenetre)
fenetre.mainloop()