# Напишите программу, удаляющую из текста все слова, содержащие ""абв""
#Исходный текст: London абв is the capital абв of GB
#Результат: London is the capital of GB


txt = input("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')
