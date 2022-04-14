
import tkinter as tk
from enum import Enum

class Unit(Enum):
	POUND = 1
	OUNCE = 2
	GRAM = 3
	KILOGRAM = 4
	EACH = 5

class Item:
	def __init__(self, name, unit):
		self.name = name
		self.unit = unit

	def orderPriceText(self):
		return self.name + ' order price'

	def orderUnitText(self):
		return self.name + ' order quantity (' + self.unit.name + ')'

	def unitPriceText(self):
		return 'Price per ' + self.unit.name
