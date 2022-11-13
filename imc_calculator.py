from tkinter import * 

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Cálculo do IMC - Índice de Massa Corporal")

        self.name = Label(master, text="Nome do paciente:")
        self.name.grid(row=0, column=0, pady = 5, padx = 10)

        self.adress = Label(master, text="Endereço Completo:")
        self.adress.grid(row=1, column=0, pady = 5, padx = 10)

        self.label_height = Label(master, text="Altura (m):")
        self.label_height.grid(row=2, column=0, pady = 5, padx = 10)

        self.label_weight = Label(master, text="Peso (kg):")
        self.label_weight.grid(row=3, column=0, pady = 5, padx = 10)

        self.label_result = Label(master, text="Resultado:")
        self.label_result.grid(row=2, column=2)

        self.name = Entry(master)
        self.name.grid(row=0, column=1, pady = 5)

        self.adress = Entry(master)
        self.adress.grid(row=1, column=1)

        self.entry_height = Entry(master)
        self.entry_height.grid(row=2, column=1)

        self.entry_weight = Entry(master)
        self.entry_weight.grid(row=3, column=1)

        self.entry_result = Entry(master)
        self.entry_result.grid(row=2, column=3, ipady = 20)

        self.button_calculate = Button(master, text="Calcular", command=self.calculate)
        self.button_calculate.grid(row=6, column=1, pady = 20, padx = 20)

        self.restart_button = Button(master, text="Reiniciar", command=self.restart)
        self.restart_button.grid(row=6, column=2, pady = 20, padx = 20)

        self.close_button = Button(master, text="Fechar", command=self.quit)
        self.close_button.grid(row=6, column=3, pady = 20, padx = 20)

    def quit(self):
        self.master.quit()

    def restart(self):
        self.name.delete(0, END)
        self.adress.delete(0, END)
        self.entry_height.delete(0, END)
        self.entry_weight.delete(0, END)
        self.entry_result.delete(0, END)

    def calculate(self):
        height = float(self.entry_height.get())
        weight = float(self.entry_weight.get())
        result = weight / (height * height)
        self.entry_result.delete(0, END)
        if result < 17:
            self.entry_result.insert(0, "Muito abaixo do peso")
        elif result >= 17 and result < 18.5:
            self.entry_result.insert(0, "Abaixo do peso")
        elif result >= 18.5 and result < 25:
            self.entry_result.insert(0, "Peso normal")
        elif result >= 25 and result < 30:
            self.entry_result.insert(0, "Acima do peso")
        elif result >= 30 and result < 35:
            self.entry_result.insert(0, "Obesidade I")
        elif result >= 35 and result < 40:
            self.entry_result.insert(0, "Obesidade II (severa)")
        elif result >= 40:
            self.entry_result.insert(0, "Obesidade III (mórbida)")


root = Tk()
Calculator(root)
root.mainloop()