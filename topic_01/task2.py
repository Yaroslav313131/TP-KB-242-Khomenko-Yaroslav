py = "   python very interesting   "

print("Оригінал:", repr(py))

print("strip():", repr(py.strip()))          # прибирає пробіли
print("capitalize():", repr(py.strip().capitalize()))  # перша літера велика , strip потрібен щоб поршою була літера а не пробіл
print("title():", repr(py.title()))  # кожне слово з великої літери
print("upper():", repr(py.upper()))          # усе великими літерами
print("lower():", repr(py.lower()))          # усе маленькими літерами