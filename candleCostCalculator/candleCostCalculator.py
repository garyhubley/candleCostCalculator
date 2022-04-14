import tkinter as tk
from tkinter import filedialog, Text
import os
from item import *
from field import *

# create app window
app = tk.Tk()
app.title('Candle Cost Calculator')

def caclulate_cost():
	wax_ppu = float(wax_price_field.text.get()) / float(wax_weight_field.text.get())


# items: 
wax = Item(name = 'Wax', unit = Unit.POUND)
wax_price_field = Field(app=app, label=wax.orderPriceText(), row=0, col=0)
wax_weight_field = Field(app=app, label=wax.orderUnitText(), row=0, col=2)

jar = Item(name = 'Jar', unit = Unit.EACH)
jar_price_field = Field(app=app, label=jar.orderPriceText(), row=1, col=0)
jar_quantity_field =Field(app=app, label=jar.orderUnitText(), row=1, col=2)

lid = Item(name = 'Lid', unit = Unit.EACH)
lid_price_field = Field(app=app, label=lid.orderPriceText(), row=2, col=0)
lid_quantity_field =Field(app=app, label=lid.orderUnitText(), row=2, col=2)

wick = Item(name = 'Wick', unit = Unit.EACH)
wick_price_field = Field(app=app, label=wick.orderPriceText(), row=3, col=0)
wick_quantity_field =Field(app=app, label=wick.orderUnitText(), row=3, col=2)

label = Item(name = 'label', unit = Unit.EACH)
label_price_field = Field(app=app, label=label.orderPriceText(), row=4, col=0)
label_quantity_field =Field(app=app, label=label.orderUnitText(), row=4, col=2)

frag = Item(name = 'FO', unit = Unit.OUNCE)
frag_price_field = Field(app=app, label=frag.orderPriceText(), row=5, col=0)
frag_quantity_field =Field(app=app, label=frag.orderUnitText(), row=5, col=2)

calc_btn = tk.Button(app, text='Calculate', width=10, command=caclulate_cost)
calc_btn.grid(row=6, column=3)

app.geometry('700x700')
#canvas = tk.Canvas(app, height=700, width=700, bg="#263d42")
#canvas.pack()


app.mainloop()
