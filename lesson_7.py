import sqlite3

connection = sqlite3.connect("store.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
""")

connection.commit()


def create_product(name, price, quantity):
    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )
    connection.commit()
    print("Товар добавлен")


def read_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    for product in products:
        print(product)


def update_product(id, price):
    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (price, id)
    )
    connection.commit()
    print("Цена обновлена")


def delete_product(id):
    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (id,)
    )
    connection.commit()
    print("Товар удалён")


create_product("Ноутбук", 50000, 5)
create_product("Мышка", 1000, 10)
create_product("Клавиатура", 2000, 7)

print("\nВсе товары:")
read_products()

print("\nПосле изменения цены:")
update_product(1, 45000)
read_products()

print("\nПосле удаления:")
delete_product(2)
read_products()

connection.close()