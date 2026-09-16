import customtkinter as ctk
ctk.set_appearance_mode('white')


# janela ----------------

janela = ctk.CTk()
janela.geometry('500x400')
janela.resizable(False, False)
janela.title('APP VIAGEM')
janela.iconbitmap('car_23773.ico')

# corpo da janela ------------------
titulo = ctk.CTkLabel(janela,
                      text="APP VIAGEM",
                      text_color='black',
                      font=("Verdanna", 35,('bold')))

titulo.pack(pady=30)


# caixa de texto 1 -----------------
dstviagem = ctk.CTkEntry(janela,
                         width=400,
                         height=40,
                         border_color="black",
                         placeholder_text="Digite a distância da viagem em KM",)

dstviagem.pack(pady=10)


# caixa de texto 2 -----------------
consumo = ctk.CTkEntry(janela,
                       width=400,
                       height=40,
                       border_color='black',
                       placeholder_text='Digite o consumo do seu vehículo')

consumo.pack(pady=10)

# caixa de texto 2 -----------------
preco = ctk.CTkEntry(janela,
                       width=400,
                       height=40,
                       border_color='black',
                       placeholder_text='Preço do combustível')

preco.pack()

botao = ctk.CTkButton(janela,
                       width=320,
                       height=40,
                       text='Calcular',
                       cursor='heart',
                       border_color='black',
                       font=('arial', 30),
                       border_width=2)
botao.pack(pady=50)
janela.mainloop()