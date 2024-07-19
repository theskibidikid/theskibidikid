from tkinter import *
from tkinter import ttk

class TemperatureConverter:
    def __init__(self):
        self.units = ["Celsius", "Fahrenheit", "Kelvin"]

    def convert(self, from_temp, to_temp, amount):
        if from_temp == 'Fahrenheit':
            if to_temp == 'Celsius':
                amount = amount - 32
                amount = amount * 5/9
            elif to_temp == 'Kelvin':
                amount = amount - 32
                amount = amount * 5/9 + 273.15

        elif to_temp == 'Fahrenheit':
            if from_temp == 'Celsius':
                amount = amount * 9/5
                amount = amount + 32
            elif from_temp == 'Kelvin':
                amount = amount - 273.15
                amount = amount * 9/5 + 32

        elif from_temp == 'Celsius':
            if to_temp == 'Kelvin':
                amount = amount + 273.15

        elif from_temp == 'Kelvin':
            if to_temp == 'Celsius':
                amount = amount - 273.15
        elif from_temp == to_temp:
            return amount
        return amount

class App(Tk):
    def __init__(self, converter):
        Tk.__init__(self)
        self.my_converter = converter
        self.config(bg='lightblue')
        self.geometry('800x406')
        self.title = Label(self,text="Temperature Converter")
        self.title.config(font=('Courier',15))
        self.title.place(x=300,y=5)
        self.entry_box = Entry(self,bd=3,justify=CENTER)
        self.entry_box.place(x=350,y=80)
        self.from_unit_list = StringVar(self)
        self.from_unit_list.set('Celsius')
        self.to_unit_list = StringVar(self)
        self.to_unit_list.set('Fahrenheit')
        font = ('Courier',12)
        self.option_add('*TCombobox*Listbox.font',font)
        self.from_unit_dropdown = ttk.Combobox(self,textvariable=self.from_unit_list,value=list(self.my_converter.units))
        self.to_unit_dropdown = ttk.Combobox(self,textvariable=self.to_unit_list,value=list(self.my_converter.units))
        self.from_unit_dropdown.place(x=250,y=50)
        self.to_unit_dropdown.place(x=400,y=50)
        self.result = Label(self,text='')
        self.result.config(font=('Arial',12,'bold'))
        self.result.place(x=380,y=200)
        self.convert_button = Button(self,text='Convert',fg='black',bg='yellow',command=self.do_convert)
        self.convert_button.config(font=('Arial',10))
        self.convert_button.place(x=380,y=120)

    def do_convert(self):
        amount = float(self.entry_box.get())
        from_temp = self.from_unit_dropdown.get()
        to_temp= self.to_unit_dropdown.get()
        converted_amount = self.my_converter.convert(from_temp,to_temp,amount)
        self.result.config(text=str(converted_amount))


my_converter = TemperatureConverter()
#print(my_converter.convert("Celsius","Kelvin",25))
App(my_converter)
mainloop()
