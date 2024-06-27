from customer import Customer
from item import Item
from seller import Seller

# Crear un vendedor
seller = Seller("DIC Coffee")

# Añadir varios artículos al inventario del vendedor
for i in range(10):
    Item("CPU", 40830, seller)
    Item("Memoria RAM", 13880, seller)  
    Item("Placa madre", 28980, seller)  
    Item("Fuente de alimentación", 8980, seller)  
    Item("Caja de PC", 8727, seller)  
    Item("Disco duro de 3.5 pulgadas", 10980, seller) 
    Item("SSD de 2.5 pulgadas", 13370, seller) 
    Item("M.2 SSD", 12980, seller)  
    Item("Refrigerador de CPU", 13400, seller)  
    Item("Tarjeta gráfica", 23800, seller)  

print("🤖 Por favor, dime tu nombre")
customer = Customer(input())

print("🏧 Ingresa la cantidad que deseas cargar en tu billetera")
customer.wallet.deposit(int(input()))

print("🛍️ Comenzando compras")
end_shopping = False
while not end_shopping:
    print("📜 Lista de productos disponibles")
    seller.show_items()

    print("️️⛏ Ingresa el número del producto que deseas")
    number = int(input())

    print("⛏ Ingresa la cantidad del producto que deseas")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 Contenido del carrito")
    customer.cart.show_items()
    print(f"🤑 Total a pagar: {customer.cart.total_amount()}")

    print("😭 ¿Deseas finalizar la compra? (sí/no)")
    end_shopping = input() == "sí"

print("💸 ¿Deseas confirmar la compra? (sí/no)")
if input() == "sí":
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ Resultados ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️Artículos de {customer.name}")
customer.show_items()
print(f"😱👛 Saldo en la billetera de {customer.name}: {customer.wallet.balance}")

print(f"📦 Inventario de {seller.name}")
seller.show_items()
print(f"😻👛 Saldo en la billetera de {seller.name}: {seller.wallet.balance}")

print("🛒 Contenido del carrito")
customer.cart.show_items()
print(f"🌚 Total a pagar: {customer.cart.total_amount()}")

print("🎉 Fin del programa")
