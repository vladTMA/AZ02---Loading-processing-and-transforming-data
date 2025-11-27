# main.py

# Задание: Исследование оценок учеников
# Представьте, что у вас есть таблица из 10 учеников с оценками учеников по 5 разным предметам. Вам нужно выполнить несколько шагов, чтобы проанализировать эти данные:
# 1. Самостоятельно создайте DataFrame с данными
# 2. Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно
# 3. Вычислите среднюю оценку по каждому предмету
# 4. Вычислите медианную оценку по каждому предмету
# 5. Вычислите Q1 и Q3 для оценок по математике:
# 6. Q1_math = df['Математика'].quantile(0.25)
# 7. Q3_math = df['Математика'].quantile(0.75)
# 8. Можно также попробовать рассчитать IQR
# 9. Вычислите стандартное отклонение

import pandas as pd
import matplotlib.pyplot as plt
from utils import print_section

# Ученики, предметы, оценки
data = {
    'Name': ['Anna', 'Benjamin', 'Boris', 'Brit', 'Glen', 'Helen', 'Ken', 'Kristin', 'Liz', 'Voldemar'],
    'Art': [9, 10, 10, 8, 9, 10, 8, 7, 8, 9],
    'Biology': [10, 9, 9, 10, 10, 8, 5, 10, 7, 8],
    'Mathematics': [10, 9, 8, 9, 6, 7, 8, 9, 10, 7],
    'Chemistry': [10, 9, 9, 9, 9, 4, 7, 7, 9, 10],
    'Physics': [10, 9, 9, 7, 6, 10, 4, 5, 9, 9],
}

# Создаём DataFrame
df = pd.DataFrame(data)

# Сохраняем в Excel
df.to_excel('students.xlsx', index=False)

# Читаем обратно
df2 = pd.read_excel('students.xlsx')


# Выводим результаты
print_section("Первые строки таблицы")
print(df2.head())

print_section("Средние значения")
print(df2.mean(numeric_only=True))

print_section("Медианные значения")
print(df2.median(numeric_only=True))

print_section("Стандартное отклонение")
print(df2.std(numeric_only=True))

print_section("Квартильные значения по математике")
print(df['Mathematics'].quantile([0.25, 0.75]))

# Q1, Q3 и IQR
Q1 = df['Mathematics'].quantile(0.25)
Q3 = df['Mathematics'].quantile(0.75)
IQR = Q3- Q1

print_section("Квартильный размах (IQR)")
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)


# Заголовок в консоли
print_section("График распределения оценок по предметам")

# Построение графика
plt.figure(figsize=(10, 6))  # увеличим размер для читаемости
df2.boxplot(column=['Art', 'Biology', 'Mathematics', 'Chemistry', 'Physics'])
plt.title("Распределение оценок по предметам", fontsize=14, fontweight='bold')
plt.ylabel("Оценки")
plt.xlabel("Предметы")

# Сначала сохраняем, потом показываем
plt.savefig("plot.png", dpi=300, bbox_inches="tight")
plt.show()
