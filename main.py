import phrases
import prices


from prices import menu
from phrases import client

borsch = input('Скільки тарілок борщу ви хочете?:>> ').strip()
borsch_quantity = int(borsch)
total_borsch = borsch_quantity * menu['Борщ']

dumplings = input('Скільки порцій вареників ви хочете?:>> ').strip()
dumplings_quantity = int(dumplings)
dumplings_price = 60
total_dumplings = dumplings_quantity * dumplings_price

cutlets = input('Скільки порцій котлет ви хочете?:>> ').strip()
cutlets_quantity = int(cutlets)
cutlets_price = 70
total_cutlets = cutlets_quantity * cutlets_price

salad = input('Скільки порцій салату ви хочете?:>> ').strip()
salad_quantity = int(salad)
salad_price = 40
total_salad = salad_quantity * salad_price

compote = input('Скільки чашок компоту ви хочете?:>> ').strip()
compote_quantity = int(compote)
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

print('Сьогодні діє спеціальна знижка 15%!!')
print(f"Клієнт: {client}")
print(f"Борщ: {borsch_quantity} тарілок x {borsch_price} грн/тарілка = {total_borsch} грн")
print(f"Вареники: {dumplings_quantity} порцій x {dumplings_price} грн/порція = {total_dumplings} грн")
print(f"Котлети: {cutlets_quantity} порцій x {cutlets_price} грн/порція = {total_cutlets} грн")
print(f"Салат: {salad_quantity} порцій x {salad_price} грн/порція = {total_salad} грн")
print(f"Компот: {compote_quantity} чашок x {compote_price} грн/чашка = {total_compote} грн")

print(f"\nЗагальна вартість без знижки: {without_discount:.2f} грн")
print(f"Знижка 15%: -{discount:.2f} грн")
print(f"Фінальна вартість: {total_discount:.2f} грн")
print(receipt)
print(random)
