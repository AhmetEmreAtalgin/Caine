from tkinter import *

window = Tk()
window.geometry("400x120")
window.title("Prototype")

icon = PhotoImage(file='main.png')
window.iconphoto(True,icon)
window.config(background="black")
window.config(background="#000000")

window.mainloop()

#file = str(input("Hangi Dosyayı istersin? :"))