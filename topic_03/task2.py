print("Тестування методів списків \n")

# Початковий список
lst = [5, 2, 8]
print("Початковий список:", lst)

# append() – додає один елемент у кінець
lst.append(10)
print("Після append(10):", lst)

# extend() – додає кілька елементів 
lst.extend([20, 30])
print("Після extend([20, 30]):", lst)

# insert() – вставляє елемент у вказану позицію
lst.insert(1, 99)  
print("Після insert(1, 99):", lst)

# remove() – видаляє перше входження значення
lst.remove(8)
print("Після remove(8):", lst)

# copy() – створює копію списку
lst_copy = lst.copy()
print("Копія списку (copy()):", lst_copy)

# sort() – сортує список за зростанням
lst.sort()
print("Після sort():", lst)

# reverse() – розвертає список
lst.reverse()
print("Після reverse():", lst)

# clear() – очищає список
lst.clear()
print("Після clear():", lst)