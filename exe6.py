from tkinter import *

root=Tk()

rosa="#d93ffc"
root.title("botões com fundo")
root.wm_resizable(width=False, height=False)
root.geometry("500x400+200+200")
root.configure(bg=rosa)

def mudar_cor(color):
    root.configure(bg=color)

button1= Button(root, text="roxo", command=lambda:mudar_cor("#a59fff"))
button2= Button(root, text="verde", command=lambda:mudar_cor("#2bf6b2"))
button3= Button(root, text="azul", command=lambda:mudar_cor("#2abcf5"))
button4= Button(root, text="amarelo", command=lambda:mudar_cor("#f9ff9f"))

button1.grid(row=0, column=0, padx=10, pady=10)
button2.grid(row=0, column=1, padx=10, pady=10)
button3.grid(row=1, column=0, padx=10, pady=10)
button4.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()