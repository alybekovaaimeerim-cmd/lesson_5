from faker import Faker

# Эта библиотека нужна для генерации случайных реалистичных данных.
fake = Faker()

name = fake.name()
email = fake.email()
address = fake.address()

print("Имя:", name)
print("Email:", email)
print("Адрес:", address)