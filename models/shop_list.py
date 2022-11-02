from models.order import *
from datetime import datetime



order1 = Order("Tom Thomas", datetime.now().strftime('%d-%m-%y %H:%M'), 1, "Book of Pizza")
order2 = Order("Jack Jackson", datetime.now().strftime('%d-%m-%y %H:%M'), 4, "Book of magic")
order3 = Order("John Johnson", datetime.now().strftime('%d-%m-%y %H:%M'), 2, "Dictionary")
order4 = Order("Richard Richardson", datetime.now().strftime('%d-%m-%y %H:%M'), 2, "Atlas")
order5 = Order("John Johnson", datetime.now().strftime('%d-%m-%y %H:%M'), 2, "Dictionary")
order6 = Order("Julie Richardson", datetime.now().strftime('%d-%m-%y %H:%M'), 2, "Atlas")
order7 = Order("Danial Davis", datetime.now().strftime('%d-%m-%y %H:%M'), 15, "Action Force Comics")
order8 = Order("Tom Jamison", datetime.now().strftime('%d-%m-%y %H:%M'), 2, "Atlas")
order9 = Order("Anne Huston", datetime.now().strftime('%d-%m-%y %H:%M'), 2, "Dictionary")
order10 = Order("Bob Tennison", datetime.now().strftime('%d-%m-%y %H:%M'), 2, "Atlas")
order11 = Order("Mary Marston", datetime.now().strftime('%d-%m-%y %H:%M'), 2, "Sherlock Holmes")
order12 = Order("Jane Janstine", datetime.now().strftime('%d-%m-%y %H:%M'), 1, "Harry Potter")
orders = [order1, order2, order3, order4, order5, order6, order7, order8, order9, order10, order11, order12]