#Умова: N студентів отримали K яблука і розподілити їх між собою порівну.
# Не поділені яблука залишились у кошику. Скільки яблук отримає кожен студент?
# Скільки яблук залишиться в кошику?
#Програма отримує числа N і K. Вона повинна вивести два числа:
# відповіді на поставлені вище питання.
#Вхідні дані: 2 цілих числа.  Кожне число користувач вводить в окремому рядку.
#Вихідні дані: вивести два числа. Перше - кількість яблук у студента, друге - кількість
#  яблук, що лишилось у кошику.

print('Enter caunter of student')
caunter_stud = int(input())
print('Enter caunter of apple')
caunter_apple = int(input())
print(caunter_apple // caunter_stud)
print(caunter_apple % caunter_stud)
