import tkinter as tk 
#vai inicializar uma janela 

janela = tk.Tk ()

# Título da janela 

janela.title ('Calculadora Simples')

#armazenar o texto do display
entrada_var = tk.StringVar () 

#campo de entrada(display)
display = tk.Entry(
    janela,#janela onde o campo vai aparecer 
    textvariable= entrada_var, # conecta o campo a variavél
    font= ("Impact",25),# Define a fonte e tamanho 
    justify="right" # Alinhs o texto a direita

)

display.pack(fill="both",padx=45,pady=90)# Adiciona o display ma jamela com espaçamento


#criar botões, cada botão adiciona um número ou operador

tk.Button (janela , text = "7",command = lambda : entrada_var.set (entrada_var.get()+"7")).pack(side = "left"),
tk.Button (janela , text = "8",command = lambda : entrada_var.set (entrada_var.get()+"8")).pack(side = "left"),
tk.Button (janela , text = "9",command = lambda : entrada_var.set (entrada_var.get()+"9")).pack(side = "left"),
tk.Button (janela , text = "/",command = lambda : entrada_var.set (entrada_var.get()+"/")).pack(side = "left"),


tk.Button (janela , text = "4",command = lambda : entrada_var.set (entrada_var.get()+"4")).pack(side = "left"),
tk.Button (janela , text = "5",command = lambda : entrada_var.set (entrada_var.get()+"5")).pack(side = "left"),
tk.Button (janela , text = "6",command = lambda : entrada_var.set (entrada_var.get()+"6")).pack(side = "left"),
tk.Button (janela , text = "*",command = lambda : entrada_var.set (entrada_var.get()+"*")).pack(side = "left"),

tk.Button (janela , text = "1",command = lambda : entrada_var.set (entrada_var.get()+"1")).pack(side = "left"),
tk.Button (janela , text = "2",command = lambda : entrada_var.set (entrada_var.get()+"2")).pack(side = "left"),
tk.Button (janela , text = "3",command = lambda : entrada_var.set (entrada_var.get()+"3")).pack(side = "left"),
tk.Button (janela , text = "-",command = lambda : entrada_var.set (entrada_var.get()+"-")).pack(side = "left"),

tk.Button (janela , text = "0",command = lambda : entrada_var.set (entrada_var.get()+"0")).pack(side = "left"),
tk.Button (janela , text = ".",command = lambda : entrada_var.set (entrada_var.get()+".")).pack(side = "left"),

tk.Button(janela,text = "=", command = lambda : entrada_var.set(str(eval(entrada_var.get())))).pack(side = "left")

tk.Button(janela,text = "+", command = lambda : entrada_var.set(entrada_var.get()+"+")).pack(side="left")

tk.Button(janela,text = "C", command = lambda : entrada_var.set("")).pack(side="left")

janela.mainloop()