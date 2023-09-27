import customtkinter as ctk
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *


# Dicionário para mapear o número do mês ao nome do mês
meses_dict = {
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
    5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
    9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
}


def adicionar_valor():
    valor = float(entry_valor.get())
    mes = list(meses_dict.keys())[
        list(meses_dict.values()).index(mes_selecionado.get())]

    valores[mes-1] = valor

    entry_valor.delete(0, tk.END)

    # Atualiza a tabela
    texto_tabela = ""
    for i, valor in enumerate(valores):
        texto_tabela += f"{meses_dict[i+1]}: {valor:.2f}\n"
  


def gerar_grafico(tipo_grafico, valores):
    # Limpa o frame_grafico antes de adicionar um novo gráfico
    
    for widget in frame_grafico.winfo_children():
        widget.destroy()

    meses = list(meses_dict.values())
    meses_abreviados = [mes[:3] for mes in meses]

    fig = Figure(figsize=(5.8, 3.8), dpi=100)
    ax = fig.add_subplot(111)

    if tipo_grafico == 'Barra':
        ax.bar(meses_abreviados, valores)
    elif tipo_grafico == 'Linha':
        ax.plot(meses_abreviados, valores)
    elif tipo_grafico == 'Dispersão':
        ax.scatter(meses_abreviados, valores)
    #elif tipo_grafico == 'Pizza':
       # ax.pie(valores, labels=meses_abreviados, autopct='%1.1f%%')

    ax.set_xlabel('Mês')
    ax.set_ylabel('Valor Gasto')
    ax.set_title('Gastos Mensais')

    ax.set_xticklabels(meses_abreviados)

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack()

    

def mostrar_tabela():
    frame_tabela.pack()
    frame_grafico.pack_forget()


def mostrar_grafico():
    frame_grafico.pack()
    frame_tabela.pack_forget()


def main():
    global entry_valor, mes_selecionado

    root = ctk.CTk()
    root.title("Registro de Gastos")
    root.geometry("600x600")
    root.iconbitmap("./assets/financa.ico")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")


    image_frame = ctk.CTkFrame(master=root, width=580, height=150)
    image_frame.place(x=10, y=10)

    bem_vindo = ctk.CTkLabel(image_frame, text='BEM-VINDO', font = ('Roboto', 30, 'bold'), text_color= ('white') )
    bem_vindo.place(x=65, y=15)


    img = PhotoImage(file="./assets/img.png")
    label_img = ctk.CTkLabel(image_frame, image=img)
    label_img.place(x=350, y=20)

    label_mes = ctk.CTkLabel(image_frame, text="Selecione o mês:")
    label_mes.place(x=25, y=55)

    mes_selecionado = ctk.CTkComboBox(image_frame, values=list(meses_dict.values()))
    mes_selecionado.place(x=25, y=80)

    label_valor = ctk.CTkLabel(image_frame, text="Digite o valor gasto:")
    label_valor.place(x=170, y=55)

    entry_valor = ctk.CTkEntry(image_frame)
    entry_valor.place(x=170, y=80)

    button_adicionar = ctk.CTkButton(
        image_frame, text="Adicionar Valor", command=adicionar_valor)
    button_adicionar.place(x=25, y=112)

    tipo_grafico = ctk.CTkComboBox(
        root, values=['Barra', 'Linha', 'Dispersão'])
    tipo_grafico.place(x=450, y=165)

    button_gerar = ctk.CTkButton(
        image_frame, text="Gerar Gráfico", command=lambda: gerar_grafico(tipo_grafico.get(), valores))
    button_gerar.place(x=170, y=112)

    global frame_tabela, frame_grafico


    frame_grafico = ctk.CTkFrame(root, width=580, height=390)
    frame_grafico.place(x=10, y=200)


    root.mainloop()


if __name__ == "__main__":
    valores = [0] * 12
    main()
