from customer import Customer
from item import Item
from seller import Seller

seller = Seller("Tienda DIC")  # "DICストア" -> "Tienda DIC"
for i in range(10):
    Item("CPU", 40830, seller)
    Item("Memoria", 13880, seller)  # "メモリー" -> "Memoria"
    Item("Placa Base", 28980, seller)  # "マザーボード" -> "Placa Base"
    Item("Unidad de Fuente de Alimentación", 8980, seller)  # "電源ユニット" -> "Unidad de Fuente de Alimentación"
    Item("Caja de PC", 8727, seller)  # "PCケース" -> "Caja de PC"
    Item("HDD de 3.5 pulgadas", 10980, seller)  # "3.5インチHDD" -> "HDD de 3.5 pulgadas"
    Item("SSD de 2.5 pulgadas", 13370, seller)  # "2.5インチSSD" -> "SSD de 2.5 pulgadas"
    Item("M.2 SSD", 12980, seller)  # "M.2 SSD" -> "M.2 SSD"
    Item("Enfriador de CPU", 13400, seller)  # "CPUクーラー" -> "Enfriador de CPU"
    Item("Tarjeta Gráfica", 23800, seller)  # "グラフィックボード" -> "Tarjeta Gráfica"

print("🤖 Por favor, ingresa tu nombre")  # "🤖 あなたの名前を教えてください" -> "🤖 Por favor, ingresa tu nombre"
customer = Customer(input())

print("🏧 Por favor, ingresa la cantidad para depositar en la cartera")  # "🏧 ウォレットにチャージする金額を入力にしてください" -> "🏧 Por favor, ingresa la cantidad para depositar en la cartera"
customer.wallet.deposit(int(input()))

print("🛍️ Comenzamos con las compras")  # "🛍️ ショッピングを開始します" -> "🛍️ Comenzamos con las compras"
end_shopping = False
while not end_shopping:
    print("📜 Lista de productos")  # "📜 商品リスト" -> "📜 Lista de productos"
    seller.show_items()

    print("️️⛏ Por favor, ingresa el número del producto")  # "️️⛏ 商品番号を入力してください" -> "️️⛏ Por favor, ingresa el número del producto"
    number = int(input())

    print("⛏ Por favor, ingresa la cantidad del producto")  # "⛏ 商品数量を入力してください" -> "⛏ Por favor, ingresa la cantidad del producto"
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 Contenido del carrito")  # "🛒 カートの中身" -> "🛒 Contenido del carrito"
    customer.cart.show_items()
    print(f"🤑 Importe total: {customer.cart.total_amount()}")  # "🤑 合計金額: {customer.cart.total_amount()}" -> "🤑 Importe total: {customer.cart.total_amount()}"

    print("😭 ¿Quieres terminar las compras? (yes/no)")  # "😭 買い物を終了しますか？(yes/no)" -> "😭 ¿Quieres terminar las compras? (yes/no)"
    end_shopping = input() == "yes"

print("💸 ¿Deseas confirmar la compra? (yes/no)")  # "💸 購入を確定しますか？(yes/no)" -> "💸 ¿Deseas confirmar la compra? (yes/no)"
if input() == "yes":
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈Resultado┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")  # "୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈結果┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧" -> "୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈Resultado┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧"
print(f"🛍️ Propiedades de {customer.name}")  # "🛍️ ️{customer.name}の所有物" -> "🛍️ Propiedades de {customer.name}"
customer.show_items()
print(f"😱👛 Saldo de la cartera de {customer.name}: {customer.wallet.balance}")  # "😱👛 {customer.name}のウォレット残高: {customer.wallet.balance}" -> "😱👛 Saldo de la cartera de {customer.name}: {customer.wallet.balance}"

print(f"📦 Estado del inventario de {seller.name}")  # "📦 {seller.name}の在庫状況" -> "📦 Estado del inventario de {seller.name}"
seller.show_items()
print(f"😻👛 Saldo de la cartera de {seller.name}: {seller.wallet.balance}")  # "😻👛 {seller.name}のウォレット残高: {seller.wallet.balance}" -> "😻👛 Saldo de la cartera de {seller.name}: {seller.wallet.balance}"

print("🛒 Contenido del carrito")  # "🛒 カートの中身" -> "🛒 Contenido del carrito"
customer.cart.show_items()
print(f"🌚 Importe total: {customer.cart.total_amount()}")  # "🌚 合計金額: {customer.cart.total_amount()}" -> "🌚 Importe total: {customer.cart.total_amount()}"

print("🎉 Fin")  # "🎉 終了" -> "🎉 Fin"
