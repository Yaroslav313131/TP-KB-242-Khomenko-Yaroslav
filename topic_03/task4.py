import bisect

lst = [1, 3, 5, 7, 9]
print("Список:", lst)

val = int(input("Введіть число для вставки: "))
pos = bisect.bisect_left(lst, val)  # знаходимо позицію для вставки
print(f"Елемент {val} слід вставити на позицію {pos}")