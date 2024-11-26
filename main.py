import phrases
import prices

from phrases import client

print(f"Вітаємо у ресторані \"Дача\", {client}!")

borsch = input('Скільки тарілок борщу ви хочете?:>> ').strip()
borsch_quantity = float(borsch)
borsch_price = 50
total_borsch = borsch_quantity * borsch_price

dumplings = input('Скільки порцій вареників ви хочете?:>> ').strip()
dumplings_quantity = int(dumplings)
dumplings_price = 60
total_dumplings = dumplings_quantity * dumplings_price

cutlets = input('Скільки порцій котлет ви хочете?:>> ').strip()
cutlets_quantity = int(cutlets)
cutlets_price = 70
total_cutlets = cutlets_quantity * cutlets_price

salad = input('Скільки порцій салату ви хочете?:>> ').strip()
salad_quantity = float(salad)
salad_price = 40
total_salad = salad_quantity * salad_price

compote = input('Скільки чашок компоту ви хочете?:>> ').strip()
compote_quantity = float(compote)
compote_price = 20
total_compote = compote_quantity * compote_price

discount = 0.15

random = ('*' * 50)
receipt = ('=' * 50)
receipt2 = ('YOUR RECEIPT!')
print(f"Ось ваш чек, {client}!")
print(random)
print(receipt)
print(receipt2)
discount_think = 0.15
without_discount = total_borsch + total_dumplings + total_cutlets + total_salad + total_compote
discount = without_discount * discount_think
total_discount = without_discount - discount

print('today is special 15% discount!!')
print(without_discount)
print(total_discount)
print(receipt)
print(random)
