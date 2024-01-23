# 1 APP
a = "змінна з текстом"
b = 1 # числова Змінна
c = ["a", 1, 1.25, "Слово"] # List
d = {"a": "Слово", "b": 1} # Dict
e = ("a", ) # Tuple
f = {"ss", } # Set
print(f"Тип а - {type(a)}, тип b - {type(b)}, Тип c - {type(c)}, Тип d - {type(d)}, Тип e - {type(e)}, Тип f - {type(f)}.\n")

# 2 APP
print("Перша константа", False)

# 3 APP
print(abs(-12.5), f"є рівним {abs(12.5)}")

# 4 APP
letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(f"На позиції {i} знаходиться буква {letters[i]}")

# 5 APP
A = True
print("Значить А=True" if A else "Значить А=False")

# 6 APP
A = 0
print(f"Ділимо 10/{A}")
try:
    print(f"А = 0...", 10/A)
except Exception as e:
    print("Ділення на 0. Неможна так, в школі вчились, нє?")
finally:
    A = input("Якесь число яке не дорівнює 0 напиши ")
    try:
        A = int(A)
    except:
        print("Сарянчік, але тебе не виправити. ББ")
    try:
        print(f"А так мона. Маладєц! Результат - {int(10/A)}")
    except:
        exit

# 7 APP
lasd = []
with open("D:\\STUDY OOP\\STUDY-OOP\\2laba-OOP-Hnatyk\\README.md", "r") as f:
    for line in f:
        lasd.append(line)
# Тут можна любу строку вививести as you know, або взагалі весь лист, але мені шкода терміналу і скріни будуть не красиві. Тому вивожу 14 (15) рядок, бо там норм симовли інакше будуть не панятні якісь знаки питань
print(lasd[14])

#8 APP
funct = lambda name, surname: f"{name} {surname} Дуже погано спав сьогодні. Пожалійте його, поставте 5 балів ツ"
print(funct("Віктор", "Брилінський"))

