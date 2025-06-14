from tkinter import * #o asterisco [*] significa que importamos TUDO

root = Tk()
root.title("Labels")

label1 = Label(root, text="Label 1")
label1.pack(pady=10)

label2 = Label(root, text="Label 2")
label2.pack(pady=10)

label3 = Label(root, text="Label 3")
label3.pack(pady=10)


root.mainloop()