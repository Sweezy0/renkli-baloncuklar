import tkinter as tk
import random
#pencere boyutları
window_width=800
window_height=600
#baloncuk özellikleri
balloon_radıus=30
colors=["red","green","blue","yellow","purple","orange","pink"]
def create_balloon(event):
    x=event.x
    y=event.y
    color=random.choice(colors)
    balloon=canvas.create_oval(x-balloon_radıus,y-balloon_radıus,x+balloon_radıus,y+balloon_radıus,fill=color)
    move_balloon(balloon)
def move_balloon(balloon):
    canvas.move(balloon,0,-1)
    y=canvas.coords(balloon)[1]
    if y>-balloon_radıus:
        window.after(10,move_balloon,balloon)
    else:
        canvas.delete(balloon)
window=tk.Tk()
window.title("Renkli Baloncuklar")
canvas=tk.Canvas(window,width=window_width,height=window_height)
canvas.pack()
canvas.bind("<Button-1>",create_balloon)
window.mainloop()