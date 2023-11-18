import tkinter as tk
from time import strftime


def atualizar():
  time = strftime('%H:%M:%M')
  label['text'] = time
  janela.after (1000, atualizar)


janela = tk.Tk()
janela.geometry('400x300')
janela.title('Relogio Digital')
janela.configure(bg='blue')


label = tk.Label(janela, font= ('bold', 50))
label.pack()

time = tk.Label (janela, background = 'red')
time.pack(anchor = 'center')

button = tk.Button(janela, text= 'Clique aqui', command = atualizar)
button.pack()


janela.mainloop()
