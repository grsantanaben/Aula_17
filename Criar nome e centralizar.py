#___________________Exercicios

# Exercício 1: Janela Simples
# Crie uma janela simples com o Tkinter que exiba o texto "Olá, Tkinter!" 
#no centro da janela.

import tkinter as tk

janela = tk.Tk()
janela.title('Exercicio 1')
janela.geometry('400x300')

label = tk.Label(janela, text='Ola tkinter',justify='center', pady= 150)
label.pack()
janela.mainloop()


# **Exercício 2: Janela Simples
# Crie uma janela simples com o Tkinter que exiba o texto seu nome no centro da janelaimport tkinter as tk

import tkinter as tk

meunome = tk.Tk()
meunome.title('Exercicio 2')
meunome.geometry('400x300')

label = tk.Label(meunome, text='GABRIEL', justify='center', pady= 150)

label.pack()

meunome.mainloop()
