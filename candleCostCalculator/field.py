
import tkinter as tk


class Field:
	def __init__(self, app, label: str, row: int = 0, col: int = 0):
		self.app = app
		self.text = tk.StringVar()
		self.label = tk.Label(app, text=label, pady=10, padx=10)
		self.entry = tk.Entry(app, textvariable=self.text)
		self.set_position(row, col)

	def set_position(self, row: int, col: int):
		self.label.grid(row=row, column=col)
		self.entry.grid(row=row, column=col+1)

