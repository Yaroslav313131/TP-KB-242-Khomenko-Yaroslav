print("Тестування методів словників \n")

# Початковий словник
d = {"name": "Yaroslav", "age": 19, "city": "Chernihiv"}
print("Початковий словник:", d)

# update() – додає або змінює елементи
d.update({"age": 21, "country": "Ukraine"})
print("Після update({'age': 21, 'country': 'Ukraine'}):", d)

# del – видаляє елемент за ключем
del d["city"]
print("Після del d['city']:", d)

# keys() – повертає всі ключі
print("Ключі словника (keys()):", d.keys())

# values() – повертає всі значення
print("Значення словника (values()):", d.values())

# items() – повертає пари (ключ, значення)
print("Пари ключ-значення (items()):", d.items())

# clear() – очищає словник
d.clear()
print("Після clear():", d)