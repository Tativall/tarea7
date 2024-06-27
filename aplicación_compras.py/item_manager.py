# Cuando se incluye este módulo, permite manipular instancias de Item que son propiedad de sí mismo.

from item import Item
from tabulate import tabulate
from itertools import groupby

def items_list(self):   # Devuelve todas las instancias de Item que son propiedad de self (donde self es el propietario).
    items = [item for item in Item.item_all() if item.owner == self]
    return items

def pick_items(self, number, quantity):   # Devuelve las instancias de Item propiedad de self que corresponden al 'number' especificado y a la 'quantity' especificada.
    items = filter(lambda num: num["number"] == number, _stock(self))
    items = list(items)
    if len(items) == 0:
        return []
    elif len(items[0]["items"]) < quantity:
        return []
    else:
        return items[0]["items"][0:quantity]

def show_items(self):   # Muestra el estado del inventario de las instancias de Item propiedad de self en formato tabular con columnas ["番号", "商品名", "金額", "数量"].
    table_data = []
    for stock in _stock(self):
        table_data.append([stock['number'], stock['label']['name'], stock['label']['price'], len(stock['items'])])
    print(tabulate(table_data, headers=["番号", "商品名", "金額", "数量"], tablefmt="grid"))    # Utiliza el módulo tabulate para mostrar el resultado en formato de tabla.

def _stock(self):   # Devuelve el estado del inventario de las instancias de Item que son propiedad de self.
    item_ls = self.items_list()
    item_ls.sort(key=lambda m: m.name)
    group_list = []
    for key, group in groupby(item_ls, key=lambda m: m.name):   # Clasifica las instancias de Item que devuelven el mismo valor con Item#name.
        group_list.append(list(group))
    stock = []
    for index, item in enumerate(group_list):
        stock.append({"number": index, "label": {"name": item[0].name, "price": item[0].price}, "items": item})   # Los items contienen instancias de Item clasificadas.
    return stock
