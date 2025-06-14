from tkinter import *

root=Tk()
root.title("Botões")


#criamos os botões
botao1= Button(root, text="Botão 1")
botao1.pack(pady=10) #organizamos os botões com o PACK, com PADDING (espaço entre elementos) VERTICAL (no eixo y)

botao2= Button(root, text="Botão 2")
botao2.pack(pady=10)

botao3= Button(root, text="Botão 3")
botao3.pack(pady=10)

root.mainloop()
