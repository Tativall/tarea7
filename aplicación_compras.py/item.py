from ownable import ownable

class Item(ownable):
    instances = []

    def __init__(self, name, price, owner=None):
        self.name = name
        self.price = price
        self.set_owner(owner)
        # Cuando se crea una instancia de Item (self), se almacena en una variable de clase llamada instances.
        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price}

    @staticmethod
    def item_all():
        # Devuelve las instancias ==> El método estático Item.item_all() devuelve todas las instancias de Item creadas hasta ahora.
        return Item.instances
