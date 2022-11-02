from models.order import *
from datetime import datetime



order1 = Order("Tom Thomas", datetime.now().strftime('%d-%m-%y %H:%M'), 1, "Book of Pizza")
order2 = Order("Jack Jackson", datetime.now().strftime('%d-%m-%y %H:%M'), 4, "Book of magic")
order3 = Order("John Johnson", datetime.now().strftime('%d-%m-%y %H:%M'), 2, "Dictionary")
order4 = Order("Richard Richardson", datetime.now().strftime('%d-%m-%y %H:%M'), 2, "Atlas")
orders = [order1, order2, order3, order4]