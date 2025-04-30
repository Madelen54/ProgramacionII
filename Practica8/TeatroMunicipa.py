import tkinter as tk
from tkinter import messagebox
class Boleto:
    def __init__(self, numero):
        self._numero = numero
        self._precio = 0.0

    def __str__(self):
        return f"Número: {self._numero}, Precio: ${self._precio:.2f}"


class Palco(Boleto):
    def __init__(self, numero):
        super().__init__(numero)
        self._precio = 100.0


class Platea(Boleto):
    def __init__(self, numero, diasAnt):
        super().__init__(numero)
        self._precio = 50.0 if diasAnt >= 10 else 60.0


class Galeria(Boleto):
    def __init__(self, numero, diasAnt):
        super().__init__(numero)
        self._precio = 25.0 if diasAnt >= 10 else 30.0
v = tk.Tk()
v.title("Teatro Municipal")
v.geometry("500x520")
v.configure(bg="azure3")
frame1 = tk.Frame(v, width=350, height=100)
frame1.pack(pady=20)
tk.Label(frame1, text="Teatro Municipal", fg="blue", font=("Arial", 16, "bold")).pack(side="left", padx=10)
labelframe_datos = tk.LabelFrame(v, text="Datos del boleto", bg="lightBlue1", padx=10, pady=10)
labelframe_datos.pack(pady=10)

variable_control = tk.IntVar()

tk.Radiobutton(labelframe_datos, text="Palco", variable=variable_control, value=1, bg="lightBlue1").grid(row=0, column=0, padx=5, pady=5)
tk.Radiobutton(labelframe_datos, text="Platea", variable=variable_control, value=2, bg="lightBlue1").grid(row=0, column=1, padx=5, pady=5)
tk.Radiobutton(labelframe_datos, text="Galería", variable=variable_control, value=3, bg="lightBlue1").grid(row=0, column=2, padx=5, pady=5)
tk.Label(labelframe_datos, text="Número del boleto:", bg="lightBlue1").grid(row=1, column=0, padx=5, pady=10, sticky="e")
entry_numero = tk.Entry(labelframe_datos, width=10)
entry_numero.grid(row=1, column=1, padx=5, pady=10, sticky="w")

tk.Label(labelframe_datos, text="Cantidad de días para el evento:", bg="lightBlue1").grid(row=2, column=0, padx=5, pady=10, sticky="e")
entry_dias = tk.Entry(labelframe_datos, width=10)
entry_dias.grid(row=2, column=1, padx=5, pady=10, sticky="w")

labelframe_info = tk.LabelFrame(v, text="Información", bg="lightBlue1", padx=10, pady=10)
labelframe_info.pack(pady=10)

info_text = tk.Text(labelframe_info, height=4, width=50)
info_text.pack()

def vender():
    numero_str = entry_numero.get().strip()
    dias_str = entry_dias.get().strip()
    tipo = variable_control.get()

    if not numero_str or not dias_str:
        messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
        return

    try:
        numero = int(numero_str)
        dias = int(dias_str)
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos.")
        return

    if tipo == 1:
        boleto = Palco(numero)
    elif tipo == 2:
        boleto = Platea(numero, dias)
    elif tipo == 3:
        boleto = Galeria(numero, dias)
    else:
        messagebox.showwarning("Tipo no seleccionado", "Seleccione un tipo de ubicación.")
        return

    info_text.delete("1.0", tk.END)
    info_text.insert(tk.END, str(boleto))
tk.Button(labelframe_datos, text="Vender", width=12, command=vender).grid(row=3, column=0, pady=10)
tk.Button(labelframe_datos, text="Salir", width=12, command=v.quit).grid(row=3, column=1, pady=10)

v.mainloop()
